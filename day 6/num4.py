def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=' ')
    fun(n,m+1)
    print(m+1,end=' ')
n=5
fun(n)