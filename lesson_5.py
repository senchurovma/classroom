#1
x1,x2,y1,y2,z1,z2 = map(int, input().split())
def find(x1,x2,y1,y2,z1,z2): 
    min = 100
    a,b,c = abs(x2/x1),abs(y2/y1),abs(z2/z1)
    A = [a,b,c]
    for i in A:
        if i < min:
            min = i
    if min == a:
        print(x1,x2)
    elif min == b:
        print(y1,y2)
    else:
        print(z1,z2)
find(x1,x2,y1,y2,z1,z2)

#2
n = int(input())

def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


for i in range(1,n+1):
    if is_prime(i) and is_palindrome(i):
        print(i)