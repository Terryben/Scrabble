#! /usr/bin/python
import sys
from pyscrab import *
import map_words
import scrabble
import player
from WordSearch import *

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
          pos1 = raw_input("Please enter the starting point of your word as \"X,X\": ").split(",", 1)
          pos2 = raw_input("Please enter the ending point of your word as \"X,X\": ").split(",", 1)
          #print word
          #print pos1
          #print pos2
          #print pos1[0]
          #print pos1[1]
          #print pos2[0]
          #print pos2[1]
          tup1 = (int(pos1[0]), int(pos1[1]))
         # print pos1[1] + " " + pos1[3]
          tup2 = (int(pos2[0]), int(pos2[1]))
          #print tup1
          #print tup2
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
      
  def comp_turn(self, scrabble, player, diction, board):
    scrabble.draw(player)
    big=0
    max_score=0
    for j in xrange(10):
      random.shuffle(player.player_hand)
      word_s = WordSearch(board, player.player_hand)
      ws=search.hill_climbing(word_s)
      print ws
      if diction.wordScore(ws[0],board,ws[1],ws[2]) >= max_score:
        max_score = diction.wordScore(ws[0],board,ws[1],ws[2])
        big = ws
      #def play_word(self, board, p_hand, tup1, tup2, word, diction):
    print 'HERE'
    print big
    
    self.play_word(board,list(player.player_hand),big[1],big[2],big[0],diction)
    #board.insertword( big[1], big[2], big[0])
    score= diction.wordScore(big[0], board, big[1], big[2])
    player.score += score
    print big[0] + " was worth " + str(score) + " points! Your score is now " + str(player.score)

    
if __name__ == "__main__":
  board = pyscrab()
  diction = map_words()
  scrabble = scrabble()
  g = game()
  name = raw_input("Please enter your name: ")
  human = player.player(name)
  comp = player.player("Computer")
  board.printboard()
  print "" 
  while True: 
    if (len(scrabble.letterpool) < 7):
      print human.name + " had a score of " + str(human.score) + "!"
      print comp.name + " had a score of " + str(comp.score) + "!"
      if(human.score > comp.score):
        print human.name + " wins!"
        sys.exit(0)
      elif(human.score < comp.score):
        print comp.name + " wins!"
        sys.exit(0)
      else: 
        print "It's a tie!"
        sys.exit(0)
    g.human_turn(human, scrabble, board, diction)
    board.printboard()
    print ""
    if (len(scrabble.letterpool) < 7):
      print human.name + " had a score of " + str(human.score) + "!"
      print comp.name + " had a score of " + str(comp.score) + "!"
      if(human.score > comp.score):
        print human.name + " wins!"
        sys.exit(0)
      elif(human.score < comp.score):
        print comp.name + " wins!"
        sys.exit(0)
      else: 
        print "It's a tie!"
        sys.exit(0) 
    g.comp_turn(scrabble, comp, diction, board)
    board.printboard()
    print ""
