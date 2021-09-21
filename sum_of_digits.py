a=input("enter ")
p=int(a)
sum = 0
while p!=0:
    sum=sum+p%10
    p//=10
    
print(sum)