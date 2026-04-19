class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        letters = defaultdict(int)
        l, r = 0, len(s1)

        for c in s1:
            letters[c] += 1
        
        while r <= len(s2):
            temp_letters = dict(letters)

            subset = s2[l : r]
            count = 0

            for c in subset:
                print(f"c: {c}, c in?: {c in temp_letters}, count: {count}")
                if c not in temp_letters:
                    l += 1
                    r = l + len(s1)
                    break
                count += 1
                temp_letters[c] -= 1
                if temp_letters[c] == 0:
                    del temp_letters[c]
            
            if count == len(s1):
                return True
        
        return False
        