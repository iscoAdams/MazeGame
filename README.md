# Maze Engine

The Maze Game is a Python-based engine that allows users to interact with mazes. It provides functionality to input custom mazes, generate mazes of varying difficulties, and solve them using different pathfinding algorithms.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iscoAdams/maze-game.git
   ```

2. Navigate to the project directory:

## Usage

there are two options to interact with the engine:

- place the maze to maze.txt
- let the engine generate a maze for u on the fly

in my case, I used the second option, and there is an output sample inside out.txt

## project structure

maze-game/
├─mazekit/
├── get_maze.py
├── maze.py
├── mazegenerator.py
├── mazesorting.py
├── mazeutil.txt
├── props.py
├─PFMethods/
├── bfs.py
├── dfs.py
├── utils.py
├─index.py
├─maze.txt
├─out.txt
├─README.md

## Notes

- the output is in out.txt file
- the engine is not fully completed yet, so there are some bugs and issues that need to be fixed.
- it only supports walls as invalid positions
- there is no UI yet, so the engine is only used through the terminal
