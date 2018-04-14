"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Stack(object):
   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]

   def isEmpty(self):
       return len(self.items) == 0
   
class Solution(object):
    def isValid(self, s):
        dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        st = Stack()
        for i in range(0, len(s)):
            if s[i] in ["(","[","{"]:
                st.push(s[i])
                # print st.items
            elif s[i] in [")","]","}"]:
                if st.isEmpty():
                    return False
                elif dict[s[i]] == st.peek():
                    st.pop()
                    # print st.items
                else:
                    return False
            else:
                pass
        if st.isEmpty():
            return True
        else:
            return False
        
