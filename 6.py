import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self):
        self.h = 1e-5

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def __call__(self, x):
        if self.instance is None:
            raise ValueError("ошибка")
        f = self.instance
        return (f(x + self.h) - f(x - self.h)) / (2 * self.h)

class ExponentialFunction:
    derivative = Derivative()

    def __init__(self, a):
        self.a = a

    def __call__(self, x):
        return self.a * np.exp(x)

    def plot(self):
        x_values = np.linspace(-2, 2, 500)
        y_values = self(x_values)
        derivative_values = [self.derivative(x) for x in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label=r"$f(x) = a \cdot e^x$", color="blue")
        plt.plot(x_values, derivative_values, label=r"$f'(x)$", color="pink", linestyle="--")
        plt.title("Графики функции и её производной")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
        plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
        plt.legend()
        plt.grid(True)
        plt.show()

exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()