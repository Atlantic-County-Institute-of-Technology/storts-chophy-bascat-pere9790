import random
WORD_LIST = []
WORD_LEN = 5
tries = 5

def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as dictionary:
            for word in dictionary.readlines():
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File Not Found")
    print(WORD_LEN)
    print(WORD_LIST)


def strawberry():
    target = random.choice(WORD_LIST)
    print(f"{target}")

def atoms():
    print("[-] 0. Exit\n"
          "[-] 1. Change Word Length\n"
          "[-] 2. Change Difficulty\n"
          "[-] 3. Play Game")
    selection = int(input("[-] Please Select an Option: "))

    if selection == 0:
        print("Quiting Game")
        exit()
    elif selection == 1:
        print(f"Input A Number 3-7")
    elif selection == 2:
        print()
    elif selection == 3:
        strawberry()

def main():
    atoms()
    strawberry()
    extract_words()


if __name__ == "__main__":
    main()