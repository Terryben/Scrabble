import search
import utils
from pyscrab import pyscrab
from scrabble import scrabble
import map_words

class colec:
  def __init__ (self,word,tup11,tup12,lista):
    self.word=word
    self.start=tup11
    self.end=tup12
    #print len(lista)
    if len(lista) != 0:
      self.last=lista
    else:
      self.last=[]
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
    #print self.hand
    self.initial=colec('',(0,0),(0,0),[])
  def actions(self, state):
    actions=[]
    if state.gettup1() == ((0,0),(0,0)) and len(state.gettup2()) ==0 and state.word is '':
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
        for i in self.hand:
          actions.append([i,(pos[0][0]-1,pos[0][1]),'u'])
      if pos[0][1] is not 0:
        for i in self.hand:
          actions.append([i,(pos[0][0],pos[0][1]-1),'l'])      
      if str(getpos(self.board,(pos[0][0]+1,pos[0][1]))).isalpha() is False:
        for i in self.hand:
          actions.append([i,(pos[0][0]+1,pos[0][1]),'d']) 
      if str(getpos(self.board,(pos[0][0],pos[0][1]+1))).isalpha() is False:
        for i in self.hand:
          actions.append([i,(pos[0][0],pos[0][1]+1),'r'])                       
      #print self.hand
      #print actions
    else:
      #print 'not in base case'
      #print self.hand
      for i in state.last:
        #print i[1]
        self.hand.remove(i[1])
      
      # CASE 1, add another letter to the word
      pos=state.gettup1()
      #print state.gettup1()
      if pos[0][0] is pos[1][0]:
        #print 'they are in a row'
        if pos[0][1] is not 0 and str(getpos(self.board,(pos[0][0],pos[0][1]-1))).isalpha() is False:
          for i in self.hand: ##left
            actions.append([i,(pos[0][0],pos[0][1]-1),'l'])  
        if pos[1][1] is not 14 and str(getpos(self.board,(pos[1][0],pos[1][1]+1))).isalpha() is False:
          for i in self.hand:## right
            actions.append([i,(pos[1][0],pos[1][1]+1),'r'])     
      else:
        #print 'they are in a col'
        if pos[0][0] is not 0 and str(getpos(self.board,(pos[0][0]-1,pos[0][1]))).isalpha() is False:
          for i in self.hand:
            actions.append([i,(pos[0][0]-1,pos[0][1]),'u'])
        if pos[1][0] is not 14 and str(getpos(self.board,(pos[1][0]+1,pos[1][1]))).isalpha() is False:
          for i in self.hand:
            actions.append([i,(pos[1][0]+1,pos[1][1]),'d'])
      
      #CASE 2: swap out a letter already in the word
      for i in state.last:
        for j in self.hand:
          actions.append([j,i[0],'replace',i[1]])
      
      
      
      #CASE 3: Remove a letter from the word
      for i in state.last:
        for j in self.hand:
          if i[0] is state.start or i[0] is state.end:
            actions.append([j,i[0],'remove',i[1]])
      
      
      #CASE 4: move a letter already on the board
      if pos[0][0] is pos[1][0]:
        test=0
        j=True
        test=pos[0]
        while j:
          for i in state.last:
            #print test,i[0]
            if test is i[0]:
              test=(pos[0][0],pos[0][1]+1)
              break
            else:
              j=False
              break
        asdf=[]
        for i in state.last:
          asdf.append(i[0])
        if str(getpos(self.board,(test[0]-1,test[1]))).isalpha() is True:
          actions.append(['0',(test[0]-1,test[1]),'change'])
        if str(getpos(self.board,(test[0]+1,test[1]))).isalpha() is True:
          actions.append(['0',(test[0]+1,test[1]),'change'])
        if str(getpos(self.board,(test[0],test[1]+1))).isalpha() is True and test not in asdf:
          actions.append(['0',(test[0],test[1]+1),'change'])
      else:
        #print 'they are in a col'
        test=0
        j=True
        test=pos[0]
        while j:
          for i in state.last:
            if test is i[0]:
              test=(pos[0][0]+1,pos[0][1])
              break
            else:
              j=False
              break
        asdf=[]
        for i in state.last:
          asdf.append(i[0])
        if str(getpos(self.board,(test[0],test[1]-1))).isalpha() is True:
          actions.append(['0',(test[0],test[1]-1),'change'])
        if str(getpos(self.board,(test[0],test[1]+1))).isalpha() is True:
          actions.append(['0',(test[0],test[1]+1),'change'])
        if str(getpos(self.board,(test[0]+1,test[1]))).isalpha() is True and test not in asdf:
          actions.append(['0',(test[0]+1,test[1]),'change'])
      
      #print self.hand
      #print state
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
      a=state.last
      a.append(((action[1]),action[0]))
      return colec(tempstring,action[1],tuple(temp),a)
      
      
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
      a=state.last
      a.append(((action[1]),action[0]))
      return colec(tempstring,action[1],tuple(temp),a)
      
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
      a=state.last
      a.append(((action[1]),action[0]))
      return colec(tempstring,tuple(temp),action[1],a)
      
    elif action[2] is 'r':
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
      a=state.last
      a.append(((action[1]),action[0]))
      return colec(tempstring,tuple(temp),action[1],(a))
    
    return
  def value(self, state):
    return
 
    
    
if __name__ == "__main__":
  a=pyscrab()
  #a.insertword((1,1),(1,11),'abalienation')
  #a.insertword((1,1),(12,1),'abalienation')
  a.insertword((6,7),(10,7),'test')
  #a.printboard()
  b=scrabble()
  c=WordSearch(a.board,b.player2hand)
  z=c.actions(c.initial)
  temp=c.result(c.initial,z[7])
  print temp
  #print temp
  z1=c.actions(temp)
