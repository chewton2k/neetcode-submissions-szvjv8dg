class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Return the length of the shortest valid transformation sequence.
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])  # Each item is (word, number of words so far).
        words = set(wordList)
        visited = {beginWord}

        def neighbors(word):
            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == word[i]:
                        continue
                    candidate = word[:i] + letter + word[i + 1:]
                    if candidate in words:
                        yield candidate

        while q:
            current_word, length = q.popleft()
            for next_word in neighbors(current_word):
                if next_word in visited:
                    continue
                if next_word == endWord:
                    return length + 1
                visited.add(next_word)
                q.append((next_word, length + 1))
                
            
        return 0
