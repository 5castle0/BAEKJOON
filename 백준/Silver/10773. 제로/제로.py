#10773
n=int(input())

arr=[]
for i in range(n):
    a=int(input())
    if a==0:
        arr.pop()
        continue
    arr.append(a)
print(sum(arr))
    