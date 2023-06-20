lst=[]
count,total=0,0
for i in range(20):
    a,b,c=map(str,input().split())
    if c=='P':
        continue
    else:
        count+=float(b)
        if c=='A+': lst.append(4.5*float(b))
        elif c=='A0':lst.append(4.0*float(b))
        elif c=='B+':lst.append(3.5*float(b))
        elif c=='B0':lst.append(3.0*float(b))
        elif c=='C+':lst.append(2.5*float(b))
        elif c=='C0':lst.append(2.0*float(b))
        elif c=='D+':lst.append(1.5*float(b))
        elif c=='D0':lst.append(1.0*float(b))
        else: lst.append(0)
        
for i in lst:
    total+=i
print(total/count)