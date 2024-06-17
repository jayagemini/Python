class Solution(object):
    def isValid(self, s):
        matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening parentheses
        stack = []
    
    # Iterate through each character in the string
        for c in s:
        # If the character is a closing parenthesis
            if c in matching_parentheses:
                if stack and stack[-1]==matching_parentheses[c]:
                    stack.pop()
                else:
                    return False    
            # Pop from stack if it's not empty, otherwise assign a dummy value

              
            else:
            # If it's an opening parenthesis, push it onto the stack
                stack.append(c)
    
    # If the stack is empty at the end, all parentheses are valid
        return True if not stack else False
  

        
        

c=Solution()
print(c.isValid("([)]"))        
# Example usage
print(c.isValid("()"))         # True
print(c.isValid("()[]{}"))     # True
print(c.isValid("(]"))         # False
print(c.isValid("([)]"))       # False
print(c.isValid("{[]}"))       # True
