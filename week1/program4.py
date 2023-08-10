"""Write a function that generates a simple multiplication quiz.
 The function should prompt the user with questions and provide feedback on their answers."""


import random


def multiplication_quiz():
    print("We are giving you numbers b/w 1 to 100 try to give the multiplication value: ")
    multiplicand = random.randint(1,100)
    multiplier = random.randint(1,100)
    print(f"In this question the multiplicand is : {multiplicand:.2f} and the multiplier is : {multiplier:.2f}")
    answer = multiplicand*multiplier
    answer_user = float(input("Enter the answer here (up to .2 values): "))

    if answer == answer_user:
        print("You are correct!!")
    else:
        print("Sorry you get this wrong!! ")


if __name__== "__main__":
    multiplication_quiz()
