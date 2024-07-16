#2839
#5로 나누어지는 것
#5와 3으로 해결가능한 것
#3으로 나누어지는 것
#안되는 것
    
n = int(input())
count=0

if n%5==0:
    print(n//5)
else:
    while(n>0):
        n-=3
        count+=1
        if n%5==0:
            print(count+n//5)
            break
        elif n==1 or n==2:
            print(-1)
            break
        elif n==0:
            print(count)
            break