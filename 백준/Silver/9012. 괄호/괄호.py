#9012
t = int(input())
for i in range(t):
    n=0
    check=0
    a = input()
    while(a!=''):
        if a[0]=='(':
            n+=1
            a=a[1:]
        else:
            n-=1
            if n<0:
                check=1
                break
            a=a[1:]
    if check==0 and n==0:    
        print('YES')
    else:
        print('NO')
    
