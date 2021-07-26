"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=[]
        carry=0
        
        if len(a) != len(b):
            if len(a)>len(b):
                diff = len(a)-len(b)
                #b=list(b)
                #b.append(diff*"0")
                #b.reverse()
                #b=str(''.join(b))
                append = diff*"0"
                append+=b
                b=append
            else:
                diff = len(b) - len(a)
                append = diff*"0"
                append+=a
                a=append
        a=list(str(a))
        b=list(str(b))
        print(a,b)
        for i in range(len(a)-1,-1,-1):
            #print(a[i])
            add = int(a[i])+int(b[i])
            if add >= 2:
                if carry==1:
                    res.append(str(carry))
                    carry=1
                else:
                    res.append(str(0))
                    carry=1
                #res.append(0)
            else:
                if carry==0:
                    res.append(str(add))
                else:
                    if carry+int(a[i])+int(b[i])>=2:
                        carry=1
                        res.append("0")
                        #print("in")
                    else:
                        res.append(str(carry))
                        carry=0
        
        if carry==1:
            res.append(str(carry))
        
        res.reverse()
        #print(str(res))
        
        return str(''.join(res))
        
