from celery import shared_task
import os
from ydata_profiling import ProfileReport
from django.contrib import messages
import pandas as pd

@shared_task
def generateReport(df,minimal=False,title="Profile Report"):
    # messages.warning("Report generation on progress wait for completion")
    print(title +" "+ str(minimal))
    load_df = pd.read_json(df)
    try:
        if minimal:
            profile = ProfileReport(load_df,minimal=True,title=title)
        else:
            profile = ProfileReport(load_df,minimal=False,title=title)
        profile.to_file(os.path.join('templates',"report.html"))
        # messages.success("Report Has been generated sucessfully")
        return "Report Has been generated successfully"
    except Exception as e:
        print(e)
        return "Report was not generated"


@shared_task
def add(a,b):
    return a+b
