#Kevin Perez-Morales
#11/14/25
import random

word_bank = [] #Empty list, later used to store words of a selected length.
word_length = 5 #Word length variable, default set as 5.
max_tries = 5 #Difficulty setting based on maximum tries, default set as 5.

#A function to load words only of a specific length from the text file.
def load_words():
    global word_bank #Define the variable throughout the entire program.
    word_bank = [] #Reset the words lists after every run.

    try:
        #Try to open the text file in the assets folder.
        with open("assets/words_alpha.txt", "r") as file:
            #Read each line in the file.
            for line in file:
                w = line.strip()#Remove whitespaces for functionality.

                #If the length of the word matches the chosen length, store it in the word_bank list.
                if len(w) == word_length:
                    word_bank.append(w)

    #If the file doesn't exist, or cannot be found, it will be messaged to the user.
    except FileNotFoundError:
        print("[!] Text file not found.")
        return
    
#A function to choose a random target word from the word_bank list.
def get_random_word():
    #If for some reason the word_bank is empty, that means the text file did not load properly, and it will be messaged to the user.
    if not word_bank:
        print("[!] No words loaded.")
        return None

    #Randomly choose a word from the list.
    return random.choice(word_bank)

#A function to compare guess to target and generate storts/chophy/bascat lists.
def evaluate_guess(guess, target):

    #Set default response to everything as "Bascat".
    result = ["Bascat" for _ in range(len(target))]

    #Compare each letter in guess to each letter in target, running through every guess and target value.
    for i in range(len(guess)):
        for j in range(len(target)):

            #If values match at all:
            if guess[i] == target[j]:

                #Then if value is the correct letter and in the correct place, Chophy will display in that spot.
                if i == j:
                    result[i] = "Chophy"
                    break

                #Then if value exists in the list, but in wrong spot, Storts will display in that spot.
                else:
                    result[i] = "Storts"
                    break

    return result

#A function to use the Storts, Chophy, and Bascat.
def play_game():

    #Get the random word from the text file, using the function.
    secret = get_random_word()

    #If for some reason no random word loaded, stop the game.
    if secret is None:
        return

    print("\n —----- New Game Started —-----")

    #The number of attempts_left is defined by the level, and therefore max_tries.
    attempts_left = max_tries

    #Keep running the function, or game, until user runs out of attempts.
    while attempts_left > 0:

        print(f"\nYou have {attempts_left} tries left.")

        #Ask the user to enter a word guess.
        guess = input(f"Enter a {word_length}letter word: ").lower().strip()

        #Check if guess is the correct length.
        if len(guess) != word_length:
            print(f"[!] Guess must be exactly {word_length} letters.")
            continue

        #Check to see if the guess is an a real dictionary word, according to the text file.
        if guess not in word_bank:
            print("[!] Not a valid English word.")
            continue

        #If the guess is the same as random word, then user wins.
        if guess == secret:
            print("\n You guessed the word!")
            print(f"The correct word was: {secret}")
            return

        #Otherwise get the feedback markings.
        feedback = evaluate_guess(guess, secret)

        #Show Storts, Chophy, and Bascat results.
        print("Response:", feedback)

        attempts_left -= 1 #Subtract one attempt for each guess.

    #If loop ends, it means the player is out of tries.
    print("\n You ran out of tries!")
    print(f"The correct word was: {secret}")

#A function to show how main menu options and let user modify settings.
def menu():
    global word_length, max_tries  #Define the variable throughout the entire program.

    print("\n —------- MAIN MENU —-------")
    print("[0] Exit")
    print("[1] Change Word Length (3–7)")
    print("[2] Change Difficulty")
    print("[3] Play Game")

    #Check to see if the input is actually a number.
    try:
        choice = int(input("Select: "))
    except ValueError:
        print("[!] Invalid number.")
        return

    #Option 0: Exit Game
    if choice == 0:
        print("Goodbye!")
        exit()

    #Option 1: Change Word Length
    elif choice == 1:
        try:
            new_len = int(input("Enter new word length (3–7): "))

            #Set the optional lengths of 3–7.
            if 3 <= new_len <= 7:
                word_length = new_len
                print(f"[***] Word length set to {word_length}.")
                load_words() #Reload words for new length.
            else:
                print("[!] Word length must be between 3 and 7.")

        except ValueError:
            print("[!] Invalid number.")

    #Option 2: Change Difficulty
    elif choice == 2:

        print("\nChoose difficulty:")
        print("[1] Easy   (8 tries)")
        print("[2] Normal (5 tries)")
        print("[3] Hard   (3 tries)")

        try:
            diff = int(input("Select difficulty: "))

            if diff == 1:
                max_tries = 8
            elif diff == 2:
                max_tries = 5
            elif diff == 3:
                max_tries = 3
            else:
                print("[!] Invalid difficulty.")
                return

            print(f"[***] Difficulty changed. You now have {max_tries} tries.")

        except ValueError:
            print("[!] Invalid input.")

    #Option 3: Play Game
    elif choice == 3:
        play_game()

    else:
        print("[!] Not an option.")

#A function to keep running and showing the menu, until the user quits.
def main():
    load_words()
    while True:
        menu()

if __name__ == "__main__":
    main()