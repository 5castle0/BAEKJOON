#3273
import sys

n = int(sys.stdin.readline())
data=sorted(list(map(int,sys.stdin.readline().split())))
x=int(sys.stdin.readline())
count=0

left, right = 0,n-1
while left<right:
    if data[left]+data[right]==x:
        count+=1
        left+=1
    elif data[left]+data[right]>x:
        right-=1
    else: #data[left]+data[right]<x
        left+=1
        
print(count)