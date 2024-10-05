a = input()
n = 0
for i in a:
    if i == 'n':
        a = a.replace(i,'!',1)
        n += 1
print(a,n)