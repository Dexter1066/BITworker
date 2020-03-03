import random
Age = random.randint(0, 100)
count = 0
print('You have three guesses.')
while True:
    if count == 0 or count % 3 != 0:
        Guess = eval(input("Please input your guess: "))
        if Guess == Age:
            print("Congratulations!")
            break
        elif Guess < Age:
            print("Too small!")
            count += 1
        elif Guess > Age:
            print("Too big!")
            count += 1
    elif count % 3 == 0:
        print ('Would you like another round?')
        answer = input()
        if answer == 'Y' or answer == 'y':
            count = 0
            continue
        if answer == 'N' or answer == 'n':
            break
