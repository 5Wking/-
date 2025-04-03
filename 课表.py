import requests
from requests import session
import re

session=requests.session()

url = 'https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N2151'

dat = {'xnm':"2024",
      "xqm": "12",
      "kzlx": "ck",
      "xsdm":""}
resp = session.post(url,headers={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0","cookie":"JSESSIONID=DEF2CD4672F570C9346243A14EDF07C8; route=c92d6970412b30d498843820149dd3dc"},data=dat)

resp.encoding = 'utf-8'

#print(resp.text)
obj =re.compile(r'cdmc(?P<place>.*?),.*?cxbj.*?'
                r'jc(?P<class>.*?)jcor.*?'
                r'kcmc(?P<subject>.*?),.*?kcxszc.*?'
                r'xm(?P<teacher>.*?),.*?xnm.*?'
                r'xqjmc(?P<week>.*?),.*?xqm.*?'
                r'zcd(?P<weekend>.*?),.*?zfjmc',re.S)
#r'sjkcgs(?P<weekends>.*?)totalResult'
it=obj.finditer(resp.text)
for i in it:
    print("地点",i.group('place').strip())
    print("第几节", i.group('class').strip())
    print("课程",i.group('subject').strip())
    print("老师",i.group('teacher').strip())
    print("周几", i.group('week').strip())
    print("第几周", i.group('weekend').strip())
    print("-"*30)
















