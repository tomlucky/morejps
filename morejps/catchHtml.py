#!/user/bin/env python
# coding=utf8

import httplib2
from BeautifulSoup import BeautifulSoup
import lxml.html

from morejps.models import *

url = "xxx"


# h = httplib2.Http(".cache")


def get_html(url):
    response, content = httplib2.Http().request(url, "GET")
    # print type(content)
    return content.decode('utf-8')


# h = httplib2.Http()
#
# resp, content = h.request(url, "GET")
# print type(content)


# htmlText = get_html(url)
# urls = open("index.html", 'r').read()

# urlList = BeautifulSoup(urls.read()).findAll('a')
def saveFolderDB(name, path):
    # if FolderDate.objects.filter(name=name).count() > 0:  # no need save
    #     print "no need save: " + name
    # else:
    FolderDate.objects.create(name=name, path=path)


def saveImgsDB(name, foldername, path, avpath):
    ContainDate.objects.create(name=name, folderdate=foldername,
                               imgpath=path, avpath=avpath)


def getData():
    dom = lxml.html.fromstring(get_html(url))
    urlList = dom.xpath('.//a[@href]')
    # print "urllist:::", urlList
    for dateFolder in urlList:  # get all folders
        # print "date folder name: ", dateFolder.text, " size:", len(str(dateFolder.text))
        if len(str(dateFolder.text)) == 8:
            # print dateFolder.text
            subUrl = url + dateFolder.text

            saveFolderDB(dateFolder.text, subUrl)

            imgsFolders = lxml.html.fromstring(get_html(subUrl)).xpath('.//a[@href]')
            # print imgsFolders
            for imgFolder in imgsFolders:  # get sub folders in date
                # print "imgFolder:", imgFolder.text
                if not str(imgFolder.text).__contains__('Parent') and not str(imgFolder.text).__contains__('.'):
                    imgLinks = lxml.html.fromstring(get_html(subUrl + "/" + imgFolder.text)).xpath('.//a[@href]')
                    for imgLink in imgLinks:  # get imglinks !!!
                        # print "imgLink:", imgLink.text
                        if str(imgLink.text).__contains__('.'):
                            imgurl = subUrl + "/" + imgFolder.text + "/" + imgLink.text
                            avpath = subUrl + "/" + imgFolder.text + "/1/xml/"
                            # print "final imgLink:", imgurl
                            # if ContainDate.objects.filter(imgpath=imgurl).count() > 0:  # no need save
                            #     break
                            saveImgsDB(imgFolder.text, dateFolder.text, imgurl, avpath)

                            # break
