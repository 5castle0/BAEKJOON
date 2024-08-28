#2309
import sys

data=[]
total=0

for i in range(9):
    height=int(sys.stdin.readline())
    data.append(height)
    total+=height

pop_list=[]
    
for i in range(9): #01234567
    for j in range(i+1,9):
        if (len(pop_list)==2):
            break
        if total-(data[i]+data[j])==100:
            pop_list.append(data[i])
            pop_list.append(data[j])
            
for i in sorted(data):
    if i in pop_list:
        continue
    print(i)