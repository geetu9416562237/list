a=[76,4,5,7,3,9,4,534,53,5,2,354,3]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
        # print("even",a[i])
    else:
        c.append(a[i])
        # print("odd",a[i])
    i=i+1
print("even",b)
print("odd",c)
    



