class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #create stack, enter openning brackets, find closing brackets, if they match, pop. if not return false
        stack = []
        slen = len(s)
        for i in range(slen):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i])
            elif(not stack): #empty stack is 0, not on empty = 1
                return False
            else:
                if(s[i] == ')' and stack[-1] == '('):
                    stack.pop()
                elif(s[i] == ']' and stack[-1] == '['):
                    stack.pop()
                elif(s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        if(not stack):
            return True
        return False