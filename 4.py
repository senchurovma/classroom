class Rectangle:
    def __init__(self, width, height):
        super().__setattr__('width', width)
        super().__setattr__('height', height)
    
    def __setattr__(self, key, value):
        if key not in ('width', 'height'):
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(key, value)

r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25 # Успешно
r.color = 'red'  # AttributeError: Local attributes are not allowed

print(r.__dict__)
