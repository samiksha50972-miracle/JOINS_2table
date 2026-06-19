from django.shortcuts import render
from app.models import *
# Create your views here.

def empTodept(request):
    QSLEDO=Emp.objects.select_related('deptno').all()

    d={'QSLEDO':QSLEDO}
    return render(request,'empTodept.html',d)

def empTomgr(request):
    QSLEMO=Emp.objects.select_related('mgr').all()
    d={'QSLEMO':QSLEMO}
    return render(request,'empTomgr.html',d)