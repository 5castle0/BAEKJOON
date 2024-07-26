#1764
import sys

n,m = map(int,sys.stdin.readline().split())

nolisten=set()
noseen=set()

for i in range(n):
    nolisten.add(sys.stdin.readline().rstrip())
for i in range(m):
    noseen.add(sys.stdin.readline().rstrip())

nolistenseen=sorted(list(nolisten&noseen))
print(len(nolistenseen))

for i in sorted(nolistenseen):
    print(i)