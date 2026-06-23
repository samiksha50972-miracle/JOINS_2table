

from django.shortcuts import render
from app.models import *


# Create your views here.

from django.db.models import Prefetch


def  DeptToEmp(request):
    #syntax1: all dept and all employee
    QSLDEO=Dept.objects.prefetch_related('emp_set').all()
    #syntax2:particular dept but all employess
    QSLDEO=Dept.objects.prefetch_related('emp_set').filter(dloc='chicago')
    #synatax 3: particular employees with respective salaries and their department
    QSLDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='blake')))
    d={'QSLDEO':QSLDEO}
    return render(request,'DeptToEmp.html',d)






