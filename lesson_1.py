import math as m
R = int(input('Введите радиус окружности в см: '))
print('Длина окружности: ',round((2*(m.pi)*R),2))
print('Площадь круга: ',round(((m.pi)*(R**2)),2))


x,y = 10,55
print(x,y)
x,y = y,x
print(x,y)


L = int(input('Введите длину маятника: '))
g = 9.81
print('Период колебаний маятника: ',round((2*(m.pi)*((L/g)**0.5))),2)
