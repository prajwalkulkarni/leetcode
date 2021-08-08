"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        can=[]
        n=len(words)
        
        #words = [i.lower() for i in words]
        keyboard = ["QWERTYUIOPqwertyuiop","ASDFGHJKLasdfghjkl","ZXCVBNMzxcvbnm"]
        
        toCheck =  -1
        string=""
        flag=0
        for i in range(0,n):
            #print(words[i][0])
            if words[i][0] in keyboard[0]:
                toCheck = 0
            elif words[i][0] in keyboard[1]:
                #print("H here;")
                toCheck = 1
            elif words[i][0] in keyboard[2]:
                toCheck = 2
            
            
            if toCheck != -1:
                #print("XX")
                for j in words[i]:
                    if j in keyboard[toCheck]:
                        string+=j
                    else:
                        string=""
                        break
                        
                if string == words[i]:
                    #print("Yes")
                    can.append(words[i])
                    string=""
            
        
        
        return can
                
