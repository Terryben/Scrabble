#! /usr/bin/python
import sys
from pyscrab import *
import map_words
import scrabble
import player

class game:
  
  def play_word(self, board, p_hand, tup1, tup2, word, diction):
    word_pos = diction.findWordPos(tup1, tup2) 
    if board.can_insert(word_pos, p_hand, word, diction): 
      board.insertword(tup1, tup2, word) 
      return True
    else: 
      print word + " cannot be played" 
      return False

  def human_turn(self, player, scrabble, board, diction):
    scrabble.draw(player)
    turn_over = False
    while not turn_over:
      print "1: Play a word."
      print "2: Pass your turn."
      usr_input = raw_input("Enter the number of the action you would like to perform:")
      if usr_input == "1":
        print "Player " + player.name + "'s turn. Here is your hand."
        print player.player_hand
        can_play_word = True
        try:
          word = raw_input("Please enter the word you would like to place: ").split(' ', 1)[0]
          pos1 = raw_input("Please enter the starting point of your word as \"(X,X)\": ")
          pos2 = raw_input("Please enter the ending point of your word as \"(X,X)\": ")
          #print word
          #print pos1
          #print pos2
          tup1 = (int(pos1[1]), int(pos1[3]))
         # print pos1[1] + " " + pos1[3]
          tup2 = (int(pos2[1]), int(pos2[3]))
        except StandardError:
          print "Incorrect formatting."
          can_play_word = False
        if can_play_word:
          if self.play_word(board, player.player_hand, tup1, tup2, word, diction):
            score= diction.wordScore(word, board, tup1, tup2)
            player.score += score
            print word + " was worth " + str(score) + " points! Your score is now " + str(player.score)
            turn_over = True
      elif usr_input == "2":
        turn_over = True
    return
      

if __name__ == "__main__":
  board = pyscrab()
  diction = map_words.map_words()
  scrabble = scrabble.scrabble()
  g = game()
  name = raw_input("Please enter your name: ")
  human = player.player(name)
  comp = player.player("computer")
  board.printboard()
  
  print "" 
  while True: 
    g.human_turn(human, scrabble, board, diction)
    board.printboard()
    print "" 
    
    
