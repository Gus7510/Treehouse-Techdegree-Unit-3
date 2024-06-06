# Create your Game class logic in here.
from phrase import Phrase


class Game():
    
    def __init__(self):
        
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
        self.guesses = [" "]
        
    def create_phrases():
        phrase = ["Hello World", 
                   "An apple a day keeps the Doctor away", 
                   "Like father like son",
                   "No pain no gain",
                   "Third time lucky"]
        return phrase
        
    
        
        
    
    
    