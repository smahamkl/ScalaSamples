from collections import defaultdict

class SpellChecker:
    def __init__(self):
        self.min = 100
        self.max = -1
        self.wordDict = defaultdict(lambda : "-1")

    def setUp(self, wordList):
        for word in wordList:
            if len(word) < self.min:
                self.min = len(word)
            if(len(word) > self.max):
                self.max = len(word)
            index = 0
            for char in word:
                self.wordDict[index] = [char] + self.wordDict.get(index, [])
                index += 1

    def isMatch(self, strings):
        print(self.min)
        print(self.max)
        for string in strings:
            index = 0
            if (len(string) >= self.min) & (len(string) <= self.max):
                for char in string:
                    if (char != '.') & (char not in self.wordDict.get(index, [])):
                        print(string + ": not match")
                        break
                    index += 1
            else:
                print(string + ": not match")

if __name__ == "__main__":
    sc = SpellChecker()
    sc.setUp(['cat', 'bat', 'rat', 'drat', 'dart', 'drab'])
    sc.isMatch(['act','c.t','.at','..t','d..t','dr..','...','....', '.....', 'h.t', 'c', '.'])
    # for word in checks:
    #     print(speller.isMatch(word))