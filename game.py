#! /usr/bin/python
import sys
from pyscrab import *
import map_words
import scrabble

class game:

  def play_word(board, p_hand, tup1, tup2, word, diction):
    word_pos = diction.findWordPos(tup1, tup2) 
    if board.can_insert(word_pos, p_hand, word, diction): 
      board.insertword(tup1, tup2, word) 
    else: 
      print word + " cannot be played in that position" 



  if __name__ == "__main__":
    board = pyscrab()
    diction=map_words.map_words()
    players =scrabble.scrabble()
    player_hand = ['p', 'h', 'o', 'n', 'e', 'n', 'o']
    player_hand2 = ['n', 'o']
    num_args = len(sys.argv)

    while num_args > 1:
      word = sys.argv[num_args-1]
      print word + " is a valid word? " + str(diction.isValidWord(word))
      num_args = num_args - 1
    #board.insertword((0,0), (0, 3), 'add')
    #board.insertword((0,2), (3, 2), 'damn')
    play_word(board, player_hand, (7, 0), (7, 5), "phone", diction)
    print "p_hand is: "
    print player_hand
    #play_word(board, player_hand, (7, 0), (7, 5), "phone", diction)
    #print "P_hand after second insert is: "
    #print player_hand
    play_word(board, player_hand2, (3, 2), (3, 3), "no", diction)
    print "their hand is: "
    print player_hand2
    player_hand2 = ['p', 'h', 'o', 'n', 'e', 'n', 'o']
    #play_word(board, player_hand, (8, 0), (8, 5), "phone", diction)
    play_word(board, player_hand2, (4, 3), (8, 3), "phone", diction)
    print "The score is: "
    print diction.wordScore("phone", board, (7,0), (7, 5)) 
    print "their hand is: "
    print player_hand2
    
    
    board.printboard() 
