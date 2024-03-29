from django.http import JsonResponse
from celery.result import AsyncResult
from analyse.models import DatasetFile
import pandas as pd
from seo.seoTasks.audit import audit

def getMainTaskResponse(request, task_id):
    task_resp = AsyncResult(id=task_id)
    if task_resp.state == "SUCCESS":
        data = task_resp.get()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "task failed or task-id Not found"}, status=404)


def getAnalysisTaskResponse(request, task_id):
    task_resp = AsyncResult(id=task_id)
    if task_resp.state == "SUCCESS":
        data = task_resp.get()
        return JsonResponse(data)
    else:
        return JsonResponse(
            {"error": "task failed task failed or task-id Not found"}, status=404
        )


def getKeywords(request, task_id):
    task_resp = AsyncResult(id=task_id)
    if task_resp.state == "SUCCESS":
        data = task_resp.get()
        return JsonResponse(data)
    else:
        return JsonResponse(
            {"error": "task failed task failed or task-id Not found"}, status=404
        )


def getCsvColumns(request, pid):
    dataset = DatasetFile.objects.get(id=pid)
    csv_path = dataset.file_field
    print(csv_path)
    try:
        csv_file = pd.read_csv(csv_path)
        header = csv_file.columns.to_list()
        header.pop(0)
        return JsonResponse({"result": header})
    except Exception as e:
        return JsonResponse({"result": []})
    

def makeAuditRequest(request):
    url = request.GET.get("url")
    if url:
        audit.delay("",url)
    else:
        return JsonResponse({
            "status": "failed",
            "result": "URL query is not enetered"
        })
