class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # main idea - two-pointer by sorted array
        nums.sort()

        # set the container
        solutions = set()

        # edge case test; leave the problem of finding unique pair to set
        unique_set = set(nums)
        if len(unique_set) == 1 and 0 in nums and len(nums)>=3:
            return([[0,0,0]])

        # loop thru
        i = 0
        n = len(nums)
        while i < (len(nums)-1):
            left = i+1
            right= n-1

            while left < right:
                pair = (nums[i], nums[left], nums[right])
                checksum = sum(pair)

                if checksum == 0:
                    if pair not in solutions:
                        solutions.add(pair)
                    left += 1
                    right -= 1

                if checksum > 0:
                    right -= 1

                if checksum < 0:
                    left += 1

            i += 1
        return(solutions)

