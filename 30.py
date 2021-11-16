l=[]
n=int(input("enter a length"))
i=0
while i<5:
    e=int(input("enter a value"))
    l.append(e)
    print("length of list",l)
i=0
k=0
while k<len(l):
    k=k+k*l[i]
    i+=1
print(l)
print(k)
if k%n==0:
    print("divisible h")
else:
    print("nhi h")