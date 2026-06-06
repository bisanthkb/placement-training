list=[2,1,6,2,1,2,4,7,8,1,2]
k=10
r,l,s,m=0,0,0,0
while r<len(list):
    s+=list[r]
    while s>k:
        s-=list[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)