def collatz_check(num):
    iterations=1
    while(num!=1):
        if num%2==0:
            num=num/2
            iterations+=1
        else:
            num=(num*3)+1
            iterations+=1
    print(iterations)

num=int(input("Enter the number, you want to iterate for: "))
collatz_check(num)