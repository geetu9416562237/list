numbers=[50,4, 23, 56, 12, 5, 65,10, 7]
i=0
max=0
max1=0
while i<len(numbers):
    if max<numbers[i]:
        max=numbers[i]
    elif max<numbers[i]:
        max1=numbers[i]

    i=i+1
print(max) 
print(max1)
