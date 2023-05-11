import random
from mazekit.maze import Maze
from mazekit.mazegenerator import MazeGenerator
from mazekit.mazesorting import sort_logic
from enum import Enum

class Option(Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

def get_maze(option:Option) -> 'Maze':
    mazes = MazeGenerator.generate_some_mazes(20)
    sorted_mazes = sort_logic(mazes)
    index = 0
    sz = len(sorted_mazes)
    if option == "easy":
        index = random.randint(0, sz//2)
    elif option == "medium":
        index = random.randint(sz//2, sz//2+1)
    elif option == "hard":
        index = random.randint(sz//2+1, sz-2)
    return sorted_mazes[index]