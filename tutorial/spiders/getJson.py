import urllib2
import json

'''
Extract specific location str
'''
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex: endIndex]



#Get news.163.com's json data
response = urllib2.urlopen(r'http://news.163.com/special/0001220O/news_json.js')
html_gbk = response.read()

# gbk-->utf8
html_utf = html_gbk.decode("gbk").encode("utf-8")

# transfer to std json format
js = GetMiddleStr(html_utf,'var data={"category":','],[]]};')
js_0 = js.replace('[','')
js_1 = js_0.replace(']','')
js_2 = js_1.replace('"news":','')
news_json ='[' + js_2 + ']'


# 'c':category  't':news title  'l':url  'p':time
hjson = json.loads(news_json, encoding ="utf-8")
for items in hjson:
    print items['l']


