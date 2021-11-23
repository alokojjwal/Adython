p=input()
def prime(con_p):
    d=0
    if(con_p<2):
        # print("not prime")
        d=1
        return d
    else:
        for i in range(2,con_p):
            if(con_p%i==0):
                # print("not prime")
                d=1
                return d
    if(d==0):
        return d

q=len(p)
for i in range(q):
    r=p[:q-i]
    s=int(r)
    f=prime(s)
    if(f!=0):
        print("Not concatenated_prime")
        break
    
if(f==0):
    print("Concatenated prime")        