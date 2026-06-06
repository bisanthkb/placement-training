s="aaaaaaabbbbbbbcccdddddddd"
c,k=1,0
res=("")
for i in range(1,len(s)):
    if s[k]==s[i]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        k=i
        c=1
res+=s[-1]+str(c)
print(res)