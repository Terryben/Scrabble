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
      print "That word cannot be played in that position" 



  if __name__ == "__main__":
    board = pyscrab()
    diction=map_words.map_words()
    players =scrabble.scrabble()
    player_hand = ['p', 'h', 'o', 'n', 'e']
    num_args = len(sys.argv)

    while num_args > 1:
      word = sys.argv[num_args-1]
      print word + " is a valid word? " + str(diction.isValidWord(word))
      print "The word score is: " + str(diction.wordScore(word, diction.alphScore, (1,0), (1, len(word))))
      num_args = num_args - 1
    board.insertword((0,0), (0, 3), 'add')
    board.insertword((0,2), (3, 2), 'damn')
    play_word(board, player_hand, (7, 0), (7, 5), "phone", diction)
    board.printboard() 
