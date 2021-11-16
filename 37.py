question_list=["How many continents are there?",
            "which is the capital of india",
            "who is the pm of india?",
            "How many colors are there in indian flag?"]
option_list=[["four","nine","seven","two"],
            ["Delhi","mumbai","Bangalore","kolkata"],
            ["Narendra Modi","Ramanath Kovind","APJ Abdul kalam","Manmohan singh"],
            ["Two","Three","Four","five"]]
option=[["four","nine"],
       ["delhi", "mumbai"],
       ["Narendra Modi","Ramanath Kovind"],
       ["two","three"]
]
solution_list=[3,1,1,2]
sul=[2,1,1,2]
# print("CO-POWERED by Dabar Amala presents,Koun Banega Crorepati")
print("wlecome to my quiz")
i=0
c=0
while i<len(question_list):
    print("your question is on screen")
    print(i+1,question_list[i])
    a=0
    while a<len(option_list):
        print(a+1,option_list[i][a])
        a+=1
    j=int(input("enter solution"))
    if j==solution_list[i]:
        print("congrats")
    elif j==5050:

        if c==0:
            sum=0
            while sum<len(option):
                print(sum+1,option[sum])
                sum+=1
            c+=1
            num=int(input("enter a value"))
            if num==sul[i]:
                print("congrats")
            else:
                print("your anser is wrong")
                break
        else:
            print("you used 5050")
            print("quit")

    i+=1
    print("won")


