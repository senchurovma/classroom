import pandas as pd
import matplotlib.pyplot as plt

file = "C:/Users/mishk/Downloads/Mall_Customers.csv"
df = pd.read_csv(file, sep='')

#2
female_income = df[df['Genre'] == 'Female']['Annual Income']
average_female_income = female_income.mean()
print(f"Средняя доходность женщин: {average_female_income}")

#3
max_expenses_by_gender = df.groupby('Genre')['Spending Score'].max()
print("Максимальные расходы по полу:")
print(max_expenses_by_gender)

#4
men = df[df['Genre'] == 'Male']
plt.scatter(men['Age'], men['Annual Income'])
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.title('Зависимость дохода от возраста для мужчин')
plt.grid(True)
plt.show()

#5
grouped = df.groupby(['Genre', 'Annual Income'])['Spending Score'].mean().unstack()
grouped.plot(kind='bar', figsize=(10, 6), color=['blue', 'red'])
plt.xlabel('Доход')
plt.ylabel('Средние расходы')
plt.title('Распределение расходов в зависимости от дохода')
plt.xticks(rotation=0)
plt.legend(title='Пол')
plt.tight_layout()
plt.show()