# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random

class Game():
    
    def __init__(self):
        
        self.missed = 0
        self.phrases = [Phrase("Hello World"),
                        Phrase("An apple a day keeps the Doctor away"),
                        Phrase("Like father like son"),
                        Phrase("No pain no gain"),
                        Phrase("Third time lucky")
                             ]
        self.active_phrase = self.get_random_phrase()        # Step 6 - change the active_phrase to call the get_random_phrase
        self.guesses = [" "]
        
    def get_random_phrase(self): # Step 5 - i generate a function to randomly call a phrase
        random_phrase = random.choice(self.phrases)
        return random_phrase
    
    def welcome(self):
        print("""
              ------------------------------------
              Welcome Player, to Phrase Hunter !!!
              ------------------------------------""")
              
    def get_guess(self): # Step 10
        guess = input("\n Insert a letter ")
        return guess
              
    def start(self):    # Step 9
        self.welcome()
        # Step 12 - we end the game if the player has 5 incorrect guesses
        # Step 13 - and check_complete() returns False
        
        while self.missed < 5 and self.check_complete() is False:
            """
            AttributeError: 'Game' object has no attribute 'check_complete'
            """
            print(f"Number missed: {self.missed}")
                  
                                                
            self.active_phrase.display(self.guesses) # with print() There is a None appearing at the end of the "_" series
                                                    # print the series of "_" that represent the hidde phrase
        # Part 2
        # Step 10
            user_guess = self.get_guess()
        # the line below is for testing purposes
        #print(user_guess)
            self.guesses.append(user_guess)
        
        #self.active_phrase.display(self.guesses)       # Second call of display()
        
        # Step 11
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1 # we add 1 to the missed count
            #print("Yay !")
            else:
            #print("Bummer !")
                pass
            
            
            
            