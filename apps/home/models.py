# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
# Projectsと、その小モデルTasks
class Projects(models.Model):
    
    def __str__(self):
        return self.question_text

    def objects.get(pk):

        # ...

        

class Tasks(models.Model):
    STATUS_LIST = ((0, '待機'), (1, '取組中'), (2, '完了'))

    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_task')
    taskName = models.CharField(max_length=100, verbose_name='タスク')
    status = models.IntegerField(choices=STATUS_LIST, verbose_name='状況')
    createdDate = models.DateTimeField(default=now, null=True, blank=True, verbose_name='開始日')
    deadline = DateTimeField(blank=True,null=True, verbose_name='締め切り')
    finishedDate = DateTimeField(blank=True,null=True, verbose_name='達成した日')

'''
