import urllib2
import json

def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex: endIndex]


response = urllib2.urlopen(r'http://comment.news.163.com/cache/newlist/news_guonei8_bbs/B17R40U90001124J_1.html')
#comment json url is encoded by utf-8
html_utf = response.read()

#transfer to std json format
js = GetMiddleStr(html_utf,'var newPostList={"newPosts":','}],')
js_0 = js.replace('"d":0,','')
js_1 = js_0.replace('"1":{','')
js_2 = js_1.replace('}},','},')
news_json = js_2 + ']'

'''
key : value
f : user location
d : news code
b : comment content
n : user name
t : time
ect
'''
hjson = json.loads(news_json, encoding ="utf-8")
for items in hjson:
    print items['b']
