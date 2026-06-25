# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        # visit from "O" connect to border
        # if a node can be visited, means not be surrounded
        visited = set()
        queue = deque()
        # add "O" connect to border
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or
                    r == rows - 1 or 
                    c == cols - 1) and (board[r][c] == "O"):
                    queue.append((r, c))
        #print(queue)
        # start spreading
        while queue:
            cr, cc = queue.popleft()
            visited.add((cr, cc))
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (nc < 0 or nr < 0 or 
                    nr >= rows or nc >= cols or
                    (nr, nc) in visited or
                    board[nr][nc] == "X"):
                    continue
                # if can be visited, add into set
                visited.add((nr, nc))
                queue.append((nr, nc))
        # print(visited)

        # traverse matrix, if not in visted, means be surrounded.
        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited) and (board[r][c] == "O"):
                    board[r][c] = "X"

        