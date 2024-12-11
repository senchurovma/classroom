#1.2
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(len(list_players))
print(first_team)
print(second_team)

#2.2
import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
money_capital += spend - salary
for i in range(2,months+1):
    spend *= 1+increase
    money_capital += spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))

#3.1
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Определение функций
def f1(x):
    return x**3 - x

def f2(x):
    return 2*x - 1

# Разница функций для нахождения пересечений
def diff(x):
    return f1(x) - f2(x)

# Нахождение точек пересечения
x_roots = fsolve(diff, [-2, 0, 2])  # Три предположительных корня
y_roots = f1(x_roots)

x = np.linspace(-3, 3, 500)
y1 = f1(x)
y2 = f2(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y1 = x**3 - x', color='red')
plt.plot(x, y2, label='y2 = 2*x - 1', color='green')
plt.scatter(x_roots, y_roots, color='blue', label='Точки пересечения', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций y1 = x**3 - x и y2 = 2*x - 1')
plt.legend()
plt.grid(True)
plt.show()

for i in range(len(x_roots)):
    print(f"Точка пересечения {i+1}: x = {x_roots[i]:.4f}, y = {y_roots[i]:.4f}")