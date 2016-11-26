#!/user/bin/env python
# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from catchHtml import getData
from morejps.models import *


def index(req):
    folders = range(10)
    imgNames = range(10)
    folderdate = ''
    try:
        folderdate = req.GET["folderdate"]
    # # folderdate = req.GET.('folderdate')
    except IOError, e:
        print e
    datefolders = FolderDate.objects.all()
    containts_foldernames = ContainDate.objects.filter(folderdate=folderdate).values('name').distinct()
    print "containts_foldernames:: ", str(containts_foldernames.count()), "  folderdate:", folderdate
    imgsList = []
    for imgFolderName in containts_foldernames:
        print 'imgFolderName:::', imgFolderName.get('name'), " type::", type(imgFolderName)
        imgsPathList = []
        avPath = ''
        for y in ContainDate.objects.filter(name=imgFolderName.get('name')):
            print 'yyyyy', y
            imgsPathList += {y.imgpath}
            avPath = y.avpath
            # print  y.imgpath, imgsPathList
        imgsList.append({'imgfoldername': imgFolderName.get('name'), 'imgs': imgsPathList, 'avPath': avPath})

        print imgsList
    return render(req, 'index.html',
                  {'imgsList': imgsList, 'datefolders': datefolders})


def update(req):
    print "here"
    getData()
    index(req)
