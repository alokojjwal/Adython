def isPangram(alpha):
    if len(alpha) == 26:
        return True
    else:
        return False
 

b="-"
a = [item for item in input("Enter for Pangram test: ").split()]
b=b.join(a)
c=b.upper()
d=list(c)
e=set(d)
data = [x for x in e if x.isalnum()]
ans = isPangram(data)

if (ans):
    print("Yes, it's Pangram")
else:
    print("No, it's not a Pangram")