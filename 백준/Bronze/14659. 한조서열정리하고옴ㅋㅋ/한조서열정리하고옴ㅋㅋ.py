#14659

n = int(input())
lst = list(map(int,input().split()))
kill=[]
count=0
high=0
for i in lst:
    if high>i:
        count+=1
    else:
        high=i
        count=0
    kill.append(count)
        
print(max(kill))