from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Create a set of wordList
        wordList = set(wordList)
        # Intialize queue with beginWord and length=1
        queue = deque([[beginWord, 1]])

        # Create a set of characters present in the wordList
        char_set = {w for word in wordList for w in word}

        while queue:
            # Pop the first element from the queue
            word, length = queue.popleft()

            # Return the length if end word is found
            if word == endWord:
                return length

            # Iterate for the length of word
            for i in range(len(word)):
                # Iterate over characters in the character set of wordList
                for c in char_set:

                    # Create possible words, and check if the new_word is in the wordList
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList:
                        # Remove the new_word from wordList and add it to the queue with length+1
                        wordList.remove(new_word)
                        queue.append([new_word, length+1])

        return 0
