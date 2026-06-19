from django.db import models

# Create your models here.


class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField()
    dloc=models.CharField()

    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField()
    sal=models.DecimalField(max_digits=8,decimal_places=2)
    job=models.CharField()
    hiredate=models.DateField()
    comm=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return str(self.empno)




