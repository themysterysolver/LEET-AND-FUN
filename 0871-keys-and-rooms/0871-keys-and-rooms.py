class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def BFS():
            visited=[False]*len(rooms)
            q=deque([0])
            visited[0]=True
            while q:
                print('start',list(q))
                l=len(q)
                for i in range(l):
                    r=q.popleft()
                    for room in rooms[r]:
                        if not visited[room]:
                            q.append(room)
                            visited[room]=True
                print('end',list(q))
            print(visited)
            return all(x==True for x in visited)
        return BFS()