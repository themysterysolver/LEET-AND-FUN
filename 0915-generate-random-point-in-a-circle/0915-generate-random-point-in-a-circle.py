class Solution(object):
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r=radius
        self.x=x_center
        self.y=y_center
    def randPoint(self):
        """
        :rtype: List[float]
        """
        angle=random.uniform(0,2*math.pi)
        r=self.r*math.sqrt(random.uniform(0,1))
        x=r*math.cos(angle)
        y=r*math.sin(angle)
        x,y=x+self.x,y+self.y
        return [x,y]
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()