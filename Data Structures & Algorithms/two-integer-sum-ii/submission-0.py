class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexOne = 0
        indexTwo = 0

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    indexOne = i + 1
                    indexTwo = j + 1
        
        return [indexOne, indexTwo]
            
