import random
print("Welcome to the Simple Coin Toss Game!")
while True:
    guess = input("Guess 'heads' or 'tails': ").lower()
    while guess not in ("heads", "tails"):
        print("Invalid input. Please enter 'heads' or 'tails'.")
        guess = input("Guess 'heads' or 'tails': ").lower()
    coin = random.choice(["heads", "tails"])
    print(f"Coin shows: {coin}")
    if guess == coin:
        print("You guessed it right!")
    else:
        print("Wrong guess!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
