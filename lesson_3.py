#1
n = int(input('Введите n <= 100: '))
if n > 100:
    print('Перебор.')
else:
    for i in range(1,n+1):
        print(i**3)

print('\n')

#2
for i in range(1,10):
    for j in range(1,10):
        print('{:2d}'.format(i*j),end=' ')
    print('')