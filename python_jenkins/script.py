def hi(n):
    if n<=1:
        return 1
    return n*hi(n-1)

print(hi(6))
print(hi(9))
