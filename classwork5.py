#1
# A = []
# alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.'
# stop = 0

# def change():
#     A[0],A[len(A)-1] = A[len(A)-1],A[0]

# for i in range(int(input('Длина массива: '))):
#     i = input('Заполни массив целыми числами: ')
#     for j in i:
#         if j in alf:
#             print('Вводи целые числа! ')
#             stop = 1
#     if stop == 0:
#         i = int(i)
#         A.append(i)

# if stop == 0:
#     print(A)
#     change()
#     print(A)

#2
# A,B,C,D = map(int, input().split())

# def evk(b, d):
#     if b == 0 or d == 0: 
#          return max(b, d)
#     else:
#         if b > d:
#             return evk(b - d, d)
#         else:
#             return evk(b, d - b) 

# B,D = B/evk(B,D),D/evk(B,D)
# print(f'{int(A*D)}/{int(B*C)}')

#3
# x,y,r,p1,p2,f1,f2,l1,l2 = map(int, input().split())

# def check(x,y,r,a,b):
#     count = 0
#     if (x-a)**2 + (y-b)**2 < r**2:
#         print('Точка лежит внутри окружности')
#         count += 1
#     else:
#         print('не лежит')

# print('для P:',end='')
# check(x,y,r,p1,p2)
# print('для F:',end='')
# check(x,y,r,f1,f2)
# print('для L:',end='')
# check(x,y,r,l1,l2)

#6
s = 0
for i in range(1,int(input())+1):
    for j in str(i):
        s += int(j)
    if i == s**len(str(i)):
        print(i)
    s = 0