print("Welcome to the quiz")
print("Answer the universal truth questions")

score = 0  

answer = input("1. The sun rises in ")

if answer.lower() == "east":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")

answer1 = input("2. Earth revolves around the ")

if answer1.lower() == "sun":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")

answer2 = input("3. We breathe in ")

if answer2.lower() == "oxygen":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")

answer3 = input("4. The largest planet in our solar system is ")

if answer3.lower() == "jupiter":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")

answer4 = input("5. The currency of the European Union is the ")

if answer4.lower() == "euro":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")

print(f"Your final score is: {score}/5")
