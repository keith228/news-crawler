import re
import urllib2
import time
import datetime
import json

'''
def GetMiddleStr(content,startStr,endStr):

    patternStr = r'%s(.+?)%s'%(startStr,endStr)
    p = re.compile(patternStr,re.IGNORECASE)
    m= re.match(p,content)
    if m:
        return m.group(1)
'''


def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex: endIndex]

lastday = str(datetime.date.today() - datetime.timedelta(days=1))
year = lastday[0:4]
month = lastday[5:7]
day = lastday[8:10]

print year
print month
print day

#result = GetMiddleStr(testStr,':d','i')



'''
string_0 = '{"n":"","l":"http://v.163.com/news/"}],'
string_1 = string_0.replace('],','')
print string_1
'''





#response = urllib2.urlopen(r'http://comment.news.163.com/cache/newlist/news_guonei8_bbs/B18LQ7NT0001124J_2.html')
#html_utf = response.read()




#html_utf = html_gbk.decode("gbk").encode("utf-8")



#js = GetMiddleStr(html_utf,'var newPostList={"newPosts":',',"')

#print js

'''
js_0 = js.replace('"d":0,','')
js_1 = js_0.replace('"1":{','')
js_2 = js_1.replace('}},','},')
news_json = js_2 + ']'
'''


'''
hjson = json.loads(news_json, encoding ="utf-8")
for items in hjson:
    print items['b']
'''


'''
html_utf_uni = html_utf.decode("utf-8")
hjson = json.loads(html_utf_uni, encoding ="utf-8")
print hjson
'''


'''
print hjson['c']

print hjson['images']['large']
print hjson['summary']
'''
