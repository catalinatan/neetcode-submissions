class Solution:
    def isValid(self, s: str) -> bool:
        par_pairs = {"(": ")", "{": "}", "[": "]"}
        open_par = par_pairs.keys()
        close_par = [")", "}", "]"]
        empty_list = []
        for char in s: 
            if char in open_par: 
                empty_list.append(par_pairs[char])
                print(empty_list)
            if not empty_list:
                return False
            if char in close_par: 
                last_item = empty_list.pop()
                if char == last_item: 
                    pass
                else:
                    return False 
                print(empty_list)
        
        if len(empty_list) == 0: 
            return True
        else:
            return False
