import pyscrab
import random

class scrabble:
    def __init__ (self):
        self.letterpool = ['e']*12 + ['a']*9 + ['i']*9+ ['o']*8+ ['n']*6 + ['r']*6+ ['t']*6 +['l']*4 + ['s'] * 4 + ['u']*4 + ['d']*4+ ['g']*3 + ['b']*2+ ['c']*2+['m']*2 +['p']*2+['f']*2+['h']*2+['v']*2+['w']*2+['y']*2+['k']+['j']+['x']+['q']+['z']
        random.shuffle(self.letterpool)
        
    def draw(self,player):
            handlen=len(player.player_hand)
            for i in xrange(7-handlen):
                player.player_hand.append(self.letterpool.pop(0))
 
    def lettersleft(self):
        return len(self.letterpool)
    
