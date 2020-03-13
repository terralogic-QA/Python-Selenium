class validateParanthesis:
   def is_valid_parenthese(self, str1):
        stack, parenthese = [], {"(": ")", "{": "}", "[": "]"}
        for charac in str1:
            if charac in parenthese:
                stack.append(charac)
            elif len(stack) == 0 or parenthese[stack.pop()] != charac:
                return False
        return len(stack) == 0


print(validateParanthesis().is_valid_parenthese("(){}[]"))
print(validateParanthesis().is_valid_parenthese("()[{)}"))

