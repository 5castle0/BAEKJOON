N,M = map(int,input().split())
lst=[[],[]]
for i in range(M):
    p,o=map(int,input().split())
    lst[0].append(p)
    lst[1].append(o)
    
a=N//6
b=N%6

lowerpackage = min(lst[0])
lowerone=min(lst[1])

total = lowerpackage*a

if lowerone*b>=lowerpackage:
    total+=lowerpackage
else:
    total+=lowerone*b

print(min(total,lowerone*N))