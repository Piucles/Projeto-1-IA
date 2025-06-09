# Smart Maze Solver

This project implements a **graph-based search agent** designed to solve a maze using various search algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Greedy Best-First Search**. The agent's goal is to find a path from the starting point to the destination within a fixed number of moves. The implementation is modular, allowing for easy modification of sensors, actuators, and environment characteristics.

The maze is represented by a 12x12 grid, where '0' signifies walls and '1' represents open paths. The agent starts at cell (4, 11) and aims to reach cell (10, 0).

---

## Table of Contents

* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Maze and Movement Details](#maze-and-movement-details)
* [Contribution](#contribution)
* [License](#license)
* [Contact](#contact)

---

## Installation

To run this project, you'll need **Python** and the **Pygame** library installed.

1.  **Clone the repository** (or download the project files).
2.  **Install Pygame** (if you haven't already):

    ```bash
    pip install pygame
    ```

---

## Usage

1.  **Execute the Python script**:

    ```bash
    python labirintos.py
    ```

2.  Upon launching, the program will prompt you to **choose a search algorithm**:

    * `1` for Breadth-First Search (BFS)
    * `2` for Depth-First Search (DFS)
    * `3` for Greedy Best-First Search

3.  After your selection, the maze will be displayed in a graphical window, showing the agent traversing the path found by the chosen algorithm. The traversed path and the path cost (number of steps) will be printed to the console.

---

## Maze and Movement Details

* **Empty blocks** (where the agent can move) are represented by '1'.
* **Filled blocks** (walls) are represented by '0'.
* Movements are prioritized in the following order: **Up**, **Left**, **Right**, and then **Down**.

---
