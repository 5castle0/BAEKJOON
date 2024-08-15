L= int(input())
word = list(input())
r=31
M=1234567891
res=0

for i in range(L):
    res+=(ord(word[i])-96)*(r**i)
    
print(res%M)