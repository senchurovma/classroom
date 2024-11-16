import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b):
    return (((x**b)+(a**b))/(x**b))

x = np.array([i for i in range(11)])
x = np.linspace(0,10)
plt.plot(x,f(x,1,1), color = 'red', label = '1 случай')
plt.plot(x,f(x,2,1), color = 'green', label = '2 случай')
plt.plot(x,f(x,1,2), color = 'blue', label = '3 случай')
plt.grid()
plt.title('Заголовок')
plt.xlabel('ось абсцисс')
plt.ylabel('ось ординат')
plt.legend()
plt.show()