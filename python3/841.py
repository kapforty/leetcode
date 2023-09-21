class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        frontier, visited = [0], set()

        while frontier:
            key = frontier.pop()
            for room in rooms[key]:
                if room not in visited:
                    frontier.append(room)
            visited.add(key)
        
        return len(rooms) == len(visited)
