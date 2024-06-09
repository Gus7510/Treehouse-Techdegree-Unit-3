# Create your Phrase class logic here.

class Phrase():
    
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):     # Step 7 
        self.guesses = [" "]
        
        phrase_reveal = ""
        for letter in self.phrase:
            if letter in self.guesses:
                phrase_reveal += letter
                #print(f"{letter}", end=" ")
            else:
                phrase_reveal += "_ "
                #print("_ ")
             
        print(f"{phrase_reveal}", end=" ")
        
        
        
        
        
        """
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            #elif letter == " ":
            #    print(f"{letter}", end=" ")
            else:
                print("_ ")
        
        ###
        This code generates the following:
        no pain no gain
        _ 
        _ 
          _ 
        _ 
        _ 
        _ 
          _ 
        _ 
          _ 
        _ 
        _ 
        _ 
        
        
        """
        
        