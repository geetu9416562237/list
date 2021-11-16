# l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
# i=0
# b=[]
# while i<len(l):
#     j=0
#     while j<len(l):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
#         j+=1
#     i+=1
# print(l)


a=[56,35,2,5,7,89,4,89,4]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)
