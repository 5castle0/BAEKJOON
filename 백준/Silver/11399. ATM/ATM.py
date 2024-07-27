#11399
import sys

n= int(sys.stdin.readline())

arr=list(map(int, sys.stdin.readline().split()))

total_time=0
time=0

for i in range(len(arr)):
    time+=min(arr)
    arr.remove(min(arr))
    total_time+=time

print(total_time)