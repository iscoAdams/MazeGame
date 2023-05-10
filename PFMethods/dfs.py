from mazekit.mazeutil import MazeUtil
from PFMethods.utils import get_path

def dfs(maze, start=None, goal=None):
    start = start or maze.props.start
    goal = goal or maze.props.goal
    predecessors = {start: None}   # dictionary that maps each node to its source node
    vis = set()  # set of visited nodes

    def isReachable(node=start) -> bool:
        #base cases
        if node in vis or not MazeUtil.is_valid_pos(maze, node):
            return False
        if node == goal:
            return True # if so, will return that path later.
        
    # recursive case
        vis.add(node)
        for direction in MazeUtil.directions:
            adj = node[0] + direction[0], node[1] + direction[1]
            if isReachable(adj):
                predecessors[adj] = node
                return True
        return False
    
    return  get_path(predecessors, start, goal) if isReachable(start) else None 





# if '__main__':
#     write_file = open("out.txt", "w")

#     maze = readMaze("../mazes/customMaze.txt")
#     start = (0, 0)
#     goal = (2, 2)
#     print("Start:", start, "Goal:", goal, sep=" ", end="\n", file=write_file)
#     for row in maze:
#         print(*row, sep="", end="\n", file=write_file)
#     path = dfs(maze, start, goal)
#     assert path is not None
#     print("Path:", path, sep=" ", end="\n", file=write_file)
#     write_file.close()

    # stack = Stack() #UnboundLocalError if they have the same name
    # stack.push(start)
    # visited = set()  # set of visited nodes but i will use a dictionary to keep track of the visited nodes instead
    # predecessors = { start : None }  # dictionary of predecessors with none predecessor for the start node
   
    # while not stack.isEmpty():
    #     current_cell = stack.pop()
    #     if current_cell == goal:
    #         return get_path(predecessors, start, goal)
    #     for direction in ["up", "right", "down", "left"]:
    #     #we push clockwise
    #     #    neighbor = get_neighbors(current_cell[0], current_cell[1]) 
    #        neighbor = current_cell[0] + offset[direction][0], current_cell[1] + offset[direction][1]
    #        if is_right_pos(maze,neighbor) and neighbor not in predecessors:
    #            stack.push(neighbor)
    #            predecessors[neighbor] = current_cell
    # return None



# if not '__main__':
#     pass
# else:
#     maze = readMaze("miniMaze2.txt")
#     start = (0, 0)
#     goal = (len(maze) - 1, len(maze[0]) - 1)

#     write_file = open("out.txt", "w") #open the file to write
#     for line in maze:
#         print(*line, sep="", end="\n",file=write_file)

#     print("------------------------------------------------------",file=write_file)
#     path = dfs(maze, start, goal)
#     assert path is not None
#     print("Path:", path, sep="", end="\n",file=write_file)               




# # def get_neighbors(x, y):
# #     neighbors = []
# #     for direction, (dx, dy) in offset.items():
# #         new_x = x + dx
# #         new_y = y + dy
# #         if is_right_position(new_x, new_y):
# #             neighbors.append((new_x, new_y, direction))
# #     return neighbors


# """
# (0,1),(1,1),


# pop : (3,3)
# predecessors : 
# (0,0) : None
# (1,1):(1,0)
# (2,0):(1,0)
# (3,0):,(2,0)
# (3,1):(3,0)
# (3,2):(3,1)
# (3,3):(3,2)


# (3,3),(3,2),(3,1),(3,0),(2,0),(1,0),(0,0)

# """

# """
# depth first search
# we pop from the stack and if it's not the goal we push the neighbors to the stack
# and we add the current cell to the predecessors dictionary
# and then we check if the current cell is the goal
# if it is we return the path
# if it's not we continue
# and the result is the items of the predecessors dictionary
# and we only push to the dictionary the cells that are not visited yet (the key and the value both exists in the same item)
# the path is the list of cells from the goal to the start and before None
# """

