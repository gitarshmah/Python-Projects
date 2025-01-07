import random 

answer = random.randint(1, 101)
print("\nHi! Welcome to the Number Guessing Game\nYou will be given 7 chances to guess the number\nThe number is between 1 to 100\n")
f = False
for i in range(7):
    input_num = int(input(f"Enter the number for chance {i+1}: "))
    if input_num == answer:
        print(f"Your guessed the right number {input_num} is the answer. You win")
        f = True
        break

    elif i == 6:
        print("Unfortunately you lose")
    else:
        print("Incorrect answer try it again", end=' ')
        if input_num < answer:
             print(f"Answer is greater than your input number {input_num}")
        else:
             print(f"Answer is smaller than your input number {input_num}")    


if not f:
    print(f"The correct answer is {answer}")