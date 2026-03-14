#
# Problem: 155. Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/submissions/1947970520/
# Language: python3
# Date: 2026-03-14


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.minStack[-1] if self.minStack else val, val) 
        self.minStack.append(val)
        


    def pop(self) -> None:
        self.stack.pop() if self.stack else -1
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack.pop() if self.stack else -1

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
