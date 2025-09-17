print("**********")
print("QUIZZ")
print("**********")
questions=[ 
{"qs":"1. Which data structure works on the principle of FIFO (First In, First Out)?","answer":"b"},
{"qs":"Which planet is known as the Red Planet?","answer":"c"},
{"qs":"Who is known as the Father of C programming language?","answer":"c"},
{"qs":"In mathematics, what is the value of π (pi) approximately?","answer":"b"},
{"qs":"Which is the largest ocean on Earth?","answer":"c"}
          ]

answers=[
["a) Stack", "b) Queue", "c) Tree", "d) Graph"],
["a) Venus", "b) Jupiter", "c) Mars", "d) Saturn"],
["a) James Gosling", "b) Bjarne Stroustrup", "c) Dennis Ritchie", "d) Ken Thompson"],
["a) 2.14", "b) 3.14", "c) 4.13", "d) 3.41"],
["a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"]

        ]

score=0
for i in range(len(questions)):
    print(questions[i]["qs"])
    for j in answers[i]:
        print(j)
    ans=input("enter teh option (a/b/c/d) in small letters : ")  
    if ans == questions[i]["answer"]:
        print("correct answer ")
        score+=1
        print(f"you got score : {score}/{i+1}")
    else:
         print("wrong answer")
         print("correct option is : ",questions[i]["answer"])
         print(f"you got score : {score}/{i+1}")
     