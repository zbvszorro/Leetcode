class Solution(object):
    def twoSumBasic(self, nums, target):
        # ----------------------- most fundamental level
        found = False
        p = 0
        container = []
        while not found and p < (len(nums)-1):
            lookfor = target - nums[p]
            t = p + 1
            while t < len(nums):
                if nums[t] == lookfor:
                    container += [p, t]
                    found = True
                    break
                t += 1
            p += 1
        if len(container) ==2:
            return(container)
        else:
            return(None)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_bp = [x for x in nums]
        nums.sort()
        p = 0
        while True:
            lookfor = target - nums[p]
            answer = BS(nums, low=p + 1, high=len(nums) - 1, x=lookfor)
            p += 1
            if None != answer:
                container = [nums[p-1], nums[answer]]
                break
        if container[0] == container[1]:
            outputlist = [i for i, x in enumerate(nums_bp) if x == container[0]]
        else:
            outputlist = [ nums_bp.index(x) for x in container ]
        return outputlist

def BS(alist, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if alist[mid] == x:
            return mid
        # exclude x in the position of alist[mid]
        elif alist[mid] > x:
            return BS(alist, low, mid - 1, x)
        else:
            return BS(alist, mid + 1, high, x)

    else:
        return None
