import random
from mazekit.maze import Maze
from mazekit.mazegenerator import MazeGenerator
from mazekit.mazesorting import sort_logic
from enum import Enum

class Option(Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

def get_maze(option:Option) -> Maze:
    mazes = MazeGenerator.generate_some_mazes(20)
    sorted_mazes = sort_logic(mazes)
    index = 0
    if option == "easy":
        index = random.randint(0, len(sorted_mazes)//2)
    elif option == "medium":
        index = random.randint(len(sorted_mazes)//2, len(sorted_mazes)//2+1)
    elif option == "hard":
        index = random.randint(len(sorted_mazes)//2+1, len(sorted_mazes)-2)
    return sorted_mazes[index]