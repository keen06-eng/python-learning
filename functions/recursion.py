#calculating the factorial of a number
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#nth Fibbonacci number
def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

print(Fib(10))