# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

 
from phrasehunter.game import Game
#from phrasehunter.phrase import Phrase     #this line is not necessary anymore



# Step 2
#phrase = Phrase()
#game = Game()

# print(phrase)
# print(game)

# Step 3
#phrase_1 = Phrase("Life is like a box of chocolates")
#print(phrase_1.phrase)



if __name__ == '__main__':
    
    game=Game()
    
    # Step 4 - here i tested if the phrases would print out 
    #for phrase in game.phrases:
    #    print(phrase.phrase)
    
    # Step 5 - printing random phrases
    #def print_phrase(phrase_object):
    #    print(f"The phrase is: {phrase_object.phrase}")
    
    #print_phrase(game.get_random_phrase())
    
    # Step 6 - we check if we print a random phrase every time
    #print(game.active_phrase)   # this prints a Phrase object
    #print(game.active_phrase.phrase)    # this prints a phrase
    
    # Step 7 - we test if the following code prints the active phrase and a series of underscores "_"
    print(game.active_phrase.phrase)    # print active phrase
    game.active_phrase.display(game.guesses)    # should print a series of "_"
    
    
    
    
    
    