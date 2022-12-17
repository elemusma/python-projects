playing = input("Start quiz? ")

# if playing.upper() != "yes": // .upper() would work as well because it will turn everything uppercase
if playing.lower() != "yes":
    quit()

print("Let's start quiz!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# print("You got " + str(score) + " questions correct!") # str converts the number into a string
print("You got " + str((score/4)*100) + "%.")