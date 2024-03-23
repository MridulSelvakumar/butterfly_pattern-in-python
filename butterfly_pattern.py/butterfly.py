n=5
sp=n-1
st=1
for i in range(n):
    for j in range(st):
        print("*",end=" ")
    for k in range(sp):
        print(" ",end=" ")
    for l in range(st):
        print("*",end=" ")
    print()
    if i<n//2:
        sp-=2
        st+=1
    else:
        sp+=2
        st-=1