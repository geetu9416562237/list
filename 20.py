number=[1,2,3,4,5,6,7,8,9,0,13]
i=0
m=0
while i<len(number):
	if number[i]>m:
		m=number[i]
	i=i+1
print(m)
j=0
sm=0
while j<len(number):
    if number[j]!=m:
	    if number[j]>sm :
		    sm=number[j]
    j=j+1
print(sm)
a=0
sum=0
while a<len(number):
    if number[a]!=m and number[a]!=sm:
        if number[a]>sum:
            sum=number[a]
    a+=1
print(sum)
