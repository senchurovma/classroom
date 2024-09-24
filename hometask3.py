#1
n = int(input('Введите n <= 100: '))
if n > 100:
    print('Перебор.')
else:
    for i in range(1,n+1):
        print(i**3)

#2
z = ''
for x in range(1,11):
    for y in range(1,10):
        if x < 10 and x*y < 10:
            space = '    '
        elif x < 10 and x*y > 9:
            space = '   '
        elif x > 9 and x*y > 9:
            space = '  '
        z += f'{y}x{x}={x*y}{space}'
    z += '\n'
print(z)