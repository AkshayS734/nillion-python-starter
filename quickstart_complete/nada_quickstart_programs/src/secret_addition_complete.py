import random
from nada_dsl import *

def nada_main():
    party1 = Party(name="Player")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    max_tries = 5
    attempts = 0
    guessed_correctly = False

    while attempts < max_tries:
        # Receive guess from player
        guess = SecretInteger(Input(name=f"guess_{attempts+1}", party=party1))
        
        # Check if guess is correct
        correct_guess = (guess == secret_number)
        higher_hint = (guess < secret_number)
        lower_hint = (guess > secret_number)
        
        if correct_guess:
            guessed_correctly = True
            break
        
        attempts += 1
        
        if higher_hint:
            Output("Higher!", f"hint_{attempts}", party=party1)
        elif lower_hint:
            Output("Lower!", f"hint_{attempts}", party=party1)
    
    if not guessed_correctly:
        Output(secret_number, "reveal_number", party=party1)
    
    play_again = Input(name="play_again", party=party1)
    
    return [Output(guessed_correctly, "guessed_correctly", party=party1), Output(attempts, "attempts", party=party1), Output(play_again, "play_again", party=party1)]

if __name__ == "__main__":
    nada_main()
