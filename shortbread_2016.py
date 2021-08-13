from collections import deque
from string import ascii_lowercase

# --- Data setup
f=open("british-english",'r')

fiveLetterWords = set([line[:-1].lower() for line in f if len(line[:-1])==5])
fiveLetterWords.remove('short')

# --- Helper Functions
def neighboursOf(word):
    neighbourList=[]
    for i in range(5):
        for j in (k for k in ascii_lowercase if k!=word[i]):
            CandidateWord=word[:i]+j+word[i+1:]
            if CandidateWord in fiveLetterWords:
                neighbourList.append(CandidateWord)
                fiveLetterWords.remove(CandidateWord)
    return neighbourList

# --- Algorithm
path=deque()
previousLevels = set()
previousLevels.add('short')
parent = {'short':None}
frontLevel=['short']
pathword='bread'
while pathword!='short':
    nextLevel=[]
    for word in frontLevel:
        nbs=neighboursOf(word)
        for joiningWord in nbs:
            if joiningWord not in previousLevels:
                previousLevels.add(joiningWord)
                parent[joiningWord]=word
                nextLevel.append(joiningWord)
            if joiningWord=='bread':
                pathword=joiningWord
                while pathword:
                    path.appendleft(pathword)
                    pathword=parent[pathword]
                break
        else:
            continue
        break
    else:
        frontLevel=nextLevel
        continue
    break

print path    
