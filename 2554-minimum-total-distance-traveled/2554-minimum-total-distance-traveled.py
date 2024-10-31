from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        memo = {}

        def helper(currRobot, currFact, usedCapacity):
            if currRobot == len(robot):
                return 0
            if currFact == len(factory):
                return float('inf')

            key = (currRobot, currFact, usedCapacity)
            if key in memo:
                return memo[key]

            minDist = helper(currRobot, currFact + 1, 0)

            position, capacity = factory[currFact]
            if usedCapacity < capacity:
                dist = abs(robot[currRobot] - position)
                minDist = min(minDist, dist + helper(currRobot + 1, currFact, usedCapacity + 1))

            memo[key] = minDist
            return minDist
        return helper(0, 0, 0)