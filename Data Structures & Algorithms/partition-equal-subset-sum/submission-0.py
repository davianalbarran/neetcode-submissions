class Solution:
    # if any subarray of values in the array can add up to half of the total sum 
    # of elements in the array, we know the rest of the elements will get us to
    # the other half and thus can return true
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2 # what is that half target we need to reach?
        
        sums = set() # track sums we compute
        sums.add(0) # we will always have 0 if we choose not to use a value

        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            next_sum_set = set() # we could copy but we have more control of time complexity like this

            for val in sums:
                if (val + nums[i]) == target:
                    return True # if we found our sum, we're good to go
                next_sum_set.add(val + nums[i]) # else add the sum and continue
                next_sum_set.add(val)
            sums = next_sum_set # reset our sums to our new set so we have an updated list for next iter
        
        return False
        
        