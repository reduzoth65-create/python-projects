def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("the Factorial of 0:",factorial(0))
print("the Factorial of 1:",factorial(1))
print("the Factorial of 4:",factorial(4))
print("the Factorial of 5:",factorial(5))
print("the Factorial of 10:",factorial(10))