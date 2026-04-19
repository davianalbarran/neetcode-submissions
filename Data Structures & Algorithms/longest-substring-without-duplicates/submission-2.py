class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 1
        string_set = { s[l] }
        longest, temp = 1, 1

        while r < len(s):
            # print(f"l: {l}, r: {r}, s[l]: {s[l]}, s[r]: {s[r]}, longest: {longest}")
            if s[r] in string_set:
                longest = max(longest, temp)
                temp = 1
                l += 1
                r = l + 1
                string_set = { s[l] }
            else:
                temp += 1
                string_set.add(s[r])
                r += 1
        
        return max(longest, temp)
        