class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)==1:
            return asteroids
        result=[]
        result.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if not result:
                result.append(asteroids[i])
            elif result[-1]>0 and asteroids[i]<0:
                temp1,temp2=abs(result[-1]),abs(asteroids[i])
                if temp1==temp2:
                    result.pop()
                    continue
                elif temp1>temp2:
                    continue
                else:
                    result.pop()
                    result.append(asteroids[i])
                while True:
                    if len(result)<=1:
                        break
                    top,prev=abs(result[-1]),abs(result[-2])
                    if result[-2]>0 and result[-1]<0:
                        if prev>top:
                            result.pop()
                            continue
                        if prev==top:
                            result.pop()
                            result.pop()
                            continue
                        else:
                            temp=result.pop()
                            result.pop()
                            result.append(temp)
                    else:
                        break
            else:
                result.append(asteroids[i])
        return result
                
