#2108
import sys

n = int(sys.stdin.readline())
data =[]
dic={}

for i in range(n):
    num=int(sys.stdin.readline())
    data.append(num)
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
            
print(round(sum(data)/n)) #산술평균
print(sorted(data)[n//2]) #중앙값

mx = max(dic.values())
lst=[]
for i in dic:
    if mx==dic[i]:
        lst.append(i)
lst=sorted(lst)
if len(lst)>1:
    print(lst[1]) #최빈값
else:
    print(lst[0])
    
print(max(data)-min(data)) #범위