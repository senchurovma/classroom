#1
'''string = input().split(" ")
print(string)
count = 0
for i in string:
    if i[0] == 'е':
        print(i,end=' ')
        count += 1
print(count)'''

#2
'''count = 0
string = input()
string = string.lower()
for i in string:
    if i == ':':
        count += 1
        string = string.replace(':','%',1)
print(string,count)'''

#3
'''string = input()
string = string.lower()
count = string.count('.')
string = string.replace('.','')
print(string,count)'''

#4
'''A = []
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.'
count = -1
for i in range(10):
    i = input('Заполни массив целыми числами: ')
    for j in i:
        if j in alf:
            print('Вводи целые числа! ')
    i = int(i)
    A.append(i)
for i in range(len(A)):
    count += 1
    if count <= 9:
        if A[i] < 0 and A[i+1] < 0:
            print(A[i],A[i+1])'''

#5
'''A = []
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.'
for i in range(int(input())):
    i = input('Заполни массив целыми числами: ')
    for j in i:
        if j in alf:
            print('Вводи целые числа! ')
    i = int(i)
    A.append(i)
min = A[0]
for i in range(len(A)):
    if A[i] < min:
        min = A[i]
print(min)'''

#6
A = []
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.'
for i in range(8):
    i = input('Заполни массив целыми числами: ')
    for j in i:
        if j in alf:
            print('Вводи целые числа! ')
    i = int(i)
    A.append(i)
for i in A:
    if i < 15:
        i *= 2
print(A)