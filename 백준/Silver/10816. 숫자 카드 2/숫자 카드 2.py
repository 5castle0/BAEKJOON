#10816
import sys
n = int(sys.stdin.readline())
lst1=sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
lst2=list(map(int,sys.stdin.readline().split()))

n_dic = {}
for i in lst1:
    if i in n_dic:
        n_dic[i]+=1
    else:
        n_dic[i]=1

for i in lst2:
    if i in n_dic:
        print(n_dic[i],end=" ")
    else:
        print(0,end=" ")