print("Welcome to my Computer Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okay Lets play!! :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
    
else:
    print("Incorrect!!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does SEA stand for? ")
if answer.lower() == "search engine optimization":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

print("You Got " + str(score) + " questions correct!")
print("You Got " + str((score / 4) * 100) + "%.")