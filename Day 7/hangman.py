from random_word import RandomWords
import hangman_art


r = RandomWords()

print(hangman_art.logo)
playing = True
while playing:
    choice = r.get_random_word()
    display = ["_"] * len(choice)

    hits = 0
    lives = 6
    guesses = []
    print(" ".join(display))

    game_running = True
    while game_running:
        guess = input("Guess a letter!\n").lower()

        if guess not in guesses:
            guesses += guess
        else:
            print("You have already guessed that letter.")
            continue
        contained = False
        for i in range(len(choice)):
            if choice[i] == guess:
                contained = True
                # check if letter was already guessed
                if display[i] != guess:
                    display[i] = guess
                    hits += 1
                # if letter was already guessed there is no need to iterate over the rest of the word
                else:
                    break

        if not contained:
            print("Wrong, the word does not contain this letter.")
            lives -= 1
        else:
            print("Good job! The word contains your letter.")

        print(" ".join(display))
        print(hangman_art.stages[lives])
        print(f"You have {lives} lives left.")

        if hits >= len(choice):
            print(f"Congratulations. You have won! The word was '{choice}'.")
            game_running = False
        elif lives <= 0:
            print(f"Game over. You have lost! The word was '{choice}'.")
            game_running = False

    new_game = input("Do you want to play another round? Type 1 for Yes, 0 for No.\n")
    if new_game != "1":
        playing = False
