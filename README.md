# Final-Project-Random-Number-Game

--> Not many Git commits because project was added to GitHub Late <--

This game is a random number guesser. You will choose a difficulty while making a player, and a random number will be generated. Your mission is 
to guess the random number -> the game will guide you towards the answer for assistance <-. Can you guess the random number in one try?

--- INSTRUCTIONS FOR RANDOM NUMBER GAME ---

ALL EXAMPLES, are built keeping in mind the examples from before. So if PLAYER is used in one example,
then PLAYER is the same exact thing in another example.

1) Create an instance of NumberGuess(), passing on 2 arguments. --> BOTH STRINGS
   - First argument -> Player Name
   - Second Argument -> Difficulty (Choices: Easy, Medium, Hard, Extreme)  -> Hidden Difficulty If Anything Else is Entered.

     Example:
     player = NumberGuess("corey", "Easy")

2) To begin your first game.

   - Type (instance).play()
  
     Example:
     player.play()

3) You will be prompted to make a guess.

4) To check player stats type print(instance)

   Example:
   print(player)

5) Close the terminal to exit the game, or type -- instance.play() -- again to play another game. (Stats will carry over matches).

HAVE FUN!

If your terminal is stating "Number Guess is not defined" than run the code below in the terminal before playing.

python
from finalproject import NumberGuess

Then your game should work.
   
