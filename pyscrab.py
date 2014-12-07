import sys
from termcolor import *
class pyscrab():
  def __init__ (self):
    self.board = [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
    4, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 4,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
    4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4]
    
    self.empty = [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
    4, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 4,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
    4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4]
  def printboard(self):
    i=0
    listred= []
    listmagenta =[]
    listblue =[]
    listcyan =[]
    for k in self.board:
      if (i)%15 == 0:
          print'\n\n',
      if k == 4:
          cprint(' TW', 'red', attrs=[], end = ' ')
          listred.append(i)
      elif k == -1:
         cprint('  *', 'magenta', attrs=['bold'], end = ' ')
      #print 'TW',
      elif k == 3:
          cprint(' DW', 'magenta', attrs=[], end = ' ')
          listmagenta.append(i)
      #print 'DW',
      elif k == 2:
          cprint(' TL', 'blue', attrs=[], end = ' ')
          listblue.append(i)
      #print 'TL',
      elif k == 1:
          cprint(' DL', 'cyan', attrs=[], end = ' ')
          listcyan.append(i)
      #print 'DL',
      elif k == 0:
          print '___',
      else:
        if i in [0, 7, 14, 105, 119, 210, 217, 224]:
          cprint(' '+k,'red', attrs=['bold'], end = '  ')
        elif i in [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]:
          cprint(' '+k,'magenta', attrs=['bold'], end = '  ')
        elif i in [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]:
          cprint(' '+k,'blue', attrs=['bold'], end = '  ')
        elif i in [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]:
          cprint(' '+k,'cyan', attrs=['bold'], end = '  ')
        else:
          cprint(' '+k,'yellow', attrs=['bold'], end = '  ')
      i=i+1
  def insertword(self,tup1,tup2,word):
    t11=tup1[0]
    t12=tup1[1]
    t21=tup2[0]
    t22=tup2[1]
    pos1=t11*15+t12
    pos2=t21*15+t22
    if t11 ==t21:
      for i in range(len(word)):
        self.board[pos1+i]=word[i]
    else:
     for i in range(len(word)):
        self.board[pos1+(15*i)]=word[i]

  def can_insert(self, word_pos, p_hand, word):#word_pos is an array of tuples representing the locations of the letters of 'word'
    if (word_pos[0][0] - word_pos[len(word)-1][0] == 0):
      word_is_up_down = True  #word is along the y axis
    else:
      word_is_up_down = False  #word is along the x axis

    can_insert = True
    up_spot = 0
    down_spot = 0
    left_spot = 0
    right_spot = 0
    needed_letters = word
    for i in range(0, len(word)):
      pos = word_pos[i][0]*15+word_pos[i][1]
      if str(self.board[pos]).isalpha()
        try:
          needed_letters.remove(str(self.board[pos]).isalpha())
        except Error:
          print "Shouldn't be here, Uh oh"
      while str(self.board[(word_pos[i][0]-1)*15+word[i][1]]).isalpha():      
        up_spot = word_pos[i][0]-1)*15+word[i][1]
      while str(self.board[(word_pos[i][0]+1)*15+word[i][1]]).isalpha():
        down_spot = word_pos[i][0]+1)*15+word[i][1]
      while



    for i in range(0, len(needed_letters)): #Check if the needed letters are in the player's hand
      try:
        p_hand.remove(needed_letters[i])
      except Error:
        can_insert = False
     

  def multiplierer(self,tup):
    t11=tup[0]
    t12=tup[1]
    pos=t11*15+t12
    if self.empty[pos] is 4:
      return 'TW'
    elif self.empty[pos] is 3 or -1:
      return 'DW'
    elif self.empty[pos] is 2:
      return 'TL'
    elif self.empty[pos] is 1:
      return 'DL'
    else:
      return 
