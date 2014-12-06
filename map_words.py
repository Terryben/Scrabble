#! /usr/bin/python
import sys
def readWords(text_file):
  f = open(text_file)
  dictionary = {}
  for line in f:
    dictionary[line.rstrip()] = True
  f.close()
  return dictionary

def alphabetScore():
  alphScore = {'e':1, 'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
  return alphScore

def wordScore(word, alphScore):
  word = word.lower()
  score = 0
  for i in range(0,len(word)):
    score += alphScore[word[i]]
  return score

def isValidWord(word):
  word = word.lower()
  try:
    if dictionary[word]:
      return True
    else:
      return False
  except KeyError:
    return False
  

if __name__== "__main__":
  if len(sys.argv) < 2:
    print "Please provide a text file to create the dictionary."
    sys.exit()
  
  dictionary = readWords(sys.argv[1])
  num_args = len(sys.argv)
  alphScore = alphabetScore()
  #print dictionary.keys()
  while num_args > 2:
    word = sys.argv[num_args-1]
    print word + " is a valid word? " + str(isValidWord(word))
    print "The word score is: " + str(wordScore(word, alphScore))
    num_args = num_args - 1
