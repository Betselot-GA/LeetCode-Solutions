#
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/submissions/1946134115/
# Language: python3
# Date: 2026-03-12


class Solution:
    def isValid(self, s: str) -> bool:
        # valid_parenthesis = ["()","{}","[]"]
        # left, right = 0, len(s)-1

        # if len(s) %2 != 0:
        #     return False

        # while left < right:
        #     parenthesis1 = s[left] + s[right]
        #     parenthesis2 = s[left] + s[left+1]


        #     if parenthesis1 in valid_parenthesis:
        #         left += 1
        #         right -= 1
        #     elif parenthesis2 in valid_parenthesis:
        #         left += 2
        #     else:
        #         return False
        # return True 
        valid_parenthesis = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c in valid_parenthesis:
                if stack and stack[-1] == valid_parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
