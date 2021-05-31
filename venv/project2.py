# secret_word = "Giraffe"
# guess = ""
# while guess != secret_word:
#     guess = input("Enter a guess: ")
#
#     print("You win")

right_word = "Beth"  # first variable
guess = ""           # guess variable
guess_count = 0      # counts how many times the guesses have guessed
guess_limit = 3      # prompts how many times a user can guess
out_of_guesses = False

while guess != right_word and not(out_of_guesses):  # keeps looping if the condition is true an not out of limit
    if guess_count < guess_limit:
       guess = input ("Enter a guess: ")
       guess_count += 1
    else:
         out_of_guesses = True

if out_of_guesses:
    print("You loose!")
else:
     print("You win")