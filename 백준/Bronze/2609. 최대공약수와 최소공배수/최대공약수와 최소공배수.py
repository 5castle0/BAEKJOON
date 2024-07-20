#2609
n,m= map(int,input().split())

for i in reversed(range(1,min(n,m)+1)):
    if n%i==0 and m%i==0:
        print(i)
        print(n*m//i)
        break