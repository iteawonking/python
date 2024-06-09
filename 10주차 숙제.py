#김우준 2024133519

   #class

#계산기 더하기 기능
result=0
def adder( num):
    global result 
    result += num
    return result
print(adder(3))
print(adder(4))

print(adder(4))
7

print(adder(5))
12

#계산기 두개 필요할 때
result1=0
result2=0

def adder1( num):
    global result 1
    result1 += num
    return result1

def adder2( num):
    global result22
    result2 += num
    return result2

print(adder(3))
print(adder(4))
print(adder(3))
print(adder(7))
3
7
3
10

#계산기가 여러 개 필요 시
class Calculator:
    def _init_(self):
    self.result=0 

def adder(self,num):
    self.result +=num
    return self.result

cal1=Calculator()
cal2=Calculator()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

#클래스 변수
class Service
secret= "지구는 4006년에 멸망한다."
    an = Service()
    an.secret
    '지구는 4006년에 멸망한다.'

#클래스 변수 공유
    Service.secret
"지구는 4006년에 멸망한다."
    Service.secret='지구가 4006년에 멸망한다는 사실은 뻥이다.'
    print(an.secret)
    지구가 4006년에 멸망한다는 사실은 뻥이다.

#클래스 내부의 함수
class Service
secret="지구는 4006년에 멸망한다?"
def sum(self,a,b):
    result= a+b
    print("%s +%s = %s."%(a,b,result))

    an = Service()
    an.sum(1,1)
    1+1=2이다.

#객체 변수
class Service:
    secret = "지구는 4006년에 멸망한다"
    def setname(self,name):
        self.name= name
def sum(self,a,b):
    result= a+b
    print("%s +%s = %s."%(self.name,a,b,result))
an = Service()
an.setname("박달도사")
an.sum(1,1)
박달도사님, 1+1=2입니다

#클래스 변수와 객체 벼ㄴ수
kim=Service ()
park=Service()
kim.name="김정보"
park.name="박융합"
print(kim.name)
김정보

print(park.name)
박융합

kim.secret="비밀은 없다"
print(park.secret)
지구는 4006년 멸망한다

print(kim.secret)
비밀은 없다

service.secret
'지구는 4006년에 멸망한다'

#init

class service
secret="지구는 4006년에 멸망한다"
def__init__(self,name):
    self.name=name
    def sum(self,a,b):
        result=a+b
        print("%s +%s = %s."%(self.name,a,b,result))

        an=service("박달도사")
        an.sum(1,1)
박달도사님, 1+1=2입니다

 #사칙연산 데이터 세팅
class Fourcal:
def setdata(self,first,second):
    self.first=first
    self.second=second

    a=FourCal()
    a.setdata(4,2)

    print(a.first)
    4

    print(a,second)
    2

#더하기

class FourCal:
    def setdata(self,first,second):
    self.first=first
    self.second=second
    def sum(self):
        result=self.first+self.second
        returen result

a=forcal()
a.setdata(4,2)

print(a.sum())
6

#사칙연산 클래스

class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
a=fourcal()
b=fourcal()
a.setdata(4,2)
b.setdata(3,7)

a.sum()
6

a.mul()
8

a.sub()
2

a.div()
2.0

b.sub()
-4


#순차적 프로그래밍

import random

player1_dice = []
player2_dice = []

for i in range(3):
  player1_dice.append(random.randint(1,6))
  player2_dice.append(random.randint(1,6))

print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
  print("Draw")
elif sum(player1_dice) > sum(player2_dice):
  print("Player 1 wins")
else:
  print("Player 2 wins")

Player 1 rolled[4, 5, 3]
Player 2 rolled[5, 3, 4]

#OOP

  from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice()))
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")

Player 1 rolled[2, 6, 2]
Player 2 rolled[5, 6, 6]
