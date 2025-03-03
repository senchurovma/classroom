class Counter:
    
    def __getattribute__(self, item):
        print(f'Доступ к атрибуту {item}')
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return None
    
    
c = Counter()
c.value = 5         # Атрибут value будет добавлен
print(c.value)      # Доступ к атрибуту value → 5
print(c.name)       # Доступ к атрибуту name → None