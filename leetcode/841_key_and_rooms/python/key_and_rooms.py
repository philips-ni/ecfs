
class Solution1(object):
    def canVisitAllRooms(self, rooms):
        def dfs(roomIdx, visited):
            if roomIdx in visited:
                return
            visited.append(roomIdx)
            connected_rooms = rooms[roomIdx]
            for r in connected_rooms:
                dfs(r, visited)
        visited = []
        dfs(0, visited)
        return len(visited) == len(rooms)
            
class Solution:
    def canVisitAllRooms(self, M):
        if len(M) == 1:
            return True
        checked = set()
        stack = [0]
        while stack != []:
            i = stack.pop()
            checked.add(i)
            for j in M[i]:
                if j not in checked:
                    stack.append(j)
        if len(checked) == len(M):
            return True
        else:
            return False
