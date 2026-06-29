

from django.shortcuts import render
from app.models import *

from django.db.models import *


# Create your views here.

from django.db.models import Prefetch
from django.db.models.functions import Length


def  DeptToEmp(request):
    #syntax1: all dept and all employee
    QSLDEO=Dept.objects.prefetch_related('emp_set').all()
    #syntax2:particular dept but all employess
    QSLDEO=Dept.objects.prefetch_related('emp_set').filter(dloc='chicago')
    #synatax 3: particular employees with respective salaries and their department
    QSLDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='blake')))
    d={'QSLDEO':QSLDEO}
    return render(request,'DeptToEmp.html',d)




def EmpToDept(request):
    QSLEDO=Emp.objects.select_related('deptno').all()
    QSLEDO=Emp.objects.select_related('deptno').filter(empno__gt=7800)
    QSLEDO=Emp.objects.select_related('deptno').filter(deptno__dloc='chicago')
    asal=Emp.objects.aggregate(asal=Avg('sal'))['asal']
    QSLEDO=Emp.objects.select_related('deptno').filter(sal__gt=asal)
    #avg sal of dept 20

    Avgsal20=Emp.objects.select_related('deptno').filter(deptno=20).aggregate(asl=Avg('sal'))['asl']
    QSLEDO=Emp.objects.select_related('deptno').filter(sal__lt=Avgsal20)


    #comm less than sal
    QSLEDO=Emp.objects.select_related('deptno').filter(sal__gt=F('comm'))

    d={'QSLEDO':QSLEDO}
    return render(request,'EmpToDept.html',d)












