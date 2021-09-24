def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
p = int(input("Enter the number to find the factorial of it: "))
f=factorial(p)
print("The factorial of",p,"is:",f)