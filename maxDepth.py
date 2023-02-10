class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        maxStackSize = 0
        for character in s:
            if(character == '('):
                maxStackSize += 1
                maxDepth = max(maxStackSize, maxDepth)
            elif(character == ')'):
                maxStackSize -= 1
        return maxDepth