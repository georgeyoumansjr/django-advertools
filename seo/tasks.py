from celery import shared_task
import os
from ydata_profiling import ProfileReport
from django.core.cache import cache

import pandas as pd
from advertools import crawl_headers, crawl, crawllogs_to_df
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

channel_layer = get_channel_layer()
@shared_task
def generateReport(group_id,df,minimal=False,title="Profile Report"):
   
    task_id = generateReport.request.id
    print("taks id in generateReport " + task_id)
    load_df = pd.read_json(df)
    
    # try:
    if minimal:
        profile = ProfileReport(load_df,minimal=True,title=title)
    else:
        profile = ProfileReport(load_df,minimal=False,title=title)
    
    try:
        profile.to_file(os.path.join('templates',"report.html"))
        async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'task_completed',
                'result': 'Report generated successfully. for Id '+ group_id
            }
        )
        return "Report Has been generated successfully"
    
    except Exception as e:
        print(e)
        async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'report_failed'
            }
        )
        return e

    # messages.success("Report Has been generated sucessfully")
    
    
    # except Exception as e:
    #     print(e)
    #     async_to_sync(channel_layer.group_send)(
    #         "group_"+group_id,
    #         {
    #             'type': 'conversion_failed',
    #         }
    #     )
    #     return "Report was not generated"




@shared_task
def add(a,b):
    return a+b


@shared_task
def serpCrawlHeaders(group_id,links:list):
    # print(links)
    links = list(links)
    # print(links)
    try:
        if os.path.exists('serp_crawl_headers_output.jl'):
            os.remove('serp_crawl_headers_output.jl')
    except PermissionError:
        return False
    

    crawl_headers(url_list=links,output_file="serp_crawl_headers_output.jl",custom_settings={'LOG_FILE': 'headerCrawl.log'})
    async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'task_completed',
                'result': 'headers crawled'
            }
        )
    serpReadDf.delay(group_id,"headers")
    df = pd.read_json('serp_crawl_headers_output.jl', lines=True)
    async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'task_completed',
                'result': 'headers crawled'
            }
        )
    return {
        "status":"completed",
        "result": df.to_json(orient="records")
    }
    
@shared_task
def serpCrawlFull(group_id,links:list):
    try:
        if os.path.exists('serp_crawl_output.jl'):
            os.remove('serp_crawl_output.jl')
    except PermissionError:
        return False
    
    task_id = serpCrawlFull.request.id
    
    crawl(url_list=links,output_file="serp_crawl_output.jl",custom_settings={'LOG_FILE': 'fullCrawl.log'})
    async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'task_completed',
                'result': 'full crawled'
            }
        )
    df = pd.read_json('serp_crawl_headers_output.jl', lines=True)

    async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'crawlRead',
                'task_id': task_id
            }
        )
    return {
        "status":"completed",
        "result": df.to_json(orient="records")
    }

@shared_task
def serpReadDf(group_id,type:str):
    if type == "headers":
        df = pd.read_json('serp_crawl_headers_output.jl', lines=True)
    else:
        df = pd.read_json('serp_crawl_output.jl', lines=True)

    data = df.to_json(orient="records")
    # print(type(data))
    async_to_sync(channel_layer.group_send)(
            "group_"+group_id,
            {
                'type': 'data_converted',
                'result': data
            }
        )

    return True
    

@shared_task
def analyzeCrawlLogs():
    logsDf = crawllogs_to_df(logs_file_path="output_file.log")

    logs_m = logsDf["message"].value_counts().to_json()
    logs_s = logsDf["status"].value_counts().to_json()
    logs_mi = logsDf["middleware"].value_counts().to_json()

    logsDf = logsDf.reset_index(drop=True).to_html(
        classes="table", justify="center"
    )

    logsDf = logsDf.replace(
        'class="dataframe table"',
        'class="table table-primary table-striped text-center"',
    )
    
    
    return {
        'logs_message': logs_m,
        'logs_status': logs_s,
        'logs_mi': logs_mi,
        'logs_dt': logsDf 
    }

