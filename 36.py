mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
liststr=mainStr.split()
a=""
i=0
while i<len(liststr):
	if liststr[i]==subStr:
		a=a+"on"+" "
	else:
		a=a+liststr[i]+" "
	i+=1
print(a)		
# print(mainStr)
