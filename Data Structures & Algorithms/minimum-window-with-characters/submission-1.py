class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_letters = defaultdict(int)
        have_letters = defaultdict(int)

        for c in t:
            need_letters[c] += 1
        
        have, need = 0, len(need_letters)
        res, resLen = (-1, -1), float("infinity")
        l = 0

        for r in range(len(s)):
            current_char = s[r]
            have_letters[current_char] += 1

            if current_char in need_letters and have_letters[current_char] == need_letters[current_char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = (l, r)
                    resLen = (r - l + 1)

                have_letters[s[l]] -= 1

                if s[l] in need_letters and have_letters[s[l]] < need_letters[s[l]]:
                    have -= 1

                l += 1
        
        (l, r) = res
        return s[l:r+1] if resLen != float("infinity") else ""

