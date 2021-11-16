question_list=["How many continents are there?",
            "which is the capital of india",
            "who is the pm of india?",
            "How many colors are there in indian flag?"]
option_list=[["four","nine","seven","two"],
            ["Delhi","mumbai","Bangalore","kolkata"],
            ["Narendra Modi","Ramanath Kovind","APJ Abdul kalam","Manmohan singh"],
            ["Two","Three","Four","five"]]
solution_list=[3,1,1,2]
# print("CO-POWERED by Dabar Amala presents,Koun Banega Crorepati")
print("wlecome to my quiz")
i=0
while i<len(question_list):
    print("your question is on screen")
    print(question_list[i])
    a=0
    while a<len(option_list):
        print(option_list[i][a])
        a+=1
    j=int(input("enter solution"))
    if j==solution_list[i]:
        print("congrats")
    else:
        print("your ans is wrong")
        print("quit")
        break
    i+=1   
print("you won the kbc")                                                                                                         #kbc without 5050 lifeline