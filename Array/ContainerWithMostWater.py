class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        bestarea = 0
        while left != right:
            leftht = height[left]
            rightht = height[right]

            newarea = min(leftht, rightht) * (right - left)
            if newarea>bestarea:
                bestarea = newarea

            if leftht >= rightht:
                right -= 1
            else:
                left += 1
        return bestarea