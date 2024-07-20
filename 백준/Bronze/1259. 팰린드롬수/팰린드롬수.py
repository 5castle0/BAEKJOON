#1259
while 1:
    n=input()
    if int(n)==0:
        break
    else:
        if n==n[::-1]:
            print('yes')
        else:
            print('no')