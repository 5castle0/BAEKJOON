lst=set(range(1,10000))
s=set()
for i in range(1,10000):
    i1=i//1000
    i2=i//100%10
    i3=i//10%10
    i4=i%10
    s.add(i+i1+i2+i3+i4)
b=sorted(lst-s)
for i in b:
    print(i)
    