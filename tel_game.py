import random
import time


def expression():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    expression = f"\t{num1} {operator} {num2}"
    return expression


def solve(exp):
    return eval(exp)


def play_game():
    print("\n \n   \t----------Inspired From Telegram Math Battle \n")
    print("\tWelcome to Math Game !")
    print(" \n \tYou have 5 seconds to solve each expression.")
    score = 0
    wrong_answers = 0

    while True:
        print("\tSolve",expression())
        exp = expression()
        result = solve(exp)
        start_time = time.time()
        user_input = input("\n\tYour answer: ")

        if time.time() - start_time > 5:
            print("Time's up!")
            break

        if int(user_input) == result:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            wrong_answers += 1
            if wrong_answers == 2:
                print("You've given two wrong answers  Game over.")
                break

    print(f"\tYour final score is: {score}")


while True:
    play_game()
    play_again = input("\tWanna play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
