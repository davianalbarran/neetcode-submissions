class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for i in range(len(strs)):
            compare = strs[i]
            compare_sorted = ''.join(sorted(compare))

            if compare_sorted in str_map:
                str_map[compare_sorted].append(compare)
            else:
                str_map[compare_sorted] = [compare]
        
        return [v for _, v in str_map.items()]
