class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        right = len(nums) - 1

        while low <= right:
            middle = (low + right) // 2

            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                low = middle + 1
            else:
                return middle 
        return -1


        

        