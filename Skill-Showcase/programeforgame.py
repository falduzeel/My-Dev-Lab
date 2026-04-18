# My first GitHub profile project - Simple Number Guessing Game
# Hand-coded by me, not AI! Let's make it fun :)

import random

def play_game():
    print("🎮 Welcome to Number Guessing Game! 🎮")
    print("I'm thinking of a number between 1-100")
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter guess: "))
            attempts += 1
            
            if guess == secret:
                print(f"🎉 WINNER! You got it in {attempts} attempts!")
                return
            elif guess < secret:
                print("📈 Too low! Try higher")
            else:
                print("📉 Too high! Try lower")
                
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
    
    print(f"💀 Game Over! Secret was {secret}")

def main():
    print("=== MY FIRST GITHUB PROJECT ===")
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! ⭐ Star my repo!")
            break

if __name__ == "__main__":
    main()