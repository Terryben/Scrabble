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

  def can_insert(self, word_pos, p_hand, word, map_word):#word_pos is an array of tuples representing the locations of the letters of 'word'
    #print "word pos is: "
    #print word_pos
    #print "word is: " + word
    try:
      if (word_pos[len(word)-1][0] - word_pos[0][0] < 0) or (word_pos[len(word)-1][1] - word_pos[0][1] < 0):
        print "check 1"
        return False
      if (word_pos[0][0] - word_pos[len(word)-1][0] == 0) and (word_pos[0][1] - word_pos[len(word)-1][1] == 0) and len(word) != 1:
        print "check 2"
        return False
    except StandardError:
      return False
    if (word_pos[0][1] - word_pos[len(word)-1][1] == 0):
      word_is_up_down = True  #word is along the y axis
    else:
      word_is_up_down = False  #word is along the x axis

    room_to_play = len(word) #Make sure that at least one letter will be played from the player's hand
    can_insert = True  #will be set to false if any problems are found
    needed_letters = [] #list of letters the player will need in their hand
    for i in range(0, len(word)):
      needed_letters.append(word[i])

    if (word_pos[0][0] - word_pos[len(word)-1][0] != 0) and (word_pos[0][1] - word_pos[len(word)-1][1] != 0): # word is not a straight line
      can_insert = False
    for i in range(0, len(word)):
      pos = word_pos[i][0]*15+word_pos[i][1]
      if str(self.board[pos]).isalpha():
        room_to_play -= 1
        if(word_is_up_down):
          if not self.check_left_right(pos, map_word, word[i]): #if it doesnt form a valid word
            can_insert = False
            #print "False 1"
        else:
          if not self.check_up_down(pos, map_word, word[i]):  #if it doesnt form a valid word
            can_insert = False
            #print "False 2"
        try:
          #print "Needed letters are"
          #print needed_letters
          #print "word[i] is "
          #print word[i]
          needed_letters.remove(word[i])
        except StandardError:
          print "Shouldn't be here, Uh oh"
      else:
        if(word_is_up_down):
          if not self.check_left_right(pos, map_word, word[i]): #if it doesnt form a valid word
            can_insert = False
            #print "False 3"
        else:
          if not self.check_up_down(pos, map_word, word[i]):  #if it doesnt form a valid word
            #print self.check_up_down(pos, map_word, word[i])
            can_insert = False
            #print "False 4"
    if(word_is_up_down):
      if not self.last_check_up_down(word_pos, word, map_word):
        can_insert = False
    else:
      if not self.last_check_left_right(word_pos, word, map_word):
        can_insert = False
    if room_to_play == 0:
      can_insert = False
    if  can_insert:
      for i in range(0, len(needed_letters)): #Check if the needed letters are in the player's hand
        try:
          #print "P hand in false 5 is: "
          #print p_hand
          #print "the needed letter is: "
          print needed_letters[i]
          p_hand.remove(needed_letters[i])
        except StandardError:
          print needed_letters[i] + " added back"
          can_insert = False
          for j in range(0, i):
            p_hand.append(needed_letters[j])
          #print "False 5"
    return can_insert

  def can_insert2(self, word_pos, p_hand, word, map_word):#word_pos is an array of tuples representing the locations of the letters of 'word'
    #print "word pos is: "
    #print word_pos
    #print "word is: " + word
    try:
      if (word_pos[len(word)-1][0] - word_pos[0][0] < 0) or (word_pos[len(word)-1][1] - word_pos[0][1] < 0):
        #print "check 1"
        return False
      if (word_pos[0][0] - word_pos[len(word)-1][0] == 0) and (word_pos[0][1] - word_pos[len(word)-1][1] == 0) and len(word) != 1:
        #print "check 2"
        return False
    except StandardError:
      return False
    if (word_pos[0][1] - word_pos[len(word)-1][1] == 0):
      word_is_up_down = True  #word is along the y axis
    else:
      word_is_up_down = False  #word is along the x axis

    room_to_play = len(word) #Make sure that at least one letter will be played from the player's hand
    can_insert = True  #will be set to false if any problems are found
    needed_letters = [] #list of letters the player will need in their hand
    for i in range(0, len(word)):
      needed_letters.append(word[i])

    if (word_pos[0][0] - word_pos[len(word)-1][0] != 0) and (word_pos[0][1] - word_pos[len(word)-1][1] != 0): # word is not a straight line
      can_insert = False
    for i in range(0, len(word)):
      pos = word_pos[i][0]*15+word_pos[i][1]
      if str(self.board[pos]).isalpha():
        room_to_play -= 1
        if(word_is_up_down):
          if not self.check_left_right(pos, map_word, word[i]): #if it doesnt form a valid word
            can_insert = False
            #print "False 1"
        else:
          if not self.check_up_down(pos, map_word, word[i]):  #if it doesnt form a valid word
            can_insert = False
            #print "False 2"
        try:
          #print "Needed letters are"
          #print needed_letters
          #print "word[i] is "
          #print word[i]
          needed_letters.remove(word[i])
        except StandardError:
          print "Shouldn't be here, Uh oh"
      else:
        if(word_is_up_down):
          if not self.check_left_right(pos, map_word, word[i]): #if it doesnt form a valid word
            can_insert = False
            #print "False 3"
        else:
          if not self.check_up_down(pos, map_word, word[i]):  #if it doesnt form a valid word
            #print self.check_up_down(pos, map_word, word[i])
            can_insert = False
            #print "False 4"
    if(word_is_up_down):
      if not self.last_check_up_down(word_pos, word, map_word):
        can_insert = False
    else:
      if not self.last_check_left_right(word_pos, word, map_word):
        can_insert = False
    if room_to_play == 0:
      can_insert = False
    if  can_insert:
      put_back = []
    return can_insert



  def last_check_up_down(self, word_pos, word_inc, map_word):
    word = []
    for i in range(0, len(word_inc)):
      word.append(word_inc[i])
    up_spot = word_pos[0][0]*15+word_pos[0][1]
    down_spot = word_pos[len(word)-1][0]*15+word_pos[len(word)-1][1]
    while str(self.board[up_spot-15]).isalpha():#loop through while traveling up
      up_spot -= 15
      word.insert(0, str(self.board[up_spot]))
    while str(self.board[down_spot+15]).isalpha():#loop through while traveling down
      down_spot += 15
      word.append(str(self.board[down_spot]))
    if len(word) > 1:
      return map_word.isValidWord(word)
    else:
      return True

  def last_check_left_right(self, word_pos, word_inc, map_word):
    word = []
    for i in range(0, len(word_inc)):
      word.append(word_inc[i])
    left_spot = word_pos[0][0]*15+word_pos[0][1]
    right_spot = word_pos[len(word)-1][0]*15+word_pos[len(word)-1][1]
    while str(self.board[left_spot-1]).isalpha():#loop through while traveling up
      left_spot -= 1
      word.insert(0, str(self.board[leftp_spot]))
    while str(self.board[right_spot+1]).isalpha():#loop through while traveling down
      right_spot += 1
      word.append(str(self.board[right_spot]))
    if len(word) > 1:
      return map_word.isValidWord(word)
    else:
      return True    

  def check_left_right(self, pos, map_word, letter):#(row, column)
    word = []
    word.append(letter)
    left_spot = pos
    right_spot = pos
    while str(self.board[right_spot+1]).isalpha(): #loop through and find the right most letter in this row that is connected to the original spot
      right_spot += 1
      word.append(str(self.board[right_spot]))
    while str(self.board[left_spot-1]).isalpha(): #find left most letter
      left_spot -= 1
      word.insert(0, str(self.board[left_spot]))
    if len(word) > 1:
      return map_word.isValidWord(word)
    else:
      return True

  def check_up_down(self, pos, map_word, letter):
    word = []
    word.append(letter)
    up_spot = pos
    down_spot = pos
    while str(self.board[up_spot-15]).isalpha():#loop through while traveling up
      up_spot -= 15
      word.insert(0, str(self.board[up_spot]))
    while str(self.board[down_spot+15]).isalpha():#loop through while traveling down
      down_spot += 15
      word.append(str(self.board[down_spot]))
    if len(word) > 1:
      return map_word.isValidWord(word)
    else:
      return True


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
