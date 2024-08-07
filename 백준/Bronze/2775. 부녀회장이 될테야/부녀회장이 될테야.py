#2775
import sys

t= int(sys.stdin.readline())

for i in range(t):
    k= int(sys.stdin.readline()) #floor
    n= int(sys.stdin.readline()) #room
    lst=[i for i in range(1,n+1)] #index : 0~n-1
    for floor in range(k):
        for room in range(1,n):
            lst[room]=lst[room]+lst[room-1]
    print(lst[-1])
            