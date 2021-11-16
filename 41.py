#c = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
c=input("ent")
a=[]
i=0

while i<len(c):
    j=0
    count=0
    b=[]
    while j<len(c):
        if c[i]==c[j]:
            count=count+1
        j+=1
    b.append (c[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i+=1
print(a)

