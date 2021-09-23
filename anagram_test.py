def check(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
  
b="-"
d="-"
a = [item for item in input("Enter the first set for Anagram test: ").split()]
b=b.join(a)
c=list(b)
data = [x for x in c if x.isalnum()]
d=d.join(data)
s1=d.upper()    
  
b="-"
d="-"
a = [item for item in input("Enter the second set for Anagram test: ").split()]
b=b.join(a)
c=list(b)
data = [x for x in c if x.isalnum()]
d=d.join(data)
s2=d.upper()    

check(s1, s2)