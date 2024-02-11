from art import logo, vs
from game_data import data
import random


def rounds(score, a):
    print(logo)
    b = data[random.randint(0, len(data) - 1)]
    while a == b:
        b = data[random.randint(0, len(data) - 1)]
    print(f"Compare A: {a["name"]}, a {a["description"]} from {a["country"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]} from {b["country"]}")
    choose = input("Who has more followers? A or B? ").lower()
    while choose != "a" and choose != "b":
        choose = input("Who have more followers? A or B?").lower()
    if choose == "a":
        if a["follower_count"] >= b["follower_count"]:
            score += 1
            a = b
            print("\n\n\n\n\n")
            rounds(score, a)
        else:
            if score > 1:
                print(f"Game Over! You did {score} points!")
            else:
                print(f"Game Over! You did {score} point!")

    else:
        if b["follower_count"] > a["follower_count"]:
            score += 1
            a = b
            print("\n\n\n\n\n")
            rounds(score, a)
        else:
            if score > 1:
                print(f"Game Over! You did {score} points!")
            else:
                print(f"Game Over! You did {score} point!")


def game():
    score = 0
    a = data[random.randint(0, len(data) - 1)]
    print("start")
    rounds(score, a)
    print("\n\n\n\n\n")
    if input("Press y to play again: ").lower() == "y":
        game()


game()
