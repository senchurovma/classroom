#1
# n = 3
# arr = list()
# for i in range(n):
#   brr = list()
#   for i in range(n):
#     brr.append(int(input()))
#   arr.append(brr)
# print(arr)
# print(max(arr[1]))
# max3 = []
# for i in range(n):
#   for j in range(i):
#     max3.append(arr[i][2])
# print(max(max3))

#2
# n = 3
# m = 3
# arr = list()
# for i in range(n):
#   brr = list()
#   for i in range(m):
#     brr.append(int(input()))
#   arr.append(brr)
# print(arr)
# for i in range(n):
#   for j in range(m):
#     if arr[i][j] > 0:
#       arr[i][j] = 1
#     elif arr[i][j] < 0:
#       arr[i][j] = 0
# print(arr)

#3
n = 3
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
print(arr)

sum1 = 0
sum2 = 0
count = -1
for i in range(n):
  for j in range(n):
    count += 1
    if i == j:
      sum1 += arr[i][j]
    elif i == i+j-1-count:
      sum2 += arr[i][j]