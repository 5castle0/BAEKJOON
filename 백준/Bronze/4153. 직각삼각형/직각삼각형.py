#4153

while 1:
    lst = list(map(int,input().split()))
    if lst[0]==0 and lst[1]==0 and lst[2]==0:
        break
    long=max(lst)
    lst.remove(long)
    if long*long==lst[0]*lst[0]+lst[1]*lst[1]:
        print("right")
    else:
        print("wrong")
