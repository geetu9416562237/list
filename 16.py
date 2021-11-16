test_list = [1,1,0,0,1]
print ("The original list is : " + str(test_list))
res = int("".join(str(x) for x in test_list), 2)
print ("The converted integer value is : " +  str(res))