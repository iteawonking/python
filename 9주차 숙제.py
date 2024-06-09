#김우준 2024133519
#1부터 5까지의 정수 리스트 만들기

number_list = []
number_list.append(1) 
number_list.append(2)
number_list.append(3) 
number_list.append(4) 
number_list.append(5)

number_list = []
for number in range(1, 6):
    number_list.append(number)

number_list = list(range(1, 6))
[1, 2, 3, 4, 5]

#1부터 5까지의 정수 리스트 만들기 – List comprehension
number_list = [number for number in range(1,6)]
[1, 2, 3, 4, 5]

#함수 적용
number_list = [number-1 for number in range(1,6)]
[0, 1, 2, 3, 4]

# 조건 적용
a_list = [number for number in range(1,6) if number % 2 == 1]
[1, 3, 5]

#List Comprehension 예제
sentence = ['I', 'Love', 'Python', 'Soooooo', 'MUCH!!!']
#함수 적용
[word.lower() for word in sentence]
['i', 'love', 'python', 'soooooo', 'much!!!']
#조건 적용
[word for word in sentence if len(word) > 6]
['Soooooo', 'MUCH!!!']
# 함수 적용하여 튜플로 저장
[(x, x ** 2, x ** 3) for x in range(10)]
[(0, 0, 0),
 (1, 1, 1),
 (2, 4, 8),
 (3, 9, 27),
 (4, 16, 64),
 (5, 25, 125),
 (6, 36, 216),
 (7, 49, 343),
 (8, 64, 512),
 (9, 81, 729)]

#List Comprehension-두 개의 for
rows = range(1,4)
cols = range(1,3)
for row in rows:
for col in cols:
print(row, col)
1 1
1 2
2 1
2 2
3 1
3 2

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
print(cell)
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)

[(i,j) for i in range(5) for j in range(i)]
[(1, 0),
 (2, 0),
 (2, 1),
 (3, 0),
 (3, 1),
 (3, 2),
 (4, 0),
 (4, 1),
 (4, 2),
 (4, 3)]

#Dictionary Comprehension
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
{'t': 2, 'l': 1, 'r': 1, 's': 1, 'e': 2}

# Set Comprehension
a_set = {number for number in range(1,6) if number % 3 == 1}
{1, 4}

# Functions
def sum(a,b):
    return a+b
sum(1,2)
3

sum(1.3,3.1)
4

sum('love','phython')
'lovephython'


#iteration - zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)


# zip을 이용하여 영어-프랑스 사전 만들기
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

list( zip(english, french) )
 [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

 dict( zip(english, french) )
 {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

# 함수 키워드 인자
# wine, entree, dessert를 받아서 딕셔너리로 만들어 반환하는 함수
def menu(wine, entree, dessert):
return {'wine': wine, 'entree': entree, 'dessert': dessert}
#함수 호출
menu(entree='beef', dessert='bagel', wine='bordeaux’)
{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}

menu('frontenac', dessert='flan', entree='fish')
{'entree': 'fish', 'dessert': 'flan', 'wine': 'frontenac'}

#기본 매개변수 값정하기
# dessert의 기본값을 정해줌
def menu(wine, entree, dessert=‘pudding’):
return {'wine': wine, 'entree': entree, 'dessert': dessert}

#함수호출
 menu('chardonnay', 'chicken')
{'dessert': pudding ’, 'wine': 'chardonnay', 'entree': 'chicken'}

#dessert 값을 입력한 경우
 menu('dunkelfelder', 'duck', 'doughnut')
{'dessert': 'doughnut', 'wine': 'dunkelfelder', 'entree': 'duck'}

#가능한 경우
def menu(price, wine='chardonnay', entree='chicken’, dessert=‘pudding’):
return {’price': price, 'wine': wine, 'entree': entree, 'dessert': dessert}
menu(100) # 1 위치 인자
menu(price=100) # 1 키워드 인자
menu(price=120, entree='beef’) # 2 키워드 인자
menu(dessert='bagel', price=110) # 2 키워드 인자
menu(‘eighty’ ‘saint-pierre’, ‘fish’) # 3 위치 인자
menu(‘hundred’ wine=‘saint-pierre’) # 1 위치 인자, 1 키워드 인자

#불가능한 경우
menu() # price에 인자가 할당이 안됨
menu(price=100, ‘saint-pierre’) # 키워드 인자 할당 후, 위치 인자
menu(100, price=120) # 같은 변수에 두 번 할당
menu(main=‘cream pasta’) # 정의되지 않은 매개변수
     
#docstring
#함수 시작 부분에 문자열을 포함하여 함수 정의에 문서를 붙일 수 있음
def echo(anything):
#'echo returns its input argument'
return anything

def print_if_true(thing, check):
    #Prints the first argument if a second argument is true.
#The operation is:
#1. Check whether the *second* argument is true.
#2. If it is, print the *first* argument.

if check:
print(thing)

#help() 함수를 호출하여 내용을 출력할수 있음
help(echo)
# help on function echo in module_main:

echo(anything)
#echo returns its input argument

print(echo._doc_) 
#echo returns its input argument

#Python library
#유용한 프로그램들을 미리 만들어 놓아 불러서 쓸 수 있게 한 것
#패키지라고도 함
#기본으로 설치되지 않는 것들은 필요할 때 설치할 수 있음    
     
import math
math.sqrt(16)
4.0

#패키지 설치
scikit-learn
$ pip install scikit-learn


