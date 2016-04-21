# -*- coding: utf-8 -*-
import re
from collections import Counter
class StatWords(object):
        def statTopN(self,path, n):
                file = open(path,'r')
                wordDict = {}
                content = file.read()
                wordlist = re.split('[\s\ \\,\;\.\!\n]+', content)
                for word in wordlist:
                        if word in wordDict:
                                wordDict[word]=wordDict[word]+1
                        else:
                                wordDict[word] = 1
                count = Counter(wordDict)
                print count.most_common()[:n]


if __name__ == '__main__':
       s = StatWords()
       s.statTopN('test.txt',3)
                
                
        
