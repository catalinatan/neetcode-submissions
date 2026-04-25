class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force 
        # result = []

        # for i in range(len(temperatures)):
        #     days = 0 
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]: 
        #             days = j - i # how many days to wait not index 
        #             break
        #     result.append(days)
            
        # return result

        # stack 
        result = [0] * len(temperatures)
        stack = [] # pair = [temp, index]
        # pop from stack after appending i at each one, if j > i 
        for i, t in enumerate(temperatures): 
            while stack and t  > stack[-1][1]: # current temp > top element in stack
                stackIdx, stackT = stack.pop() # remove top element from stack
                result[stackIdx] = (i - stackIdx)
            stack.append([i, t])

        return result 