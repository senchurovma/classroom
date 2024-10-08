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