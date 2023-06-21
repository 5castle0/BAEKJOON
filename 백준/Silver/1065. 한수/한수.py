#0621 onetry, oneself
n=int(input())
count=0

if n>=100:
    count=99
    for i in range(100,n+1):
        i1=i//100
        i2=(i%100)//10
        i3=i%10
        if i2-i1==i3-i2:
            count+=1
else: count=n
print(count)