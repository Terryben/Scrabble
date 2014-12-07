import search
import utils
from pyscrab import pyscrab
from scrabble import scrabble
import map_words

class colec:
  def __init__ (self,word,tup11,tup12,tup21):
    self.word=word
    self.start=tup11
    self.end=tup12
    self.last=tup21
  def gettup1(self):
    return (self.start,self.end)
  def gettup2(self):
    return (self.last)
  def __str__(self):
    return self.word+' '+ str(self.start)+ ' ' +str(self.end)+ ' '+ str(self.last)
  
def getpos(board,tup1):
  t11=tup1[0]
  t12=tup1[1]
  return board[t11*15+t12]


class WordSearch:
  def __init__ (self,boardstate,playerhand):
    self.board=boardstate
    self.hand=playerhand
    self.initial=colec('',(0,0),(0,0),(0,0))
  def actions(self, state):
    actions=[]
    if state.gettup1() == ((0,0),(0,0)) and state.gettup2() == ((0,0)) and state.word is '':
      pos=[]
      for i in range(len((self.board))):
        if str(self.board[i]).isalpha():
          pos.append([i/15,i%15])
          break;
      #print getpos(self.board,tuple(pos[0]))
      temp=pos[0]
      #while str(getpos(self.board,(temp[0],temp[1]+1))).isalpha():
      #  temp=list((temp[0],temp[1]+1))
       # print getpos(self.board,tuple(temp))
      if pos[0][0] is not 0:
        for i in b.player2hand:
          actions.append([i,(pos[0][0]-1,pos[0][1]),'u'])
      if pos[0][1] is not 0:
        for i in b.player2hand:
          actions.append([i,(pos[0][0],pos[0][1]-1),'l'])      
      if str(getpos(self.board,(pos[0][0]+1,pos[0][1]))).isalpha() is False:
        for i in b.player2hand:
          actions.append([i,(pos[0][0]+1,pos[0][1]),'d']) 
      if str(getpos(self.board,(pos[0][0],pos[0][1]+1))).isalpha() is False:
        for i in b.player2hand:
          actions.append([i,(pos[0][0],pos[0][1]+1),'r'])                       
      print b.player2hand
      print actions
      
    return actions
  def result(self,state,action):
    tempstring=""
    temp=list(action[1])
    
    
    if action[2] is 'u':
      temp=list((temp[0]+1,temp[1]))
     # print ' found the u\n\n'+str(getpos(self.board,(temp[0],temp[1])))
      tempstring=tempstring+action[0]
      while str(getpos(self.board,(temp[0],temp[1]))).isalpha():
        tempstring=tempstring+ str(getpos(self.board,tuple(temp)))
        temp=list((temp[0]+1,temp[1]))
      temp=list((temp[0]-1,temp[1]))
    #  print temp
    #  print action[1]
      #for i in xrange(temp[0]-action[1][0]):
        #print str((temp[0]+i,temp[1]))+ 'asd'
        #tempstring=tempstring+str(getpos(self.board,(temp[0]+i,temp[1])))
     # print tempstring
      return colec(tempstring,action[1],tuple(temp),action[1])
      
      
    elif action[2] is 'l':
      temp=list((temp[0],temp[1]+1))
      tempstring=tempstring+action[0]
     # print ' found the l\n\n'+str(getpos(self.board,(temp[0],temp[1])))
      while str(getpos(self.board,(temp[0],temp[1]))).isalpha():
        tempstring=tempstring+str(getpos(self.board,tuple(temp)))
        temp=list((temp[0],temp[1]+1))
      temp=list((temp[0],temp[1]-1))  
      #print temp
      #print action[1]
      #for i in xrange(temp[1]-action[1][1]):
        #print str((temp[0]+i,temp[1]))+ 'asd'
        #tempstring=tempstring+str(getpos(self.board,(temp[0],temp[1]+i)))
     # print tempstring
      return colec(tempstring,action[1],tuple(temp),action[1])
      
    elif action[2] is 'd':
      temp=list((temp[0]-1,temp[1]))
      #print ' found the d\n\n'
      while str(getpos(self.board,(temp[0],temp[1]))).isalpha():
        tempstring=tempstring+str(getpos(self.board,tuple(temp)))
        temp=list((temp[0]-1,temp[1]))
        #print getpos(self.board,tuple(temp))
      temp=list((temp[0]+1,temp[1]))
      tempstring=tempstring[::-1] +action[0]
      
      #print temp
      #print action[1]
      #print tempstring
      return colec(tempstring,tuple(temp),action[1],action[1])
      
    else:
      temp=list((temp[0],temp[1]-1))
      #print ' found the r\n\n'
      while str(getpos(self.board,(temp[0],temp[1]))).isalpha():
        tempstring=tempstring+str(getpos(self.board,tuple(temp)))
        temp=list((temp[0],temp[1]-1))
        #print getpos(self.board,tuple(temp))
      temp=list((temp[0],temp[1]+1))
      tempstring=tempstring[::-1] +action[0]
      #print temp
      #print action[1]
      #print tempstring
      return colec(tempstring,tuple(temp),action[1],action[1])
    
    return
  def value(self, state):
    return
 
    
    
if __name__ == "__main__":
  a=pyscrab()
  #a.insertword((1,1),(1,11),'abalienation')
  #a.insertword((1,1),(12,1),'abalienation')
  a.insertword((6,7),(10,7),'test')
  a.printboard()
  b=scrabble()
  c=WordSearch(a.board,b.player1hand)
  z=c.actions(c.initial)
  print c.result(c.initial,z[14])
