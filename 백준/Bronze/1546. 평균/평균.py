#1546
n = int(input())
lst = list(map(int,input().split()))

best = max(lst)
total=0

for i in lst:
    total+=i/best*100

print(total/n)