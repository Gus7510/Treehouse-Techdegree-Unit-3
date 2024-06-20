# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random
from sys import exit

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
    
    
    def valid_guess(self, guess):
        if len(guess) > 1:
            print("Please enter only a single letter character (a-z) ")
            return False
        
        elif not guess.isalpha():
            print("Please enter only a single letter character (a-z) ")
            return False
            
        elif guess in self.guesses:
            print("Please try with another letter (a-z) ")
            return False
        
        else:
            return True
            
            
            
    def game_over(self):
        
        # Step 14
        if self.missed == 5:
            print(" Sorry, you lost the game ")
        else:
            print(" Congratulations, you won the game !!!")            
            
            
        
            
    def start(self):    # Step 9
        self.welcome()
        # Step 12 - we end the game if the player has 5 incorrect guesses
        # Step 13 - and check_complete() returns False
        while True:
            
            while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            
            
                print(f"Number missed: {self.missed}") # We print the number of missed tries
                  
                                                
                self.active_phrase.display(self.guesses) 
                # with print() There is a None appearing at the end of the "_" series
                                                    # print the series of "_" that represent the hidde phrase
        # Part 2
        # Step 10
        
                
                user_guess = self.get_guess() # we get the user's guess
        # the line below is for testing purposes
        #print(user_guess)
        
        
                if self.valid_guess(user_guess) == True:
                    
                    self.guesses.append(user_guess)
        
        #self.active_phrase.display(self.guesses)       # Second call of display()
        
        # Step 11
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1 # we add 1 to the missed count
            #print("Yay !")
                else:
            #print("Bummer !")
                    pass
            
            self.game_over()    
            
            play_again_choice = input("Would you like to play again? (y/n) ")
            if "y".lower() in play_again_choice:
                
                self.__init__()
                self.start()
            
            else:
                exit(0)
        
        
        


