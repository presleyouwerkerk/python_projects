secret_word = input("Player 1, type a word: ")
playing = True
correct_guesses = []
wrong_guesses = []
mistakes = 0
maximum_mistakes = 9
display = ["_"] * len(secret_word) 

while playing:
    if all(letter in correct_guesses for letter in secret_word):
        print("You won! The word was:", secret_word)
        break

    if mistakes == maximum_mistakes:
        print("You lost! The word was:", secret_word)
        break

    guess = input("Player 2, guess a letter: ")

    if guess in correct_guesses or guess in wrong_guesses:
        print("You have already guessed this letter!")
        continue
    
    if guess in secret_word:
        correct_guesses.append(guess)

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

        print("Correct guess!")
        print("Secret word: ", display)
        continue
    else:
        wrong_guesses.append(guess)
        mistakes += 1
        print("Wrong guess!")
        print("You have made", mistakes, "mistakes, you can make", maximum_mistakes, "mistakes in total")
        print("Secret word: ", display)
        continue