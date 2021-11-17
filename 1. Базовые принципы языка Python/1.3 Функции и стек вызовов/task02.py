n, k = map(int, input().split())


def foo(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    else:
        return foo(n - 1, k) + foo(n - 1, k - 1)
    
    
c = foo(n, k)
print(c)