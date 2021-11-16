
#  l=[4,7,9,12,6,8,8,9,7,5,4,2,1,3,4,6,9]
# a=[]
# for i in l:
#     if i  not in a:
#          a.append(i)
#          for i in range(len(l)):
#             for j in range(i + 1, len(l)):
#                 if l[i] > l[j]:
#                      l[i], l[j] = l[j], l[i] 
#                      print(a)
#                      print(l)










l=[2,3,4,3,4,36,4,6,4,6,51,2,1,0,1,2,6,8,55,3,4,43,2,1,4,2,32]
a=[]
for i in l:
    if i not in a :
        a.append(i)
        b=a
        for i in range(len(b)):
            for j in range (i+1, len(b)):
                if b[i]>b[j]:
                    b[i],b[j]=b[j],b[i]
print(b)