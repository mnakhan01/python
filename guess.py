secret_word = "Himalayas"
guess = ""
guess_count = 0
guess_limit = 3
out_of_options = False
while guess != secret_word and not(out_of_options):
	if guess_count < guess_limit:
		guess = input("enter your guess: ")
		guess_count += 1
	else:
		out_of_options = True
if out_of_options:
	print("You Lose")
else:
	print("You Win!")
