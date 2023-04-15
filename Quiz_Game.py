print("Welcome to Computer Quiz")

playing = input("U want to play right? ")
if playing.lower() != "yes":
    print("just go")
    quit()
else:
    print("good answer")
    score = 0
    whole = 4

answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print("wrong")
    print("just kidding. it's correct")
    score += 1
else: 
    print("u didn't have to type <yes> if u were going to fuck up anyway")
    print("-123 points from hufflepuff. idiot. (just kidding pls stay)")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else: 
    print("incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else: 
    print("incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("correct")
    score += 1
else: 
    print("incorrect")

print("You got " + str(score / whole * 100) + " %" + " questions correct. well done I guess.")

#Sources: https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=10&t=190s , first project
#Date: 14.04.23
# 1