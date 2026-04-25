class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        strs_len = len(strs)
        if strs_len != 0: 
            for idx in range(strs_len):
                word = strs[idx]
                if idx < strs_len - 1:
                    output_str += word + "~~~"
                else:
                    output_str += word
            return output_str
        else:
            return str(strs)

    def decode(self, s: str) -> List[str]:
        output_list = s.split("~~~")
        if s != "[]":
            return output_list
        else:
            return []
        
