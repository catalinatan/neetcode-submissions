# Stack - LIFO

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        # sort with closest to target first

        for p, s in pair: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() 
            # if the car behind is slower than the front it will never catch up and 
            # become 2 fleets but if the car behind is faster then it will catch up 
            # they become one fleet thats why u pop it 
        return len(stack)