# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:01:28 2018

@author: admin
"""
"""Count words."""

def combine(outputList,sortList):  
    CombineList = list()
    for index in xrange(len(outputList)):  
        CombineList.append((outputList[index],sortList[index])) 
    return CombineList

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n most frequent words.
    
    words = s.split()
    words = sorted(words)
    count = [1 for x in range(len(words))]
    item = 0
    checked = [words[0]]
    
    for i in range(1,len(words)):
        if words[i] == words[i-1]:
            count[item] = count[item] + 1
        else:
            item = item + 1
            checked.append(words[i])
    
    count = count[0:item+1]
    
    words2 = combine(checked,count)
    words2.sort(key=lambda x:x[1],reverse=True)
    
    return words2[0:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
