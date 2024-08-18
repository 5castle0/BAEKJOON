#1157

word =input().upper()
abc = list(set(word))
count=[]

for i in abc:
    count.append(word.count(i))
    
if count.count(max(count))>=2:
    print('?')
else:
    print(abc[count.index(max(count))])