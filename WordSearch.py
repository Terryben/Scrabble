import search
import utils
from pyscrab import pyscrab
from scrabble import scrabble
from map_words import *
import random

class colec:
  def __init__ (self,word,tup11,tup12,lista,playerhand):
    self.word=word
    self.start=tup11
    self.end=tup12
    self.hand=playerhand
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
    return self.word+' '+ str(self.start)+ ' ' +str(self.end)+ ' '+ str(self.last) + ' '+ str(self.hand)
  def totup(self):
    return (self.word,tuple(self.start),tuple(self.end),tuple(self.last),tuple(self.hand))
  
def getpos(board,tup1):
  t11=tup1[0]
  t12=tup1[1]
  return board[t11*15+t12]


class WordSearch:
  def __init__ (self,boardstate,playerhand):
    self.board=boardstate
    self.hand=playerhand
    #print self.hand
    self.initial=('',(0,0),(0,0),tuple([]),tuple(playerhand))
  def actions(self, state):
    #print str(state) + ' in actions'test5.so
    actions=[]
    state1=colec(state[0],state[1],state[2],list(state[3]),list(state[4]))
    if state1.gettup1() == ((0,0),(0,0)) and len(state1.gettup2()) ==0 and state1.word is '':
      pos=[]
      for i in range(len((self.board.board))):
        if str(self.board.board[i]).isalpha():
          pos.append([i/15,i%15])
          break;
      #print getpos(self.board.board,tuple(pos[0]))
      temp=pos[0]
      #while str(getpos(self.board.board,(temp[0],temp[1]+1))).isalpha():
      #  temp=list((temp[0],temp[1]+1))
       # print getpos(self.board.board,tuple(temp))
      if pos[0][0] is not 0:
        for i in state1.hand:
          actions.append((i,(pos[0][0]-1,pos[0][1]),'u'))
      if pos[0][1] is not 0:
        for i in state1.hand:
          actions.append((i,(pos[0][0],pos[0][1]-1),'l'))      
      if str(getpos(self.board.board,(pos[0][0]+1,pos[0][1]))).isalpha() is False:
        for i in state1.hand:
          actions.append((i,(pos[0][0]+1,pos[0][1]),'d')) 
      if str(getpos(self.board.board,(pos[0][0],pos[0][1]+1))).isalpha() is False:
        for i in state1.hand:
          actions.append((i,(pos[0][0],pos[0][1]+1),'r'))                       
      #print state.hand
      #print actions
    else:
      #print 'not in base case'
      #print state.hand
      # CASE 1, add another letter to the word
      pos=state1.gettup1()

      #print state.gettup1()
      if pos[0][0] is pos[1][0] and len(state1.hand)!= 0:
        #print 'they are in a row'
        if pos[0][1] is not 0 and str(getpos(self.board.board,(pos[0][0],pos[0][1]-1))).isalpha() is False:
          for i in state1.hand: ##left
            actions.append((i,(pos[0][0],pos[0][1]-1),'l'))  
        if pos[1][1] is not 14 and str(getpos(self.board.board,(pos[1][0],pos[1][1]+1))).isalpha() is False:
          for i in state1.hand:## right
            actions.append((i,(pos[1][0],pos[1][1]+1),'r'))     
      if pos[0][1] is pos[1][1] and len(state1.hand)!= 0:
        #print 'they are in a col'
        if pos[0][0] is not 0 and str(getpos(self.board.board,(pos[0][0]-1,pos[0][1]))).isalpha() is False:
          for i in state1.hand:
            actions.append((i,(pos[0][0]-1,pos[0][1]),'u'))
        if pos[1][0] is not 14 and str(getpos(self.board.board,(pos[1][0]+1,pos[1][1]))).isalpha() is False:
          for i in state1.hand:
            actions.append((i,(pos[1][0]+1,pos[1][1]),'d'))
      
      #CASE 2: swap out a letter already in the word
      if len(state1.hand)!= 0 and len(state1.word)!= 0:
        for i in state1.last:
          for j in state1.hand:
            actions.append((j,i[0],'replace',i[1]))
      
      '''
        first=0
        last=1
        for item in state1.last:
          if item[0] is state1.start:
            first=item[1]
          elif item[0] is state.end:
            last=item[1]
        for j in state1.hand:
          if last != 1:
          actions.append((j,state1.start,'replace',first))
          actions.append((j,state1.end,'replace',last))
      '''
      
      #CASE 3: Remove a letter from the word
      if len(state1.word)!= 0:
        for i in state1.last:
          if i[0] is state1.start or i[0] is state1.end:
            actions.append((i[1],i[0],'remove'))
      
      
      #CASE 4: move a letter already on the board
      if pos[0][0] is pos[1][0]:
        test=0
        j=True
        if len(state1.last) is 0:
          j=False
        test=pos[0]
        while j:
          for i in state1.last:
            #print test,i[0]
            if test is i[0]:
              test=(pos[0][0],pos[0][1]+1)
              break
            else:
              j=False
              break
        asdf=[]
        for i in state1.last:
          asdf.append(i[0])
        if str(getpos(self.board.board,(test[0]-1,test[1]))).isalpha() is True:
          actions.append(('0',(test[0]-1,test[1]),'change'))
        if str(getpos(self.board.board,(test[0]+1,test[1]))).isalpha() is True:
          actions.append(('0',(test[0]+1,test[1]),'change'))
        if str(getpos(self.board.board,(test[0],test[1]+1))).isalpha() is True and test not in asdf:
          actions.append(('0',(test[0],test[1]+1),'change'))
      else:
        #print 'they are in a col'
        test=0
        j=True
        if len(state1.last) is 0:
          j=False
        test=pos[0]
        while j:
          for i in state1.last:
            if test is i[0]:
              test=(pos[0][0]+1,pos[0][1])
              break
            else:
              j=False
              break
        asdf=[]
        for i in state1.last:
          asdf.append(i[0])
        if str(getpos(self.board.board,(test[0],test[1]-1))).isalpha() is True:
          actions.append(('0',(test[0],test[1]-1),'change'))
        if str(getpos(self.board.board,(test[0],test[1]+1))).isalpha() is True:
          actions.append(('0',(test[0],test[1]+1),'change'))
        if str(getpos(self.board.board,(test[0]+1,test[1]))).isalpha() is True and test not in asdf:
          actions.append(('0',(test[0]+1,test[1]),'change'))
      
      #print state.hand
      #print state
    random.shuffle(actions)
    return actions
  def result(self,state,action):
    state1=colec(state[0],state[1],state[2],list(state[3]),list(state[4]))
    #print str(state) +  '   printing state   action: ' + str(action[2])
   # print str(state1)  + ' in result'
    #print action
    tempstring=""
    temp=list(action[1])
    
    asd=[]
    for i in state1.last:
      asd.append(i[0])
    
    if action[2] is 'u' and action[1] not in asd:
      temp=list((temp[0]+1,temp[1]))
     # print ' found the u\n\n'+str(getpos(self.board.board,(temp[0],temp[1])))
      tempstring=action[0]
      if len(state1.word) is 0:
        while str(getpos(self.board.board,(temp[0],temp[1]))).isalpha():
          tempstring=tempstring+ str(getpos(self.board.board,tuple(temp)))
          temp=list((temp[0]+1,temp[1]))
        temp=list((temp[0]-1,temp[1]))
      else:
        tempstring=action[0]+state1.word
        temp=state1.end
    #  print temp
    #  print action[1]
      #for i in xrange(temp[0]-action[1][0]):
        #print str((temp[0]+i,temp[1]))+ 'asd'
        #tempstring=tempstring+str(getpos(self.board.board,(temp[0]+i,temp[1])))
     # print tempstring
      a=state1.last
      a.append(((action[1]),action[0]))
      b=state1.hand
     # print 'a ' +str(a)
     # print 'b '+ str(b)
     # print action
      b.remove(action[0])
      c=colec(tempstring,action[1],temp,a,b).totup()
     # print c
      return c
      
      
    elif action[2] is 'l' and action[1] not in asd:
      temp=list((temp[0],temp[1]+1))
      tempstring=action[0]
     # print ' found the l\n\n'+str(getpos(self.board.board,(temp[0],temp[1])))
     
      if len(state1.word) is 0:
        while str(getpos(self.board.board,(temp[0],temp[1]))).isalpha():
          tempstring=tempstring+str(getpos(self.board.board,tuple(temp)))
          temp=list((temp[0],temp[1]+1))
        temp=list((temp[0],temp[1]-1))
      else:
        tempstring=action[0]+state1.word
        temp=state1.end
      #print temp
      #print action[1]
      #for i in xrange(temp[1]-action[1][1]):
        #print str((temp[0]+i,temp[1]))+ 'asd'
        #tempstring=tempstring+str(getpos(self.board.board,(temp[0],temp[1]+i)))
     # print tempstring
      a=state1.last
      a.append(((action[1]),action[0]))
      b=state1.hand
     # print 'a ' +str(a)
      #print 'b '+ str(b)
     # print action
      b.remove(action[0])
      #print tempstring
      c=colec(tempstring,action[1],temp,a,b).totup()
     # print c
      return c
      
    elif action[2] is 'd' and action[1] not in asd:
      temp=list((temp[0]-1,temp[1]))
      #print ' found the d\n\n'
      #tempstring=action[0]
      
      if len(state1.word) is 0:
        while str(getpos(self.board.board,(temp[0],temp[1]))).isalpha():
          tempstring=tempstring+str(getpos(self.board.board,tuple(temp)))
          temp=list((temp[0]-1,temp[1]))
        #print getpos(self.board.board,tuple(temp))
        temp=list((temp[0]+1,temp[1]))
        tempstring=tempstring[::-1] +action[0]
      else:
        tempstring=state1.word+action[0]
        temp=state1.start
      #print temp
      #print action[1]
      #print tempstring
      a=state1.last
      a.append(((action[1]),action[0]))
      b=state1.hand
      b.remove(action[0])
      #print tempstring
      c=colec(tempstring,temp,action[1],a,b).totup()
      #print c
      return c
      
    elif action[2] is 'r' and action[1] not in asd:
      temp=list((temp[0],temp[1]-1))
      #print ' found the r\n\n'
      #tempstring=action[0]
      if len(state1.word) is 0:
        while str(getpos(self.board.board,(temp[0],temp[1]))).isalpha():
          tempstring=tempstring+str(getpos(self.board.board,tuple(temp)))
          temp=list((temp[0],temp[1]-1))
        #print getpos(self.board.board,tuple(temp))

        temp=list((temp[0],temp[1]+1))
        tempstring=tempstring[::-1] +action[0]
      else:
        tempstring=state1.word+action[0]
        temp=state1.start
     
      #print temp
      #print action[1]
      #print tempstring
      a=state1.last
      a.append(((action[1]),action[0]))
      b=state1.hand
      b.remove(action[0])
      c=colec(tempstring,temp,action[1],a,b).totup()
      #print c
      return c
    
    elif action[2] is 'replace':
      #print 'in replace ' + str(action)
      #print str(state) + ' start'
      pos=state1.gettup1()
      spot=action[1]
      temp=state1.start
      '''
      if action[1] is state1.start:
        tempstring=action[0]+state1.word[1:]
      else:
        tempstring=state1.word[:len(state1.word)-1]+action[0]
      '''
      
      if pos[0][0] is pos[1][0]:
        counter=0
        while True:
          #print temp, action[1]
          if temp[0] == action[1][0] and temp[1] == action[1][1]:
            tempstring=tempstring+action[0]
           # print 'found it'
          else:
            #print temp
            tempstring=tempstring+state1.word[counter]
          counter=counter+1
          temp=(temp[0],temp[1]+1)
          if temp[1]>state1.end[1]:
            break
      
      else:
        counter=0
        while True:
          if temp[0] == action[1][0] and temp[1] == action[1][1]:
            tempstring=tempstring+action[0]
            #print 'found it'
          else:
           # print temp
            tempstring=tempstring+state1.word[counter]
          temp=(temp[0]+1,temp[1])
          counter=counter+1
          if temp[0]>state1.end[0]:
            break
            
      #print tempstring
      b=state1.hand
      b.remove(action[0])
      b.append(action[3])
      a=state1.last
      a.remove((action[1],action[3]))
      a.append((action[1],action[0]))
      c=colec(tempstring,state1.start,state1.end,a,b).totup()
      #print str(c)+ ' finish'
      return c
      
      
      
      
    elif action[2] is 'remove':
     # print 'in remove ' + str(action)
     # print str(state) + ' start'
      pos=state1.gettup1()
      temp= state1.start
      temp1=state1.end
      tempstring=state1.word
      if pos[0][0] is pos[1][0]:
        if action[1] is state1.start:
          tempstring=state1.word[1:]
          temp=(temp[0],temp[1]+1)
        else:
          tempstring=state1.word[:len(state1.word)-1]
          temp1=(temp1[0],temp1[1]-1)
      else:
        if action[1] is state1.start:
          tempstring=state1.word[1:]
          temp=(temp[0]+1,temp[1])
        else:
          tempstring=state1.word[:len(state1.word)-1]
          temp1=(temp1[0]-1,temp1[1])
      '''
      if pos[0][0] is pos[1][0]:
        if temp is action[1]:
          temp=(action[1][0],action[1][1]+1)
          tempstring=tempstring[1:]
        else:
          temp1=(action[1][0],action[1][1]-1)
          tempstring=tempstring[:len(tempstring)]
      else:
        if temp is action[1]:
          temp=(action[1][0]+1,action[1][1])
          tempstring=tempstring[1:]
        else:
          temp1=(action[1][0]-1,action[1][1])
          tempstring=tempstring[:len(tempstring)]
      '''
      a=state1.last
      a.remove((action[1],action[0]))
      b=state1.hand
      b.append(action[0])
      c=colec(tempstring,temp,temp1,a,b).totup()
     # print str(c) + ' finish'
      return c
      
      
    elif action[2] is 'change':
    #  print 'in change '  + str(action)
     # print str(state) + ' start'
      a=state1.last
      b=state1.hand
      for i in state1.last:
        b.append(i[1])
        a.remove(i)
      tempstring=str(getpos(self.board.board,action[1]))
      c=colec(tempstring,action[1],action[1],a,b).totup()
      #print str(c) + ' finish'
      return c
    
    
    return
  def value(self, state):
    asdf=map_words()
    if asdf.isValidWord(state[0]) is False:
      return 0
    else:
      return asdf.wordScore(state[0],self.board,state[1],state[2])
  def path_cost(self, c, state1, action, state2): # my code would not work unless I copied and pasted this from search.py
    return c+1 
    
    
if __name__ == "__main__":
  a=pyscrab()
  #a.insertword((1,1),(1,11),'abalienation')
  #a.insertword((1,1),(12,1),'abalienation')
  a.insertword((6,7),(9,7),'test')
  #a.printboard()
  '''
  b=scrabble()
  print b.player2hand
  c=WordSearch(a.board,b.player2hand)
  z=c.actions(c.initial)
  
  print temp
  #print temp
  z1=c.actions(temp)
  temp1=c.result(temp,z1[19])
  print temp1
  '''

  b=scrabble()
  #print b.player2hand
  c=WordSearch(a,b.player2hand)
  z=c.actions(c.initial)
  temp=c.result(c.initial,z[0])
  G =WordSearch(a,b.player2hand)
  asdf=map_words()
  test4=search.simulated_annealing(G)
  test5=search.hill_climbing(G)
  for i in test4.path():
    if asdf.isValidWord(i.state[0]) is True:
      print asdf.wordScore(i.state[0],a,i.state[1],i.state[2]),i.state[0]
  for i in test5.path():
    if asdf.isValidWord(i.state[0]) is True:
      print asdf.wordScore(i.state[0],a,i.state[1],i.state[2]),i.state[0]
  
