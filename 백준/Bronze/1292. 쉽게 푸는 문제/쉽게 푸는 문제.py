#1292
data=[]
for i in range(1,50):
    for j in range(i):
        data.append(i)
        
a,b=map(int,input().split())
print(sum(data[a-1:b]))
        