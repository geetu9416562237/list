size=int(input("enter a  list size"))
a=[]
for i in range (size):
    val =int(input("enter a list number"))
    a.append(val)
for i in range(size):
    for j in range(0,size-i-1):
        if a[i]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted array is")
print(a)
