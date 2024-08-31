class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance(p,q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2
        d=[distance(p1,p2),distance(p1,p3),distance(p1,p4),distance(p2,p3),distance(p2,p4),distance(p3,p4)]
        print d
        d.sort()
        print d
        if d[0]==d[1] and d[1]==d[2] and d[2]==d[3] and d[4]==d[5] and d[4]>d[3]:
            return True
        else:
            return False
        

        
        