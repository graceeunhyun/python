n = int(input())
def rec(n):
    print(n)
    if n==1:
        return;
    if(n!=1):
        rec(n-1)



rec(n)
