def return_neighbours(grid,diagonal):
    neighbours = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours[(i,j)] = []
            try:
                if grid[i-1][j] and grid[i-1][j] != '#' and i-1 >= 0: #UP
                    neighbours[(i,j)].append([i-1,j])
            except:
                None

            try:
                if grid[i+1][j] and grid[i+1][j] != '#': #DOWN
                    neighbours[(i,j)].append([i+1,j])
            except:
                None

            try:
                if grid[i][j-1] and grid[i][j-1] != '#' and j-1 >= 0: #LEFT
                    neighbours[(i,j)].append([i,j-1])
            except:
                None

            try:
                if grid[i][j+1] and grid[i][j+1] != '#': #RIGHT
                    neighbours[(i,j)].append([i,j+1])
            except:
                None

            if diagonal:
                try:
                    if grid[i-1][j-1] and grid[i-1][j-1] != '#' and i-1 >= 0 and j-1 >= 0:
                        neighbours[(i,j)].append([i-1,j-1])
                except:
                    None

                try:
                    if grid[i-1][j+1] and grid[i-1][j+1] != '#' and i-1 >= 0:
                        neighbours[(i,j)].append([i-1,j+1])
                except:
                    None

                try:
                    if grid[i+1][j-1] and grid[i+1][j-1] != '#' and j-1 >= 0:
                        neighbours[(i,j)].append([i+1,j-1])
                except:
                    None

                try:
                    if grid[i+1][j+1] and grid[i+1][j+1] != '#':
                        neighbours[(i,j)].append([i+1,j+1])
                except:
                    None

    return neighbours

def bfs(neighbours,start,end):
    visited = []
    queue = [start]
    predecessorNodes = {}
    while queue:
        node = queue.pop(0)
        for neighbour in neighbours[tuple(node)]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                predecessorNodes[tuple(neighbour)] = node

    path = []
    currentNode = end
    while currentNode != start:
        try:
            currentNode = predecessorNodes[tuple(currentNode)]
            path.append(currentNode)
        except KeyError:
            messagebox.showerror('Error','No path found :(')
            return False

    return path

def reconstruct_path(grid,path):
    for i,j in path:
        if grid[i][j] != 'S':
            grid[i][j] = '*'
