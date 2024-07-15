#1064
import math

xa,ya,xb,yb,xc,yc=map(int,input().split())

if (yb-ya)*(xc-xb)==(yc-yb)*(xb-xa): #세 점이 평행할 때, zerodivisionerror를 이항으로 곱셈처리해서 해결
    print(-1.0)                      #두 점이 같을 때 < 세 점이 평행할 때0 0 1 0 47 0
else:
    ab=math.sqrt(((xa-xb)**2)+((ya-yb)**2))
    bc=math.sqrt(((xb-xc)**2)+((yb-yc)**2))
    ca=math.sqrt(((xc-xa)**2)+((yc-ya)**2))

    longest=2*max(ab+bc,bc+ca,ca+ab)
    shortest=2*min(ab+bc,bc+ca,ca+ab)
    
    print(longest-shortest)

