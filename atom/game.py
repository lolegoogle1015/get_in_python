import random

number = random.randint(0, 101)

while True:

    answer = input("Enter a number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Enter right number")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("The answer is smaller")
        continue
    elif user_answer < number:
        print("The answer is bigger")
        continue
    else:
        print("Yes, you are right!")
        break
