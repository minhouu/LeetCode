class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")" : "(",
               "}" : "{",
               "]" : "["}
        stack = []
        for i in s :
            if i == "(" or i == "[" or i ==  "{" :
                stack.append(i)

            else :
                if stack and pair[i] == stack[-1] :
                    stack.pop()
                else :
                    return False
        return stack == []