#김우준 2024133519

#XML 파싱(해석)

import xml.etree.ElementTree as et
tree=et.ElementTree(file='menu.xml')
root=tree.getroot()

print(root.tag)
<menu>
<breakfast hours="7-11">
<item price="$6.00">breakfast burritors</item>
<item price="$4.00">pancakes</item>
</breakfast>
<lunch hours="11-3">
<item price="$5.00">hamburger</item>
</lunch>
<dinner hours="3-10">
<item price="8.00">spaghetti</item>
</dinner>
</menu>

#내용 프린팅
for child in root
print('tag:',child.tag,'attribute:',child.attrib)
for grandchild in child:
    print(,|ttag:',grandchild.tag,'attribute:',grand child.attrib)

#결과

tag: breakfast attributes: {'hours': '7-11'}
    tag: item attributes: {'price': '$6.00'}
    tag: item attributes: {'price': '$4.00'}
tag: lunch attributes: {'hours': '11-3'}
    tag: item attributes: {'price': '$5.00'}
tag: dinner attributes: {'hours': '3-10'}
    tag: item attributes: {'price': '$8.00'}

len(root)
3

len(root[0])
2

#tag 이름으로 찾기

lunmch = root.find("lunch")
print(lunch)
print(lunch.get("hours"))
print(lunch.keys())
print(lunch.items())

          
#태그 안에 내용 프린트

print(root[0].findall('item'))

for item in root[0].findall('item'):
          print(item.get('price'))
          print(item.text)

#jason dumps

import jsonm
j1 = {"name":"홍길동", "birth":"0525","age":30}
j1{'age':30,'birth':'0525','name':'ghdrlfehd'}
json.dumps(j1)
'{"age":30,"birth":"0525","name"::"||u bc15||uc751||uc6a9}'

#indent 옵션
print
(json.dumps(j1, indent=2)) 
{ 
"age": 30, 
"birth": "0525",
"name": "|ubc15|uc751|uc6a9"
}

#리스트나 튜플도 json 문자열로 변경 가능

json.dumps([1,2,3]) 
'[1, 2, 3]’
json.dumps((4,5,6)) 
'[4, 5, 6]'

#Json 모듈의 loads 함수를 이용, json 문자열을 파이썬 객체로 변경

j1 = {"name":"홍길동", "birth":"0525", "age": 30} 
 d1 = json.dumps(j1) 
 json.loads(d1) 
{'name': '홍길동', 'birth': '0525', 'age': 30}

# Json file – myinfo.json

{ 
"name": "홍길동", 
"birth": "0525", 
"age": 30
}

#파일 로드

with open('./myinfo.json') as f:
 data = json.load(f) 
 
 print(type(data)) 
<class 'dict’> 
 print(data) 
{'name': '홍길동', 'birth': '0525', 'age': 30

}

# html 파일 스크래핑

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

#BeautifulSoup

pip install bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)
#특징

print(bs0bj.html.prettify())
<html>
<head>
<title>
A Useful Page
</title>
</head>
<body>
<h1>
An Interesting TiTle
</h1>
<div>
Lorem ipsum dolor sit amet, consrctetur adipisicing elit, sed do ei
</div>
</body>
</html>

bsObj.h1
bsObj.html.body.h1
bsObj.body.h1
bsObj.html.h1
