#24416
n= int(input())
f1=0
f2=0

def fib(n):
    global f1
    if n==1 or n==2:
        f1+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global f2
    lst=[0 for i in range(n)]
    lst[0] = 1
    lst[1] = 1
    for i in range(2,n):
        lst[i]=lst[i-1]+lst[i-2]
        f2+=1
    return lst[n-1]

fib(n)
fibonacci(n)
    
print(f1,end=" ")
print(f2)