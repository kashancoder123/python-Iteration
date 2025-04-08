import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return f"What is {num1} {operation} {num2}?", correct_answer

def math_quiz():
    print("🧠 Welcome to the Easy Math Quiz for Kids!")
    score = 0
    total_questions = 5

    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i+1}: {question}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Oops! The correct answer was {correct_answer}.")
        except ValueError:
            print("⚠ Please enter a number.")

    print(f"\n🎉 You got {score} out of {total_questions} correct!")

if __name__ == "__main__":
    math_quiz()
