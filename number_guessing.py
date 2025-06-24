import random
import os
import art

def clear():
    os.system('cls')


def play_game():
    print(art.logo)
    print('the clue is a number between 1 to 100')
    pick_lives = input('Do you want to try the easy or difficult mode ?').lower()
    lives = 10
    if pick_lives == "difficult":
        lives -= 5
    number = random.randint(1, 100)
    while lives > 0:
        try :
            guess = int(input("Input the number you want to guess : "))
            if guess > number:
                lives -= 1
                print(f'you guessed {guess}\ntoo high! take another guess, you have {lives} lives remaining')
            elif guess < number:
                lives -= 1
                print(f'you guessed {guess}\ntoo low! take another guess, you have {lives} lives remaining')
            elif guess == number:
                print(f"you won!")
                break
        except ValueError:
            print(f"You can only type in number")
            continue 
    if lives <= 0:
        print(f'You run out of lives! the answer was {number}')
    while True:
        play_again = input('Do you want to play again y/n ? ').lower()
        if play_again == "y":
            clear()
            play_game()
            break
        elif play_again == "n" :
            print('GGWP!')
            break
        else :
            print(f"Input only y/n, input :{play_again} is invalid")
    

clear()
play_game()