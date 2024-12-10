#1 
a = input('Введите делимое: ')
b = input('Введите делитель: ')
if not ((a.replace('.','').isdigit())) or not ((b.replace('.','').isdigit())):
    print('Введите вещественные числа!')
a,b = float(a),float(b)
if b == 0:
    print('ДЕЛЕНИЕ НА НОЛЬ!!!')
else:
    print(f'Частное: {a/b}')


#2
summa = float(input('Введите сумму покупки: '))
sale = 0
if summa > 20:
    summa *= 0.65
    sale = 35
print(f'Итого к оплате: {round(summa, 2)} у.е.')
print(f'Размер скидки составил: {sale}%')


#3
month_number = int(input('Введите порядковый номер месяца: '))
if month_number < 1 or month_number > 12:
    print('Не то.')
else:
    if month_number == 12 or month_number <= 2:
        season = 'Зима'
        if month_number == 12:
            month = 'Декабрь'
        elif month_number == 1:
            month = 'Январь'
        else:
            month = 'Февраль'
    elif month_number > 2 and month_number <= 5:
        season = 'Весна'
        if month_number == 3:
            month = 'Март'
        elif month_number == 4:
            month = 'Апрель'
        else:
            month = 'Май'
    elif month_number > 5 and month_number <= 8:
        season = 'Лето'
        if month_number == 6:
            month = 'Июнь'
        elif month_number == 7:
            month = 'Июль'
        else:
            month = 'Август'
    elif month_number > 8 and month_number <= 11:
        season = 'Осень'
        if month_number == 9:
            month = 'Сентябрь'
        elif month_number == 10:
            month = 'Октябрь'
        else:
            month = 'Ноябрь'
    print(f'Название месяца: {month}')
    print(f'Время года: {season}')