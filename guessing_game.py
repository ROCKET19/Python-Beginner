secret_number = 9
guess_count = 1
flag = 0
while guess_count <= 3:
    guessed_number = int(input(f'Guess {guess_count}: '))
    guess_count+=1
    if guessed_number == secret_number:
        print('You Won!!!')
        flag = 1
        break
if flag==0:
    print("Sorry, You've Failed")
