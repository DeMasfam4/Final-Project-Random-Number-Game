# Corey DeMas
# Date: 4-27-2026
# Final Project : Number Guessing Game


import random

class NumberGuess:
    # This class allows you to the play Random Number Guessing Game.

    def __init__(self, name: str, difficulty: str):
        self.player = name
        self.diff = difficulty
        self.attempts = 0
        self.lastscore = None
        self.record = None
        self.gamesplayed = 0

    def __str__(self):
        # This returns the Player's Name and Stats.
        return f"Player: {self.player} | Difficulty: {self.diff} | Games Played: {self.gamesplayed} | Record: {self.record} | Last Game: {self.lastscore}"
    
    def rand_num(self):
        # This function changes the "boundaries" for the random number depending on the difficulty chosen.
        if self.diff == "Easy":
            random_int = random.randint(1, 10)
        elif self.diff == "Medium":
            random_int = random.randint(1, 50)
        elif self.diff == "Hard":
            random_int = random.randint(1, 100)
        elif self.diff == "Extreme":
            random_int = random.randint(1, 1000)
        else:
            print("ERROR: Difficulty Does Not Exist. You Have Been Reassigned to ULTRA EXTREME Mode.")
            random_int = random.randint(1, 10000)
            self.diff = "ULTRA EXTREME"
        return random_int

    def set_boundary(self):
        # This function changes the upper bound depending on the difficulty, for the (num_range_high) variable in the play() function.
        if self.diff == "Easy":
            return 10
        elif self.diff == "Medium":
            return 50
        elif self.diff == "Hard":
            return 100
        elif self.diff == "Extreme":
            return 1000
        else:
            return 10000

    def play(self):
        # This is the main function that takes a guess from the player and checks if the guess is valid.

        random_int = self.rand_num()
        num_range_high = self.set_boundary()

        guess = None
        print(f"\nYou Have Chosen Difficulty {self.diff}. Choose a Number Between 1-{num_range_high}.")

        while guess != random_int:

            try:
                guess = int((input("\nMake Your Guess: ")))

                while (guess > num_range_high) or (guess < 1):
                    if guess > num_range_high:
                        guess = int(input("That Number is Higher Than the Boundary! Guess Again: "))
                    elif guess < 1:
                        guess = int(input("That Number is Below the Boundary! Guess Again: "))

                if guess > random_int:
                    print("Too High! Guess a Lower Number.")
                    self.attempts += 1
                    print(f"Attempts {self.attempts}")
                elif guess < random_int:
                    print("Too Low! Guess a Higher Number.")
                    self.attempts += 1
                    print(f"Attempts {self.attempts}")

            except ValueError:
                print("That is Not a Integer! Try Again.")

        self.attempts += 1

        self.lastscore = self.attempts
        self.attempts = 0
        self.gamesplayed += 1
        
        if self.check_record(): # If true, update the record and give a different winning message.
            self.record = self.lastscore
            return f"You Got a New Record of {self.record} Guesses! Type {self.player}.play() to Play Again!"

        return f"You Won in {self.lastscore} Guesses! Type {self.player}.play() to Play Again!"

    def check_record(self):
        # This function checks if the new score is less than the player's record, so the record can be updated.
        if isinstance(self.lastscore, int) and isinstance(self.record, int):
            return self.lastscore < self.record
        if self.record is None:
            return True

if __name__ == "__main__":
    print("Game Started. Create Your Player. WARNING: Your Difficulty Is Now Allowed to Be Changed. Choose Wisely.")