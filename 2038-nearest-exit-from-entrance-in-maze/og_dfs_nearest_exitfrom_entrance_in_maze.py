#this has print statments that help you debug and understand how queue works+BFS works!
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def BFS(r,c):
            queue=deque([(r,c)])
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            row,col=len(maze),len(maze[0])
            visited=[[False]*col for _ in range(row)]
            count=0
            while queue:
                l=len(queue)
                print('outter:',list(queue))
                for i in range(l):
                    print('innner q that is manupulated!:',list(queue))
                    x,y=queue.popleft()
                    print('innner q that is manupulated after pop!:',list(queue))
                    for dx,dy in directions:
                        nx,ny=dx+x,dy+y
                        if nx<0 or ny<0 or nx>=row or ny>=col:
                            if x==r and y==c:
                                continue
                            else:
                                return count
                        elif not visited[nx][ny] and maze[nx][ny]!='+':
                            visited[nx][ny]=True
                            queue.append((nx,ny))
                        print('active queue',list(queue),dx,dy)
                count+=1
                print('-----------BFS-----------',count)
            return -1
        for row in maze:
            print(row)
        ans=BFS(entrance[0],entrance[1])
        return ans
        
