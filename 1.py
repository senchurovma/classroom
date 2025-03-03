class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)



    def __setattr__(self, key, value):
        print(key, value)
        if   key == 'name' and value == '' :
            raise ValueError('Name cannot be empty!')
        elif key == 'age' and value < 0:
            raise ValueError("Age must be a positive number!")
        else:
            return object.__setattr__(self, key, value)
p = Person("John", 25)  # Успешно
p.name = "Alice"         # Успешно
p.age = 30               # Успешно
p.name = ""              # ValueError: Name cannot be empty!
p.age = -5               # ValueError: Age must be a positive number!