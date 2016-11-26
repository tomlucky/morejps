#!/user/bin/env python
# coding=utf8

from django.contrib import admin
from .models import *


class FolderDateAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')
    search_fields = ['name', 'path']


class ContainAdmin(admin.ModelAdmin):
    list_display = ('name', 'imgpath', 'avpath', 'folderdate')
    search_fields = ['name', 'imgpath', 'avpath']


admin.site.register(FolderDate, FolderDateAdmin)
admin.site.register(ContainDate, ContainAdmin)
