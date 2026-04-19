class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = min(1, len(nums))
        checker = min(1, len(nums))
        num_to_check = -999

        for i in sorted(set(nums)):
            print(f"(checker, longest, num_to_check, i): {(checker, longest, num_to_check, i)}")
            if i == num_to_check:
                checker += 1
            else:
                longest = max(checker, longest)
                checker = 1

            num_to_check = i+1
        
        return max(longest, checker)