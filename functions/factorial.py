def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
s=fact(5)
print(s)
