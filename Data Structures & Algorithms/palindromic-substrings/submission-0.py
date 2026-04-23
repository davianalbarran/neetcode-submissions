class Solution:
    def countSubstrings(self, s: str) -> int:
        # again, brute force is bad for this.
        # let's reuse our longest palindromic substr answer with some mods below

        count = 0 # we don't need to store the longest anymore
        for i in range(len(s)):
            # odd length strings
            l, r = i, i # both start in the same place

            # while the word is a palindrome essentially
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1 # count all palindromes
            
            # even length strings
            l, r = i, i + 1 # need to be offset to grab the neighboring char

            # while the word is a palindrome again
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1 # count all palindromes
        
        return count
    
        