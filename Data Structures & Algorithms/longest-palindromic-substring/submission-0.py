class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force is O(n^3)... yikes!
        # good hint that it's a dp problem, especially with the constraints
        # of problem
        # we can make this O(n^2) by doing a middle-out technique, queue Silicon Valley

        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd length strings
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
            
            # even length strings
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
        
        return res