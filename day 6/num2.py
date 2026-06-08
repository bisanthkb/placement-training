def num(n):
    if n==0:
        return 200
    else:
        num(n-1)
        print(n,end=' ')
n=5
num(n)