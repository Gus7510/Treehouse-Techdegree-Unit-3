# Create your Phrase class logic here.

class Phrase():
    
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
        
    def display(self, guesses):     # Step 7 
        
        phrase_reveal = ""
        for letter in self.phrase:
            if letter in guesses:
                phrase_reveal += letter
                
            
            else:
                phrase_reveal += "_ "
                
             
        print(f"{phrase_reveal}", end=" ")
        
    def check_guess(self,guess):    #Step 11
        
        if guess in self.phrase:
            return True
        else:
            return False
        
        
    def check_complete(self, guesses): # Step 13
    
        for letter in self.phrase:
            if letter not in guesses:
                return False
            
        return True
        
        