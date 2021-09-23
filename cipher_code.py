import string
alok={}
data=""
file=open("alok_write.txt","w")
for i in range(len(string.ascii_letters)):
    alok[string.ascii_letters[i]]=string.ascii_letters[i-1]

with open("alok_txt.txt") as f:
    while True:
        a=f.read(1)
        if not a:
            print("End of Letter")
            break
        elif a in alok:
            data = alok[a]
        else:
            data=a
        file.write(data)
file.close()