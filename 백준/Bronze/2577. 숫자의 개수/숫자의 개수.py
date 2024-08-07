#2577

a=int(input())
a*=int(input())
a*=int(input())
lst=[0 for i in range(10)]
for i in str(a):
    lst[int(i)]+=1
for i in lst:
    print(i)