# -*-utifulsoup coding: utf-8 -*-

import sys, traceback
import re
import time
import datetime
import json
import urllib
import urllib2
from bs4 import BeautifulSoup

def GetMiddleStr1(content,startStr,endStr):
    patternStr = r'%s(.+?)%s'%(startStr,endStr)
    p = re.compile(patternStr,re.IGNORECASE)
    m= re.match(p,content)
    if m:
        return m.group(1)

def GetMiddleStr2(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    if endIndex < 0:
        endIndex = len(content)
    return content[startIndex: endIndex]

'''
lastday = str(datetime.date.today() - datetime.timedelta(days=1))
year = lastday[0:4]
month = lastday[5:7]
day = lastday[8:10]

#return 'http://news.163.com/special/0001220O/news_json.js'
#jsurl = 'http://snapshot.news.163.com/wgethtml/http+!!news.163.com!special!0001220O!news_json.js/'+year+'-'+month+'/'+day+'/0.js'
jsurl = 'http://snapshot.news.163.com/wgethtml/http+!!news.163.com!special!0001220O!news_json.js/2015-09/20/0.js'
# gbk-->utf8
pageSource = urllib2.urlopen(jsurl).read().decode('gbk').encode('utf-8')
# transfer to std json format
#js = GetMiddleStr(pageSource,'var data={"category":','],[]]};')
js = GetMiddleStr2(pageSource,'var data={"category":','],[]]};')
js_0 = js.replace('[','')
js_1 = js_0.replace(']','')
js_2 = js_1.replace('"news":','')
news_json ='[' + js_2 + ']'


# 'c':category  't':news title  'l':url  'p':time
hjson = json.loads(news_json, encoding ="utf-8")
print 'news size is :' +str(len(hjson))
count = 0
for items in hjson:
	count +=1
	#if count>20: break
	if count<9: continue
	#print items
	for (k, v) in items.items():
		if k == 'p': news_time = v
		if k == 'c': category = v
		#news_url = 'http://news.163.com/15/0815/19/B134PU1E000146BE.html'
        news_url = items['l']
        print news_url
'''

news_url = 'http://news.163.com/15/0815/19/B134PU1E000146BE.html'
pageSource = urllib2.urlopen(news_url).read().decode("gbk").encode("utf-8")
c = re.search(r"(?<=boardId = ).+?(?=$)",pageSource,re.M)
boardId = GetMiddleStr2(c.group(),'"','",')
print boardId


'''
url = 'http://news.163.com/15/0920/22/B406G2MQ00014AED.html'
response = urllib2.urlopen(url)
html_gbk = response.read()
html_utf = html_gbk.decode("gbk").encode("utf-8")
'''

'''
for a in filter(lambda x: x.startswith('boardId ='),html_utf.split('\n')):
	item = filter(lambda x: x.startswith('boardId ='),a.split(','))[0]
	print item
'''

#soup = BeautifulSoup(pageSourcef)
#print soup.find_all("script",attrs={"type":"text/javascript"})
#aaa = soup.find_all(text='boardId')
#aaa = soup.find_all(text=re.compile('boardId'))
#a = soup.find_all(text=re.compile("boardId"))
#a = soup.find_all("script",attrs={"type":"text/javascript"})
#b = str(a)
#pattern = re.compile('boardId',re.M)
#c = pattern.search(b)
#print html_utf
#string = 'abcdefghijklmn'
#result = GetMiddleStr(string,'a','l')
#print html_utf
#test = soup.find_all('boardID')



'''
title =  response.xpath('//div[@class="ep-content"]//h1[@id="h1title"]/text()').extract()
print title
'''
