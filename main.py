# 1-mashq
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(48, 18))  
# 2-mashq
def factorial(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return 1
    memo[n] = n * factorial(n-1, memo)
    return memo[n]

print(factorial(10))  
# 3-mashq
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(30))  
