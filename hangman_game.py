import random
words=["computer","money","peacock","python","science","softie","machine"]
word=random.choice(words)
guessed=["_"]*len(word)
wrong=0
max_wrong=6
used = []
print("HANGMAN GAME")
while wrong < max_wrong and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Wrong guesses:", wrong, "/", max_wrong)
    print("Used letters:", " ".join(used))
    ch = input("Guess a letter: ").lower()
    if len(ch) != 1 or not ch.isalpha():
        print("Enter one letter only!")
        continue
    if ch in used:
        print("You already guessed that!")
        continue
    used.append(ch)
    if ch in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == ch:
                guessed[i] = ch
    else:
        print("Wrong!")
        wrong += 1
if "_" not in guessed:
    print("\nHurrayyyyyy...You won!")
    print("The word was:",word)
else:
    print("\nYou lost!")
    print("The word was:",word)