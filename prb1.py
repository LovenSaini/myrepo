import os
t=int(input())
a=1
c=0
h=""
while a<=t:
    i=input()
    p=input()
    if len(i)>len(p):
        print("IMPOSSIBLE")
    else:
        if i==p:
            print("0")
        else:
            if len(i)==len(p):
                print("IMPOSSIBLE")
            else:
                for j in range(0,len(p)):
                    if p[j]==i[0] and len(h)<len(i):
                        h=h+p[j]
                    else:
                        c+=1
                print(h)        
                if h==i:
                   print("CASE:",a,"=",c)
    a+=1