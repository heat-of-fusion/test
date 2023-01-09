# print("Hello\nWorld")
# a = 'print("Hello/nWorld")'
# for i in a:
#     if i == '/':
#         print(' \ '.strip(), end='')
#     else:
#         print(i, end='')

# from os import sep
# a, b = map(int, input().split('-'))
# print(a, b, sep='')

# f1, f2 = map(float, input().split(', '))
# print(f1*f2)

# a = 'print("Hello/nWorld")'
# for i in a:
#     if i == '/':
#         print(' \ '.strip(), end='')
#     else:
#         print(i, end='')

# a, b = map(int, input().split(','))
# print(a, ', ', b)


# print('최종적으로 내가 가진 돈으로 노트북을 {}일 {}시간 동안 사용할 수 있다.'.format(divmod(900000 / 500)[0], divmod(900000 / 500)[1]))

# print(divmod(900000, 500)[0])

# for i in range(1, 10):
#     print('*'*i, ' '*i, '*'*i, ' '*i, '*'*i)
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# j = 10
# while j >= 0:
#     print(j)
#     j -= 2

# for 변수 in range(10, 31, 10):
# 	print(변수)
# for i in range(10, 31, 10):
#     print(i)

# amount = 30000 + 50000 + 15000 + 25000

# if amount >= 100000:
#     print('상품권을 받을 수 있습니다.')
# else:
#     print('상품권을 얻을 수 있습니다.')

# student_score = 2
# f_amount = 4

# if f_amount >= 3 or student_score < 1:
#     print('학사경고')
# else:
#     print('학사경고 아님')

# user_age = int(input('나이를 입력해주세요: '))

# if user_age >= 20:
#     print('성인')
# else:
#     print('미성년자')

# mid_term_score = int(input('중간고사 점수를 입력해주세요:'))
# task_score = int(input('과제 점수를 입력해주세요:'))
# if (mid_term_score >= 70) and (task_score == 100):
#     print('Pass')
# else:
#     print('Fail')

# print('test')
# print('test2')

# import random

# def choice(list):
#     randInt = random.randrange(1, len(list))
#     return list[randInt]

# print(choice([1, 2, 3, 4]))

# print(list('abcde'))

# a = str(input(""))

# b = 0
# a_l = 1
# while b < (len(a)-1):
#     if a[b] == a[b+1]:
#         a_l += 1
#         if b == (len(a)-2):
#             print(a[b]+str(a_l), end="")
#         elif a[b] != a[b+1]:
#             print(a[b]+str(a_l),end="")
#             a_l = 1
#             if b ==(len(a)-2):
#                 print(a[b+1]+str(a_l),end="")
#                 b += 1

#  a = [ 'test.py', 'list.docs', 'docu.hwp' ] 일 때 split() method를 사용하여 a 리스트 내의 요소들의 확장자 이름을 제거하고 문서 이름만 출력하시오.

# a = [ 'test.py', 'list.docs', 'docu.hwp' ]
# for i in a:
#     print(i.split('.')[0])

# a = int(input('정수 입력: '))
# if a % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4, 5])

# for i in range(1, 10):
    # print(i)

# arr = [3, 2, 2, 5, 1, 1, 2, 4]
# new_arr = []
# prev = 0
# prev = arr[0]
# new_arr.append(prev)
# for i in arr[1:]:
#     if i == prev:
#         prev = i
#         continue
#     else:
#         new_arr.append(i)
#     prev = i
# print(new_arr)

# a = 1

# def func(d):
#     global a
#     b = a + 2
#     c = b + d
#     print('func: ', a, b, c, d)
#     a = c
#     print('func: ', a, b, c, d)

#     return c

# print('main: ', a)
# e = func(3)
# print('main: ', a)

# import numpy as np
# from scipy.spatial import Voronoi, voronoi_plot_2d
# import matplotlib.pyplot as plt

# points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
# plt.scatter(points[:, 0], points[:, 1])
# vor = Voronoi(points)

# vor_vertices = vor.vertices
# print(vor_vertices)

# vor_regions = vor.regions
# print(vor_regions)

# fig = voronoi_plot_2d(vor)
# plt.show()

# print(list(range(12, 0, -1)))

# from datetime import datetime

# now = datetime.now()

# print(now.hour)

# import turtle as t
# t.pendown()
# t.forward(90)
# t.penup()
# t.undo()

# input()



# import turtle as t
# from datetime import datetime

# clock_r = 100

# def undo(n):
#     for i in range(n):
#         t.undo()

# def write_time(token, value):
#     manual = {'h': [12, 40, 'black', 8], 'm': [60, 80, 'blue', 4], 's': [60, 110, 'red', 2]}
#     t.color(manual[token][2])
#     t.pensize(manual[token][3])
#     t.left((360 / manual[token][0]) * (manual[token][0] - value))
#     t.pendown()
#     t.forward(manual[token][1])
#     t.penup()
#     t.left(180)
#     t.forward(manual[token][1])
#     t.right((360 / manual[token][0]) * (manual[token][0] - value) - 180)
#     t.color('black')
#     t.pensize(1)


# t.speed(10)
# t.penup()
# t.forward(100)
# t.left(90)
# t.pendown()
# t.circle(100, 360)
# t.penup()
# t.left(90)
# t.forward(100)
# t.right(90)

# for i in range(12, 0, -1):
#     t.forward(80)
#     t.write(i)
#     t.goto(0, 0)
#     t.left(360 / 12)


# now = datetime.now()

# prev_hour = now.hour
# prev_minute = now.minute

# #오전, 오후 통합
# if now.hour >= 13:
#     opti_hour = now.hour - 12
# else:
#     opti_hour = now.hour
    
# #시 표시
# write_time('h', opti_hour)

# #분 표시
# write_time('m', now.minute)

# #초 표시
# while True:
#     now_new = datetime.now()
#     if now_new.minute != prev_minute:
#         undo(11)
#         write_time('m', now_new.minute)
#         prev_minute = now_new.minute
#     if now_new.hour != prev_hour:
#         undo(22)
#         write_time('h', now_new.hour)
#         write_time('m', now_new.minute)
#         prev_hour = now_new.hour
#     write_time('s', now_new.second)
#     undo(11)


# input()



# import turtle as t
# from datetime import datetime

# #시계의 반지름을 지정해준다
# clock_r = 100

# #t.undo()를 여러번 수행할 때 활용할 함수
# def undo(n):
#     for i in range(n):
#         t.undo()

# #시간을 터틀그래픽으로 출력해주는 함수
# def write_time(token, value):
#     manual = {'h': [12, 40, 'black', 8], 'm': [60, 80, 'blue', 4], 's': [60, 110, 'red', 2]}
#     t.color(manual[token][2])
#     t.pensize(manual[token][3])
#     t.left((360 / manual[token][0]) * (manual[token][0] - value))
#     t.pendown()
#     t.forward(manual[token][1])
#     t.penup()
#     t.left(180)
#     t.forward(manual[token][1])
#     t.right((360 / manual[token][0]) * (manual[token][0] - value) - 180)
#     t.color('black')
#     t.pensize(1)

# #시계의 원을 그려준다
# t.speed(10)
# t.hideturtle()
# t.penup()
# t.goto(-65, 200)
# t.write('클릭 시 타이머로 변경됩니다.')
# t.goto(0, 0)
# t.forward(100)
# t.left(90)
# t.pendown()
# t.circle(100, 360)
# t.penup()
# t.left(90)
# t.forward(100)
# t.right(90)

# #시계 내의 숫자를 그려준다
# for i in range(12, 0, -1):
#     t.forward(80)
#     t.write(i)
#     t.goto(0, 0)
#     t.left(360 / 12)


# now = datetime.now()

# prev_hour = now.hour
# prev_minute = now.minute

# #오전, 오후 통합
# if now.hour >= 13:
#     opti_hour = now.hour - 12
# else:
#     opti_hour = now.hour
    
# #시 표시
# write_time('h', opti_hour)

# #분 표시
# write_time('m', now.minute)

# #초 표시
# while True:
#     now_new = datetime.now()
#     if now_new.minute != prev_minute:
#         undo(11)
#         write_time('m', now_new.minute)
#         prev_minute = now_new.minute
#     if now_new.hour != prev_hour:
#         undo(22)
#         write_time('h', now_new.hour)
#         write_time('m', now_new.minute)
#         prev_hour = now_new.hour
#     write_time('s', now_new.second)
#     undo(11)



# a = 'asdf'
# a += 'j'
# print(a)


# from turtle import *
# setup(500, 500)
# Screen()
# title("Turtle Keys")
# move = Turtle()
# showturtle()

# def k1():
#     move.forward(45)

# def k2():
#     move.left(45)

# def k3():
#     move.right(45)

# def k4():
#     move.back(45)

# onkey(k1, "Return")
# onkey(k2, "BackSpace")
# onkey(k3, "Right")
# onkey(k4, "Down")

# listen()
# mainloop()

# import turtle as t

# t.penup()
# t.color('red')
# t.pendown()
# t.begin_fill()
# t.pendown()
# t.forward(100)
# t.backward(100)
# t.circle(100, 50)
# t.end_fill()

# input()

# print('a' == 'a' and 'b' == 'b')

# a = '1234'
# print(a[2:])

# from datetime import datetime

# now = datetime.now()
# print(now.hour)

# import winsound
# for i in range(10):
#     winsound.Beep(frequency=440, duration=1000)
list = [1, 2, 3]
print(str(list))