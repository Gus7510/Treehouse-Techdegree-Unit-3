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
    