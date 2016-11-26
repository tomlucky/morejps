#!/user/bin/env python
# coding=utf8
from django.db import models


class FolderDate(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=512)

    def __unicode__(self):  # __str__ on Python 3
        return self.name  # 在admin配置页面，可以容易的看到名


class ContainDate(models.Model):
    name = models.CharField(max_length=255)
    folderdate = models.CharField(max_length=255)
    imgpath = models.CharField(max_length=512)
    avpath = models.CharField(max_length=1024)


    def __unicode__(self):  # __str__ on Python 3
        return self.name  # 在admin配置页面，可以容易的看到名
