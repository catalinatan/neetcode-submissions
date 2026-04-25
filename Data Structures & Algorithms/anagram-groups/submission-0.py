class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = {}
        for idx in range (len(strs)):
            sorted_dict[idx] = sorted(strs[idx])

        output_list = []
        for value in sorted_dict.values():
            output_list.append([strs[key] for key, val in sorted_dict.items() if val == value])

        output_set = {tuple(sublist) for sublist in output_list}
        output_list_unique = [list(t) for t in output_set]
        return output_list_unique
                