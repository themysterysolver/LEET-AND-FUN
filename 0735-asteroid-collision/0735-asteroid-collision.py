class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            while stack and a<0<stack[-1]:
                if -a>stack[-1]:
                    stack.pop()
                    continue
                elif stack[-1]==-a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack