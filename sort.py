def sort(p):
    n=len(p)
    for j in range(n):
        for i in range(n-j-1):
            if(p[i]>=p[i+1]):
                tmp=p[i]
                p[i]=p[i+1]
                p[i+1]=tmp

a=[]
a = [int(item) for item in input("Enter the numbers to sort: ").split()]
sort(a)

for i in a:
    print(i)