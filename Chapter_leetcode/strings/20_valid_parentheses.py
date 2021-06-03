def isValid(str):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif len(stack) <= 0:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        if len(stack) == 0:
            return True
        return False


# s = "(]"
# isValid(s)
# solving this problem with a stack https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/