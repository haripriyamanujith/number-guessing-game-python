import random
import sys

guesses = 0



def main():
    global guesses
    print("****************************\n******Guess The Number******\n****************************\n")
    print("1.Easy (1-20)\n2.Medium (1-50)\n3.Hard (1-100)")
    difficulty = int(input("Choose Your Difficulty: "))
    random_number = random_number_generator(difficulty)

    while True:
        try:
            
            if number_status(random_number) == 0:
                want_to_play = play_again()
                if want_to_play == 'y':
                    random_number = random_number_generator(difficulty)
                    guesses = 0
                    continue
                elif want_to_play == 'n':
                    sys.exit("\n****************************************\nThank You For Playing 'Guess The Number'\n****************************************\n")
                else:
                    sys.exit("!!! Wrong Input !!!\nThanK You For Playing")
                    
        except ValueError:
            continue

   

def random_number_generator(difficulty):
    if difficulty == 1:
        random_number = random.randint(1,20)
    elif difficulty == 2:
        random_number = random.randint(1,50)
    elif difficulty == 3:
        random_number = random.randint(1,100)
    return random_number 



def number_status(random_number):
    global guesses
    user_guess = int(input("Enter your guess: "))
    guesses += 1  
    if random_number > user_guess:
        print("-- Too Low --")
    elif random_number < user_guess:
        print("!! Too High !!")    
    else:
        print("+-------------+\n!---You Won---!\n+-------------+")
        print(f"Total Number Of Guesses: {guesses}")
        return 0
    


def play_again():
    user = input("\nDo You Want To Play Again? y/n: ")
    return user.lower()




if __name__ == "__main__":
    main()

