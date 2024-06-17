import random


class hangman:
    def __init__(self) -> None:
        with open("words.txt", "r") as file:
            self.words = file.read().splitlines()

    def game(self):
        word = random.choice(self.words)
        word = word.lower()
        guessed = "_" * len(word)
        guessed = list(guessed)
        lstguessed = []
        
        tries = 6
        while tries > 0:
            print("\nCurrent word: ", " ".join(guessed))
            lstguessed.sort()
            print("Guessed letters: ", " ".join(lstguessed))
            print(f"Incorrect guesses remaining: {tries}")
            letter = input("Guess a letter: ").lower()

            if not letter.isalpha() or len(letter) != 1:
                print("Invalid input. Please enter a single letter.")
            elif letter in lstguessed:
                letter = ""
                print("Already guessed!!")
            elif letter not in word:
                tries -= 1
                print(f"Sorry, '{letter}' is not in the word.")
                lstguessed.append(letter)
            else:
                print(f"Good job! '{letter}' is in the word.")
                lstguessed.append(letter)
                for i in range(len(word)):
                    if letter == word[i]:
                        guessed[i] = letter

            if "_" not in guessed:
                print(f"Congratulations! You guessed the word!: {word}\n")
                break
        else:
            print(f"You ran out of tries. The word was {word}\n")

    def start(self):
        print("Welcome to Hangman!")
        while True:
            self.game()
            if input("Do you want to play again? (yes/no): ").lower() != "yes":
                break


def main():
    game = hangman()
    game.start()

if __name__ == "__main__":
    main()
        