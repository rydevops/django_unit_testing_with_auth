from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(reqeust, *args, **kwargs):
    task_id = kwargs['task_id']
    return HttpResponse(f"Requested task id is {task_id}")

