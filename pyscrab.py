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
