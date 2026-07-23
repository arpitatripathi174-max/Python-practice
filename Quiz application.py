questions = {
    "1. What is the capital of India?": "Delhi",
    "2. Which language is used for Python programming?": "Python",
    "3. How many days are there in a week?": "7",
    "4. What is 5 + 3?": "8",
    "5. What is the largest planet in our solar system?": "Jupiter"
}

score = 0

print("===== Welcome to the Quiz =====")

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.strip().lower() == answer.lower():
        print(" Correct!\n")
        score += 1
    else:
        print(" Wrong!")
        print("Correct Answer:", answer, "\n")

print("===== Quiz Finished =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")
