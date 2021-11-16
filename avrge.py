marks = [
[78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78],

    [87, 67, 49, 68, 88]
]
sum=0
i=0
avg=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=(sum+marks[i][j])
        j+=1
    avg=sum/len(marks)
    print(avg)
    i+=1