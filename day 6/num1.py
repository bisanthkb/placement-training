def num(n):
    if n==0:
        return
    else:
        print(n,end=" ")
        num(n-1)
n=5
num(n)