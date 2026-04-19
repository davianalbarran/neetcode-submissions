class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = ""
        
        for c in s:
            if c.isalnum():
                formattedString += c.lower()
        
        return ''.join(reversed(formattedString)) == formattedString
