"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution(object):
    def isValid(self, s):
          
        stack = []
        
        for char in s:
            if char in ["(", "{", "["]:

                # Push the element in the stack
                stack.append(char)
            else:

                # IF current character is not opening
                # bracket, then it must be closing.
                # So stack cannot be empty at this point.
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False

        # Check Empty Stack
        if stack:
            return False
        return True
