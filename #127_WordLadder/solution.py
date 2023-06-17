# Method: BFS: Create wordList set and create all charset; then queue the beginWord and check each word by replacing 1 char at a time, if it exist in wordList
# TC: O(m*n + 26*n) = O(m*n), where m=Length of longest word, n=No. of words in the list
# SC: O(m)
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Create a set of wordList
        wordList = set(wordList)
        # Intialize queue with beginWord and length=1
        queue = deque([[beginWord, 1]])

        # Create a set of characters present in the wordList
        charSet = {ch for word in wordList for ch in word}

        while queue:
            # Pop the first element from the queue
            word, length = queue.popleft()

            # Return the length if end word is found
            if word == endWord:
                return length

            # Iterate for the length of word
            for i in range(len(word)):
                # Iterate over characters in the character set of wordList
                for c in charSet:

                    # Create possible words, and check if the newWord is in the wordList
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordList:
                        # Remove the newWord from wordList and add it to the queue with length+1
                        wordList.remove(newWord)
                        queue.append([newWord, length+1])

        return 0
