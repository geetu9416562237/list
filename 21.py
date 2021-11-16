a=[2,4,6,34,6,4,54]
b=[]
i=0
sum=0
while i<len(a):
    if a[i]>sum:
        b.append(a[i])
    i+=1
print(b)




# l=[4,7,9,12,6,8,8,9,7]
# a=[]
# for i in l:
#     if i  not in a:
#         a.append(i)
#         # for i in range(len(l)):
#             # for j in range(i + 1, len(l)):
#                 # if l[i] > l[j]:
#                     # l[i], l[j] = l[j], l[i]
# print(a)
# print(l)