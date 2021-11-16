list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
c=[]
while i<len(list1):
    while i<len(list2):
        if list1[i]  in list2:
            c.append(list1[i])
        i+=1
    print(c)