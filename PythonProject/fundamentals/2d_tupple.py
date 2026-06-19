questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
)
    
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
questionNum = 0
num = 1

for question in questions:
    print("---------------------------------------------------------------")
    print(f"{num}. {question}")
    for option in options[questionNum]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questionNum]} is the correct answer.")

    questionNum += 1
    num += 1

print("---------------------------------------------------------------")
print("                           RESULTS                             ")
print("---------------------------------------------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

scorePercent = score / len(questions) * 100
print(f"Your Score: {score}/{len(questions)} ({scorePercent}%)")