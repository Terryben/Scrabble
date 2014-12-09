#! /usr/bin/python
import sys
class map_words():

  

  def __init__ (self):
    self.dictionary = self.readWords('words.txt')
    self.alphScore = self.alphabetScore()

  def readWords(self, text_file):
    f = open(text_file)
    dictionary = {}
    for line in f:
      dictionary[line.rstrip()] = True
    f.close()
    return dictionary

  def alphabetScore(self):
    alphScore = {'e':1, 'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
    return alphScore

  def findWordPos(self, tup1, tup2):
    #print "IN HERE"
    posArray = []
    #print str(tup1[1] - tup2[1])
    
    if ((tup1[1] - tup2[1]) == 0):  #the word is parallel with the y axis
      #print "here now " + str(abs(tup2[0]-tup1[0]))
      for i in range(0, abs(tup2[0]-tup1[0])+1):
        #print "The length in y is: "
        #print str(tup2[0]-tup1[0])
        letterlocal = (tup1[0]+i, tup1[1])
        #print "The letter is: "
        #print letterlocal
        posArray.append(letterlocal)
      return posArray
    else:        #the word is along the x axis
      #print "here now2 " + str(abs(tup2[1]-tup1[1]))
      for i in range(0, abs(tup2[1]-tup1[1])+1):
        #print "The length in x is: "
        #print i
        letterlocal = (tup1[0], tup1[1]+i)
        #print "The letter is: "
        #print letterlocal
        posArray.append(letterlocal)
      return posArray

  def wordScore(self, word, board, tup1, tup2):
    wordPos = self.findWordPos(tup1, tup2)
    #print "The wordPos is: "
    #print wordPos
    low_word = []
    for i in range(0, len(word)):
      low_word.append(word[i].lower())
    word = low_word
    score = 0
    word_mult = 1
    letter_mult = 1
    for i in range(0,len(word)):
      pos = wordPos[i][0]*15+wordPos[i][1]
      print board.empty[pos]
      if board.empty[pos] == 4:
        word_mult = word_mult*3
        print "word mult is: " + str(word_mult)
      elif board.empty[pos] == 3 or   board.empty[pos] == -1:
        word_mult = word_mult*2
        print "word mult is: " + str(word_mult)
      elif board.empty[pos] == 2:
        letter_mult = 3
        print "letter mult is: " + str(letter_mult)
      elif board.empty[pos] == 1:
        letter_mult = 2
        print "letter mult is: " + str(letter_mult)
      score += self.alphScore[word[i]]*letter_mult
      #print "The word[i] is: " + word[i]
      letter_mult = 1
      
    score = score*word_mult
    return score

  def isValidWord(self, word):
    low_word = ""
    for i in range(0, len(word)):
      low_word += str(word[i])
    try:
      if self.dictionary[low_word]:
        return True
      else:
        return False
    except KeyError:
      return False
    

  #if __name__== "__main__":
  #  if len(sys.argv) < 2:
  #    print "Please provide a text file to create the dictionary."
  #    sys.exit()
    
  #  dictionary = readWords(sys.argv[1])
  #  num_args = len(sys.argv)
  #  alphScore = alphabetScore()
    #print dictionary.keys()
  #  while num_args > 2:
  #    word = sys.argv[num_args-1]
  #    print word + " is a valid word? " + str(isValidWord(word))
  #    print "The word score is: " + str(wordScore(word, alphScore, (1,2), (1, 5)))
  #    num_args = num_args - 1
