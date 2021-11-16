a=[76,4,5,7,3,9,4,534,53,5,2,354,3]
i=0
sum1=0
b=[]
c=[]
sum=0
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
        b.append(a[i])
        
        # print("even",a[i])
    else:
        sum1=sum1+a[i]
        c.append(a[i])
        # print("odd",a[i])
    i=i+1
print("even",sum)
print("odd",sum1)
    



