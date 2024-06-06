# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

 
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase



# Step 2
#phrase = Phrase()
#game = Game()

# print(phrase)
# print(game)

# Step 3
#phrase_1 = Phrase("Life is like a box of chocolates")
#print(phrase_1.phrase)






if __name__ == '__main__':
    # Step 4
    game=Game()

    for phrase in game.phrases:
        print(phrase.phrase)