print("=== Python Quiz ===")

score = 0

answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

answer = input("2. What is 7 * 8? ")
if answer == "56":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 56.")

answer = input("3. Which programming language are you using? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Python.")

print(f"\nYour score: {score}/3")

if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")