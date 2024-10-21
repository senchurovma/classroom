#5
n = 3
m = 4
arr = list()
for i in range(n):
  brr = list()
  for i in range(m):
    brr.append(int(input()))
  arr.append(brr)
print(arr)

smax = 0
smin = 1000
v1 = 0
v2 = 0
for i in arr:
  for j in i:
    v1 += j
    v2 += j
  print(v2)
  if v1 > smax:
    smax = v1
    s1 = i
  if v2 < smin:
    smin = v2
    s2 = i
  v1, v2 = 0, 0
print(s1, smax)
print(s2, smin)

#6
n = 3
m = 4
arr = list()
for i in range(n):
  brr = list()
  for i in range(m):
    brr.append(int(input()))
  arr.append(brr)
print(arr)

def chet(a):
  if a % 2 == 0:
    a = 0
  else:
    a = 1
  return a

minel = 1000
for i in arr:
  for j in range(m):
    if i[j] < minel:
      minel = i[j]
      i[j] = chet(i[j])
  minel = 1000
print(arr)