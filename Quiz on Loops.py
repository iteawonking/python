#Quiz on Loops 김우준 2024133519

#Number1
for i in range(-5, 6):
    print(i)

-5
-4
-3
-2
-1
0
1
2
3
4
5

#Number2
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

rock
R&B
Soundtrack
R&B
soul
pop

#Number3
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

red
yellow
green
purple
blue

#Number4
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1

10
9.5
10
8
7.5

#Number5
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

['orange', 'orange']


