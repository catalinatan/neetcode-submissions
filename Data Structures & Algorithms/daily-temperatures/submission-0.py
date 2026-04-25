class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return result(list) ith day before a warmer temp appears on a future day, if no day in the future
        # set result[i] to 0 if no warmer day 
        result = []

        for i in range(len(temperatures)):
            days = 0 
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]: 
                    days = j - i
                    break
            result.append(days)
            
        return result