import random


answer = random.choice(
    open(r"C:\Users\walsh\Documents\WordsForGames.txt", "r").readline().split())

answer_list = list(answer)
hidden_length = len(answer)
hidden_answer = hidden_length * "*"
hidden_list = list(hidden_answer)
incorrect_letters = ""
guess_count = 0
total_guesses = 5


print(f"Your word is: {hidden_answer}")
print(f"You have {total_guesses} guesses")

while guess_count < total_guesses:
    if hidden_list == answer_list:
        print(f"You won! The word was {answer}")
        break
    elif total_guesses - guess_count == 1:
        print("You have 1 guess left!")

    guess = input(f"""
Guess a letter: """).lower()

    if len(guess) > 1:
        print("Please only guess one letter, dolt!")
    elif guess in hidden_list or guess in incorrect_letters:
        print("You have already guessed that letter dumbo!")
    elif guess in answer_list:
        for guess_location, char in enumerate(answer):
            if char == guess:
                hidden_list[guess_location] = guess
    elif guess not in answer_list:
        guess_count += 1
        incorrect_letters += guess
        print(f"""
Nope! You have {total_guesses - guess_count} guess left
        """)
    print("".join(hidden_list))
    print(f"""
Already guessed: {incorrect_letters}

--------------""")
    if guess_count == total_guesses:
        print(f"You lose! The word was {answer}")
print("Game over!")
