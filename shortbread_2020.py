from collections import deque
def neighboursOf(parent, parentsRecord, availableWords):
    neighbours = set(parent[:position] + replacementLetter + parent[position+1:]
        for position, originalLetter in enumerate(parent)
        for replacementLetter in 'abcdefghijklmnopqrstuvwxyz'
        if replacementLetter != originalLetter) & availableWords
    parentsRecord.update(dict.fromkeys(neighbours,parent))
    return neighbours
def shortbread(startWord, endWord, words):
    currentFrontLevel, currentBackLevel = set([startWord,]), set([endWord,])
    frontParents, backParents = {startWord:None} , {endWord:None}
    while True:
        words = (words - currentFrontLevel) - currentBackLevel
        nextFrontLevel = set.union(*(neighboursOf(word, frontParents, words) for word in currentFrontLevel))
        commonWord = (nextFrontLevel & currentBackLevel).pop() if (nextFrontLevel & currentBackLevel) else None
        if commonWord: break
        nextBackLevel = set.union(*(neighboursOf(word, backParents, words) for word in currentBackLevel))
        commonWord = (nextBackLevel & nextFrontLevel).pop() if (nextBackLevel & nextFrontLevel) else None
        if commonWord: break
        currentFrontLevel, currentBackLevel = nextFrontLevel, nextBackLevel
    path = deque([commonWord,])
    while any([frontParents.get(path[0]),backParents.get(path[-1])]):
        path.appendleft(frontParents.get(path[0]))
        path.append(backParents.get(path[-1]))
    return path

if __name__ == "__main__":
    import argparse
    import time
    from statistics import mean, stdev
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=str, default='short')
    parser.add_argument('--end', type=str, default='bread')
    args = parser.parse_args()
    start = time.time()
    words = set(line.strip() for line in open('english_words.txt')
        if len(line.strip())==len(args.start))
    start2 = time.time()
    print(shortbread(args.start, args.end, words))
    end = time.time()
    print(str((end-start) * 1000) + ' ms (Including Read words into container)' )
    print(str((end-start2) * 1000) + ' ms (Bidirectional BFS only)' )
    start, end = [], []
    for i in range(100):
        start.append(time.time())
        shortbread(args.start, args.end, words)
        end.append(time.time())
    times = [e-s for s,e in zip(start,end)]
    print(str(mean(times)*1000) + '+/-' + str(stdev(times)*1000) +
        ' ms (Bidirectional BFS only avg over 100 iterations)')
