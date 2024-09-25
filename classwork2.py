a,b,c = map(float, input().split())
if a%1 != 0 or b%1 != 0 or c%1 != 0:
    print("Ошибка, вводи целые!")
else:
    if a < b and a < c:
        print(f'наименьшее a - {a}:')
    elif b < c and b < a:
        print(f'наименьшее b - {b}:')
    elif c < a and c < b:
        print(f'наименьшее c - {c}:')
    elif a == b and a < c:
        print(f'a и b меньше c - {b}')
    elif c == b and b < a:
        print(f'b и c меньше a' - {b})
    elif c == a and c < b:
        print(f'a и c меньше b' - {c})
    else:
        print('все числа равны')
if str(a) in '123':
    print(a)
elif str(b) in '123':
    print(b)
elif str(c) in '123':
    print(c)