"""
bridth first search
what does weighted edged and un weighted edged 
bfs give the shortest path if there is no weight on the edges (no edge weightes are used)
and here in the maze every signal cell is a weight of 1
every single cell is connected by an edge of weight 1
there is no edge weightes other than the signal cell (1)
as it at first find all the vertices that are one edge away from the start
then all the vertices that are two edges away from the start and so on
and when it find the specific vertex it will stop (it is the goal vertix)
and that path i traced is the shortest path and if there is a shorter path then bfs algorithm already found it
used in GPS navigation
it's the same idea as dfs but with queue instead of stack
it move eqidistant from the start node
"""

from util import *
from DS.QueueList import Queue
def bfs(maze,start,goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start : None}
    while not queue.isEmpty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors,start,goal)
        for direction in ["up","right","down","left"]:
            neighbour = current_cell[0] + offset[direction][0], current_cell[1] + offset[direction][1]
            if is_right_pos(maze,neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None


if not '__main__':
    pass
else:
    write_file = open("out.txt", "w") #open the file to write
    # #test 1
    # maze = readMaze("miniMaze.txt")
    # start = (0, 0)
    # goal =(2,2)
    # for line in maze:
    #     print(*line, sep="", end="\n",file=write_file)
    # path = bfs(maze, start, goal)
    # assert path is not None
    # print("------------------------------------------------------",file=write_file)
    # print("Path:", path, sep="", end="\n",file=write_file)

    #test 2
    maze = [[0] * 3 for row in range(3)]
    start = (0, 0)
    goal = (2, 2)
    for line in maze:
        print(*line, sep="", end="\n",file=write_file)
    path=bfs(maze,start,goal)
    assert path is not None
    print("------------------------------------------------------",file=write_file)
    print("Path:", path, sep="", end="\n",file=write_file)
    write_file.close()


"""

pop :(3,3)
predecessors:
(0,0):None
(0,1):(0,0)
(1,0):(0,0)>>exception
(1,1):(0,1)
(2,0):(1,0)>>exception
(1,2):(1,1)
(3,0):(2,0)>>exception
(1,3):(1,2)>>exception
(2,2):(1,2)
(0,3):(1,3)>>exception
(3,2):(2,2)
(3,3):(3,2)
(3,3),(3,2),(2,2),*(1,3),(1,2),*(2,0),(1,1),*(1,0),(0,1),(0,0)
note here we only take the predecesors that we got from the previous one or 
the one that has a previous one in the predecessors dictionary
(2,2) came from (1,2) and (1,2) came from (1,1) and (1,1) came from (0,1) and so on
on the other hand dfs always give the one before it as i pop from the end 
so i just need to take the items of the keys of the predecessors dictionary
and i don't need to specifiy from which cell the predecessor came from
"""