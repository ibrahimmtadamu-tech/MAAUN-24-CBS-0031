name = input("Enter your name: ")

test_bank = [
    {"question": "What is the capital of Nigeria?",
     "options": ["A. Lagos", "B. Abuja", "C. Kano"],
     "correct_answer": "B"},

    {"question": "Python is a?",
     "options": ["A. Programming language", "B. Snake only", "C. Hardware"],
     "correct_answer": "A"},

    {"question": "Which symbol is comment in Python?",
     "options": ["A. //", "B. #", "C. **"],
     "correct_answer": "B"}
]

score = 0

for q in test_bank:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A, B, C): ")

    if answer.upper() == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(test_bank))

def print_result(name, percentage):
    if percentage >= 50:
        print(f"Congratulations {name}, you passed with {percentage}%")
    else:
        print(f"Sorry {name}, you failed with {percentage}%")

print_result(name, percentage)