import sys
import os
from mazekit.maze import Maze
from mazekit.mazeutil import MazeUtil
from mazekit.props import Props
from mazekit.mazegenerator import MazeGenerator
from mazekit.mazesorting import sort_logic
from mazekit.getmaze import get_maze, Option
from PFMethods.bfs import bfs
from PFMethods.dfs import dfs
sys.stdout = open('out.txt', 'w')

if '__main__':
    maze = get_maze(Option.easy)
    print("initial maze:")
    maze.print_grid()
    print("start", maze.props.start, "goal", maze.props.goal, sep=" ", end="\n")
    print('\n\n')
    
    dfs_path = dfs(maze)
    assert dfs_path is not None
    print("dfsPath:", dfs_path, sep=" ", end="\n\n")
    MazeUtil.print_solved_maze(maze, dfs_path)
    print('\n\n')

    bfs_path = bfs(maze)
    assert bfs_path is not None
    print("bfsPath:", bfs_path, sep=" ", end="\n\n")
    MazeUtil.print_solved_maze(maze, bfs_path)
