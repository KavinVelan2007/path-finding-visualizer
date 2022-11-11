def return_neighbours(grid):
    neighbours = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours[(i,j)] = []
            try:
                if grid[i-1][j] and grid[i-1][j] != '#' and i-1 >= 0:
                    neighbours[(i,j)].append((i-1,j))
            except:
                None

            try:
                if grid[i+1][j] and grid[i+1][j] != '#':
                    neighbours[(i,j)].append((i+1,j))
            except:
                None

            try:
                if grid[i][j-1] and grid[i][j-1] != '#' and j-1 >= 0: #LEFT
                    neighbours[(i,j)].append((i,j-1))
            except:
                None

            try:
                if grid[i][j+1] and grid[i][j+1] != '#': #RIGHT
                    neighbours[(i,j)].append((i,j+1))
            except:
                None
    return neighbours
