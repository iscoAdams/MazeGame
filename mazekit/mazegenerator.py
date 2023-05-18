from mazekit.maze import Maze
from typing import List, Tuple, Optional
class MazeGenerator:
    @staticmethod
    def generate_some_mazes(num_mazes=20) -> List['Maze']: 
        #O(sz*n*m) or O(n^3), where sz -> num of mazes to generate, and (n,m) -> size of the grid generated.
        mazes = []
        for i in range(num_mazes):
            maze = Maze.generate_maze()
            mazes.append(maze)
        return mazes 