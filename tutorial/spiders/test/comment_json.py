import json
import urllib2

'''
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex: endIndex]

response = urllib2.urlopen(r'view-source:news.163.com/15/0916/23/B3M09M8I00014JB5.html')
#response = urllib2.urlopen(r'http://comment.news.163.com/cache/newlist/news3_bbs/B2QPC78O00014JB6_1.html')
#comment json url is encoded by utf-8
html_utf = response.read()
#check_null = GetMiddleStr(html_utf,'var newPostList={"newPosts":',',"')

print html_utf
if check_null.decode('utf-8') != 'null' :

    #transfer to std json format
    js = GetMiddleStr(html_utf,'var newPostList={"newPosts":','}],')
    js_0 = js.replace('"d":0,','')
    js_1 = js_0.replace('"1":{','')
    js_2 = js_1.replace('}},','},')
    news_json = js_2 + ']'

    key : value
    f : user location
    d : news code
    b : comment content
    n : user name
    t : time
    ect
    hjson = json.loads(news_json, encoding ="utf-8")
    for items in hjson:
        print items['b']
        print items['p']
'''
