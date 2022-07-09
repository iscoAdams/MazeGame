maze = []
def readMaze(filename):
    try:
        with open(filename) as f:
            for line in f:
                maze.append(list(line.strip("\n")))
                # maze = [[char for char in line.strip("\n")] for line in f]
            num_cols = len(maze[0])
            for row in maze:
                if len(row) != num_cols:
                    #    raise ValueError("Maze is malformed")
                       print("Maze is malformed")
                       raise SystemExit(1)
        return maze
    except OSError as e:
        print("OS error: {0}".format(e))
        raise SystemExit(1) 

offset = { #dictionary for relative position of the neighbors
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

#grid here is'nt cartesian, it's a matrix 
#there is a problem with that function so i'm using the right_pos function
# is_right_position = lambda x, y: x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] != "#" and maze[x][y] != "-" and maze[x][y] != "|" and maze[x][y] != "+" and maze[x][y] != "*"

def is_right_pos(maze,pos):
    x,y = pos
    return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] != "*"

def get_path(predecessors,start,goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current] #every element has a predecessor with the previous position
    path.append(start)
    path.reverse() #reverse the path
    return path 



#sugested by copilot
# def get_path(x, y):
#     path = []
#     while maze[x][y] != "S":
#         path.append(maze[x][y])
#         x, y = x + offset[maze[x][y]][0], y + offset[maze[x][y]][1]
#     return path[::-1]

#sugested by copilot
# def get_neighbors(x, y):
#     neighbors = []
#     for direction, (dx, dy) in offset.items():
#         new_x = x + dx
#         new_y = y + dy
#         if is_right_position(new_x, new_y):
#             neighbors.append((new_x, new_y, direction))
#     return neighbors

#suggested by copilot
# def get_full_path(x, y):
#     path = []
#     while True:
#         path.append((x, y))
#         if maze[x][y] == "*":
#             break
#         for direction in offset:
#             new_x = x + offset[direction][0]
#             new_y = y + offset[direction][1]
#             if is_right_position(new_x, new_y):
#                 x = new_x
#                 y = new_y
#                 break
#     return path

