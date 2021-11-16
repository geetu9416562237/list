a=[1,2,3,4,5,6,7,8,9,0,12,11,13,14,15,16,18,19,33,34]
i=0
sum=0
avg=0
count=0
while i<len(a):
    sum=sum+a[i]
    avg=sum/len(a)
    count=count+len(a)
    # if a[i]%2==0:
        # print(a[i])
    i+=1
print(sum)
print(avg)
print(count)
    # else:
        # print(a[i])