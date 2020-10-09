class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        alist = [x for x in height]
        alist.sort()
        indexlist = list(range(len(alist)))
        bestpool = 0

        for i in range(len(alist)-1):
            level = alist[i]
            cur_position = height.index(level)
            newpool = level * max(indexlist[cur_position] - indexlist[0],
                                  indexlist[-1] - indexlist[cur_position]
                                  )
            # print( 'i = ' + str(i) + '--- best = ' + str(bestpool) + '--- newpool = ' + str(newpool))
            # print('position = ' + str(cur_position))
            # print(indexlist)
            if newpool > bestpool:
                bestpool = newpool

            #  dequeue the current position
            height  = height[:cur_position] + height[(cur_position+1):]
            # dequeue the postion from index list
            indexlist = indexlist[:cur_position] + indexlist[(cur_position+1):]
        return bestpool