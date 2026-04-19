class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = set(s)
        longest = 0

        for c in unique:
            count = l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                longest = max(longest, r - l + 1)

        return longest
        