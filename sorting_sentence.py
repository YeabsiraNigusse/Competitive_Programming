class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        sortSentence = ''
        for i in range(len(word)):
             min = i
             for j in range(i+1,len(word)):
                  if word[j][-1] < word[min][-1]:
                      min = j
             word[i],word[min] = word[min], word[i]
             sortSentence+=word[i][:-1]+" "
        return sortSentence[:-1]
