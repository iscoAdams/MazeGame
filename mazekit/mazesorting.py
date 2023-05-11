from mazekit.maze import Maze
from mazekit.props import Props
from typing import List
import random

def compare(maze1:Maze, maze2:Maze) -> bool: #  true if harder which is the latter elements in the array
    return Props.is_harder_than(maze1.props, maze2.props)

# sort the mazes based on the number of invalid positions (invalid_count)
def sort_logic(mazes:List['Maze']) -> List['Maze']:
    random.shuffle(mazes) #O(n)
    def quick_sort(array) : #O(nlogn)
        if len(array) <= 1:
            return array
        pivot = array[random.randint(0, len(array)-1)]
        pivot, array[-1] = array[-1], pivot #shift to the end of the list
        left = [maze for maze in array[:-1] if not compare(maze, pivot)]
        right = [maze for maze in array[:-1] if compare(maze, pivot)]
        return quick_sort(left) + [pivot] + quick_sort(right)
    return quick_sort(mazes)