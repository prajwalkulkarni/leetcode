"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        boolean = False
        if s=="inf" or s=="-inf" or s=="+inf" or s=="Infinity" or s=="+Infinity" or s=="-Infinity" or s=="infinity" or s=="-infinity" or s=="+infinity":
            return False
        try:
            x = float(s)
            return True
        except ValueError:
            return False
            
