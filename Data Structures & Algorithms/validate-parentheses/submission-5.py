class Solution:
    def isValid(self, s: str) -> bool:
        close_dict = {'}': '{', ']': '[', ')': '('}
        paren_list = [] 

        for char in s: 
            if char in close_dict and len(paren_list) > 0: 
                last_element = paren_list.pop()
                if last_element != close_dict[char]:
                    return False
            else:
                paren_list.append(char)
        
        if len(paren_list) == 0: 
            return True
        else:
            return False
            
        
        