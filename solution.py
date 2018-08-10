class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        SIZE = len(grid)
        maxArea = 0
        c = 1
        board = [[0 for x in range(SIZE)] for y in range(SIZE)]
        collision = []
        area = [0 for x in range(SIZE ** 2 + 1)]
        map = dict()

        for i in range(SIZE):
            for j in range(SIZE):
                if grid[i][j] == 0:
                    continue

                if i == 0:
                    if j == 0:
                        board[i][j] = c
                        c += 1
                    else:
                        if board[i][j - 1] > 0:
                            board[i][j] = board[i][j - 1]
                        else:
                            board[i][j] = c
                            c += 1
                else:
                    if j == 0:
                        if board[i - 1][j] > 0:
                            board[i][j] = board[i - 1][j]
                        else:
                            board[i][j] = c
                            c += 1
                    else:
                        if board[i - 1][j] > 0 and board[i][j - 1] > 0 and board[i - 1][j] != board[i][j - 1]:
                            collision.append((board[i - 1][j] , board[i][j - 1]))

                        if board[i - 1][j] > 0:
                            board[i][j] = board[i - 1][j]

                        if board[i][j - 1] > 0:
                            board[i][j] = board[i][j - 1]

                        if board[i][j] == 0:
                            board[i][j] = c
                            c += 1

        #print(collision)
        while len(collision) > 0:
            (c1, c2) = collision.pop()
            if c1 not in map and c2 not in map:
                map[c1] = c2
                map[c2] = c2
            else:
                if c1 in map and c2 in map:
                    if map[c1] != map[c2]:
                        for key, value in map.items():
                            if key != c2 and value == map[c2]:
                                map[key] = map[c1]
                        map[c2] = map[c1]

                else:
                    if c1 not in map:
                        map[c1] = map[c2]
                    if c2 not in map:
                        map[c2] = map[c1]

        #print(map)
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] in map:
                    board[i][j] = map[board[i][j]]
                area[board[i][j]] += 1

            #print(board[i])

        area[0] = 0
        maxArea = max(area)

        for i in range(SIZE):
            for j in range(SIZE):
                if grid[i][j] == 1:
                    continue
                sum = 1
                x = 0
                added = []

                if i > 0:
                    x = board[i - 1][j]
                    if x > 0 and x not in added:
                        sum += area[x]
                        added.append(x)

                if i < SIZE - 1:
                    x = board[i + 1][j]
                    if x > 0 and x not in added:
                        sum += area[x]
                        added.append(x)

                if j > 0:
                    x = board[i][j - 1]
                    if x > 0 and x not in added:
                        sum += area[x]
                        added.append(x)

                if j < SIZE - 1:
                    x = board[i][j + 1]
                    if x > 0 and x not in added:
                        sum += area[x]
                        added.append(x)

                if sum > maxArea:
                    maxArea = sum

        return maxArea