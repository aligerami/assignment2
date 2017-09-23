def gcd(n,m):
    if(n%m==0):
        return m
    return gcd(m,n%m)

print(gcd(99,44))