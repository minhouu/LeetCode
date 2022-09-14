class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i == "(" or i == "[" or i ==  "{" :
                stack.append(i)

            else :
                if stack and stack[-1] == "(" : 
                    if i == ")" : 
                        stack.pop()
                        continue
                if stack and stack[-1] == "[" : 
                    if i == "]" :
                        stack.pop()
                        continue
                if stack and stack[-1] == "{" : 
                    if i == "}" : 
                        stack.pop()
                        continue
                else :
                    return False
        if stack :
            return False
        else :
            return True