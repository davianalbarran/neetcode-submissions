class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_map = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in string_map:
                l = max(string_map[s[r]] + 1, l)
            
            string_map[s[r]] = r
            longest = max(longest, r - l + 1)
        
        return longest