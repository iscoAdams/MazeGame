from mazekit.maze import Maze
from mazekit.props import Props
from typing import List
import random

def is_harder(maze1:Maze, maze2:Maze) -> bool: # delegation
    return Props.compare(maze1.props, maze2.props)

def quick_sort(array) : #O(nlogn) but worst-case is O(n^2)
        if len(array) <= 1:
            return array
        pivot = array[random.randint(0, len(array)-1)]
        pivot, array[-1] = array[-1], pivot #shift to the end of the list not to choose it again.
        left = [element for element in array[:-1] if not is_harder(element, pivot)]
        right = [element for element in array[:-1] if is_harder(element, pivot)]
        return quick_sort(left) + [pivot] + quick_sort(right)

# sort the mazes based on the number of invalid positions (invalid_count)
def sort_maze(mazes:List['Maze']) -> List['Maze']: 
    random.shuffle(mazes) #O(n)
    return quick_sort(mazes) #O(nlog(n))
