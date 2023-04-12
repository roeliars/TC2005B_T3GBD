from django.shortcuts import render
from django.http import JsonResponse
from .models import Log
from django.db.models import Max

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def log(request):
    latest_logs = list(Log.objects.order_by('date')[:5].values())
    return JsonResponse(latest_logs, safe=False)

def charts(request):
    maxp = Log.objects.all().aggregate(Max('points'))
    pointList = Log.objects.all().order_by('date')
    ctx = {'maxp': maxp["points__max"], "pointList": pointList}
    return render(request, "website/charts.html", ctx)