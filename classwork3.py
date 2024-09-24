#1
a = float(input('Цена 1 кг конфет: '))
for i in range(1,11):
    print(f'Итого за {i} кг: {i*a}')


#2
b = float(input('Введите первое число последовательности:'))
summa = 0
count = 1
while b != 0:
        b = float(input('Введите следующее число последовательности:'))
        summa += b
        if b == 0:
            break
        count += 1
print(f'Сумма всех элементов: {summa}')
print(f'Количество элементов: {count}')


#3
A = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
result = 0
alphabet = '!F'
for i in A:
    if type(i) is int:
        result += i
    else:
        str(i)
        for j in i:
            if j in alphabet:
                continue
            else:
                result += int(j)
print(result)