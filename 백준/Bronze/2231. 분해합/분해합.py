#2231
n=int(input())
ok=0
for i in range(1,n):
    temp=i
    result=i
    while temp>0:
        result+=temp%10
        temp//=10
    if result==n:
        print(i)
        ok=1
        break

if ok==0:
    print(0)