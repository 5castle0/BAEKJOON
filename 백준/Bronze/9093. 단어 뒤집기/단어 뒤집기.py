a=int(input())
for i in range(a):
    string=input().split()
    for j in string:
        print(j[::-1],end=' ')