n=int(input("Enter a positive number to find the factorial of it: "))
if n<0:
    print("Not a valid number")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of",n,"is:",fact)