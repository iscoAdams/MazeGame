from mazekit.maze import Maze
from typing import List, Tuple, Optional
class MazeGenerator:
    @staticmethod
    def generate_some_mazes(num_mazes=20) -> List['Maze']:
        mazes = []
        for i in range(num_mazes):
            maze = Maze.generate_maze()
            mazes.append(maze)
        return mazes 