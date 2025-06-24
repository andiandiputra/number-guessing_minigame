import random
import os
import art

def clear():
    os.system('cls')

def play_game():
    print(art.logo)
    print('Welcome to the Number Guessing Game \nThe clue is a number between 1 to 100')
    
    while True:
        print("\nChoose game mode:")
        print("1. Easy (10 lives)")
        print("2. Difficult (5 lives)")
        print("3. Exit")
        
        mode_choice = input("Enter your choice (1-3): ")
        
        if mode_choice == "1":
            lives = 10
            break
        elif mode_choice == "2":
            lives = 5
            break
        elif mode_choice == "3":
            print("Goodbye!")
            return  
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue

    number = random.randint(1, 100)
    while lives > 0:
        try:
            guess = int(input("Input the number you want to guess: "))
            if guess > number:
                lives -= 1
                print(f'You guessed {guess}\nToo high! Take another guess, you have {lives} lives remaining')
            elif guess < number:
                lives -= 1
                print(f'You guessed {guess}\nToo low! Take another guess, you have {lives} lives remaining')
            elif guess == number:
                print(f"You won!")
                break
        except ValueError:
            print("You can only type in numbers")
            continue 
    
    if lives <= 0:
        print(f'You ran out of lives! The answer was {number}')
    
    while True:
        play_again = input('Do you want to play again y/n? ').lower()
        if play_again == "y":
            clear()
            play_game()
            return
        elif play_again == "n":
            print('GGWP!')
            return
        else:
            print(f"Input only y/n, input: '{play_again}' is invalid")

clear()
play_game()