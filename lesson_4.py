#1
a = input()
n = 0
for i in a:
    if i == 'н':
        a = a.replace(i,'!',1)
        n += 1
print(a,n)

#2
s = input()
x = []
z = ''
s = s.replace('[','/')
s = s.replace('(','/')
s = s.replace('{','/')
s = s.replace(']','+')
s = s.replace(')','+')
s = s.replace('}','+')
x.append(s.index('/'))
x.append(s.index('+'))
for i in range(min(x)+1, max(x)):
    z += s[i]
print(z)

#3
s = input().split(' ')
for i in s:
    if (i[0] == 'а' or i[0] == 'А') and i[len(i)-1] == 'я':
        print(i, end=' ')