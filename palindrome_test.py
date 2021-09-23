def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 

b="-"
d="-"
a = [item for item in input("Enter for Palindrome test: ").split()]
b=b.join(a)
c=list(b)
data = [x for x in c if x.isalnum()]
d=d.join(data)
s=d.upper()
ans = isPalindrome(s)
 
if (ans):
    print("Yes, it's Palindrome")
else:
    print("No, it's not a Palindrome")