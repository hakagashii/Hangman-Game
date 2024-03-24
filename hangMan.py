import random

"""1. Welcome the user to the game.
2. Give them the option to stop the program anytime they want to."""
print("Hello user! Welcome to Hangman Game.\nWrite 'exit' to exit whenever you want. ")

HANGMAN_PLAN = ['''
     ------
    |     |
    |
    |
    |
    |
   _|_ ''', '''

     ------
    |     |
    |     O
    |
    |
    |
   _|_ ''','''
   
     ------
    |     |
    |     O
    |     |
    |     |
    |
   _|_  ''','''
  
     ------
    |     |
    |     O
    |    /|\\
    |     |
    |
   _|_    ''','''
   
     ------
    |     |
    |     O
    |    /|\\
    |     |
    |    / \\
   _|_    '''  ]


def start():

    try:
        with open("words.txt") as file:
            words = [line.strip().lower() for line in file]
    except FileNotFoundError:
        print("Error. The file that contains words cannot be found...")
        return

    while True:
        #3. Choose a random word from at least 100 words.
        chosen_word = random.choice(words)

        #4.Tell the user how many letters does the word contain, and show that many underlines
        # as placeholders for each letter.
        print(f"The word contains {len(chosen_word)} letters")
        placeholders = ["_" for _ in chosen_word]
        print(" ".join(placeholders))

        finded_letters = set()
        incorrect_guesses = 0
        #5. Ask from the user to guess a letter.
        while True:
            findLetter = input("Guess a letter: ").lower()

            if findLetter == 'exit':
                break

                #6. If the user input is not a letter, tell them that that is not a valid input, and go back to
                #command number 5.
            if len(findLetter) != 1 or not findLetter.isalpha():
                print("Invalid input.Please enter a single letter(not two or more). ")
                continue
                """7.a. If it was guessed before, tell them that they already guessed that letter, and go
            back to command 5."""
            if findLetter in finded_letters:
                print("You already guessed this letter.")
                continue

            finded_letters.add(findLetter)

            if findLetter in chosen_word:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == findLetter:
                        placeholders[i] = findLetter
                print(" ".join(placeholders))

                if "_" not in placeholders:
                    print("Yeh, Congrats! You guessed the word correctly")
                    break
                    """7.b If it is not in the chosen word, memorize how many times they missed till
                now. If they missed 5 times till now, tell them that they lost and give
                them the option to play again or exit the program."""
            else:
                print(HANGMAN_PLAN[incorrect_guesses])
                incorrect_guesses += 1

                if incorrect_guesses == 5:
                    print("You failed.")
                    break

                """If it is in the chosen word, replace the corresponding word placeholders
(underlines) with the guessed letter. If the word is completed, tell them
that they won and give the option to play again or exit. If the word is not
completed go back to command number 5."""

        replay = input("Press Enter to play again or type 'exit' to exit the program: ")
        if replay == 'exit':
            print("Thanks for playing Hangman!")
            break


start()