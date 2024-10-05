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
A = []
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.'
for i in range(10):
    i = input('Заполни массив целыми числами: ')
    for j in i:
        if j in alf:
            print('Вводи целые числа! ')
    A.append(i)
    if i+1 <= len(A)