# --------------------------
def new_game():
    guesses = []  # Corrected the typo in 'guesses'
    correct_guesses = 0
    question_num = 0
    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter A, B, or C: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions[key], guess)  # Fixed passing the correct arguments to check_answer
        question_num += 1  # Moved the increment outside of the inner loop

    view_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0  # Added return statement


def view_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS!")
    print("------------------")

    print("Answers ", end="")
    for i in questions.values():  # Use values() to iterate through answers
        print(i, end=" ")

    print()
    print("Guesses ", end="")
    for i in guesses:
        print(i, end=" ")

    print()

    score = float(correct_guesses / len(questions) * 100)
    print("Your score is " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (YES/NO): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {"Which son of Shaji is an idiot? ": "A", "Which son of Shaji is an IITian? ": "B", "Who is Roopchand? ": "B"}

options = [["A. Roopu", "B. Roophand", "C. Sergin Garcia"],
           ["A. Roopchand", "B. Abhinand", "C. None of the above"],
           ["A. An intelligent detective", "B. A Spanish maniac who jumped from a mental hospital", "C. Nobody knows, not even himself"]]

new_game()

while play_again():
    new_game()

print("Bye")
