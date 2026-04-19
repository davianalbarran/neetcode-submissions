class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = list()
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1

            while l < r:
                l_val = nums[l]
                r_val = nums[r]

                check_sum = a + l_val + r_val

                if check_sum == 0:
                    triplets.append([a, l_val, r_val])
                    l += 1
                    r -= 1
                    while l_val == nums[l] and l < r:
                        l += 1
                elif check_sum > 0:
                    r -= 1
                elif check_sum < 0:
                    l += 1
        
        return triplets