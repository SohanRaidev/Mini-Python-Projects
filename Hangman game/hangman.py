import random


words = ["python", "hangman", "chamelion", "crocodile", "dog", "snake", "variable, elephant, tiger, lion,parrot"]

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    
           |
           |
           |
           |
        """
    ]
    return stages[attempts]

def reveal_letters(word):
    revealed = list("_" * len(word))  
    indices_to_reveal = random.sample(range(len(word)), k=max(1, len(word) // 3))  
    for index in indices_to_reveal:
        revealed[index] = word[index]

    return "".join(revealed)


def play_hangman():
    word = random.choice(words)  
    word_completion = reveal_letters(word)  
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6 

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(f"The word is: {word_completion}")

    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():  
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)

                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  
            if guess in guessed_words:
                print("You already guessed that word. Try again.")
            elif guess != word:
                print("Sorry, that is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please guess a letter or word.")

        print(display_hangman(attempts))
        print(f"The word is: {word_completion}")

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")


play_hangman()
