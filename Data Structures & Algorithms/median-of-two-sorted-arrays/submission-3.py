class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_array, second_array = nums1, nums2
        total = len(first_array) + len(second_array)
        half = total // 2

        if len(first_array) > len(second_array):
            first_array, second_array = second_array, first_array

        l, r = 0, len(first_array) - 1

        while True:
            first_idx = (l + r) // 2
            second_idx = half - first_idx - 2

            left_part_first = first_array[first_idx] if first_idx >= 0 else float("-infinity")
            right_part_first = first_array[first_idx + 1] if (first_idx + 1) < len(first_array) else float("infinity")
            left_part_second = second_array[second_idx] if second_idx >= 0 else float("-infinity")
            right_part_second = second_array[second_idx + 1] if (second_idx + 1) < len(second_array) else float("infinity")

            if left_part_first <= right_part_second and left_part_second <= right_part_first:
                if total % 2:
                    return min(right_part_first, right_part_second)
                else:
                    return (max(left_part_first, left_part_second) + min(right_part_first, right_part_second)) / 2
            elif left_part_first > right_part_second:
                r = first_idx - 1
            else:
                l = first_idx + 1