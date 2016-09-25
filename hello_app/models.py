# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TStudentInfo(models.Model):
    c_id = models.BigIntegerField(primary_key=True)
    c_name = models.CharField(unique=True, max_length=128)
    c_score = models.IntegerField()
    c_modify_time = models.DateTimeField()
    c_create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_student_info'

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.c_name