4
import random

words = ["python", "apple", "tiger", "school", "computer"]
word = random.choice(words)

guessed = []
wrong = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")

while wrong < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if Len(guess) != 1 or not guess is alpha():
        print("❌ Enter only one alphabet.")
        continue

    if guess in guessed:
        print("⚠️ You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("❌ Wrong guess!")
        print("❤️ Chances left:", max_wrong - wrong)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)