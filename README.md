# Smart Maze Solver

---

## Description

This project implements a **graph-based search agent** designed to solve a maze using various search algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Greedy Best-First Search**. The agent's goal is to find a path from the starting point to the destination within a fixed number of moves. The implementation is modular, allowing for easy modification of sensors, actuators, and environment characteristics.

The maze is represented by a 12x12 grid, where '0' signifies walls and '1' represents open paths. The agent starts at cell (4, 11) and aims to reach cell (10, 0).

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
    python your_main_file.py
    ```

2.  Upon launching, the program will prompt you to **choose a search algorithm**:

    * `1` for Breadth-First Search (BFS)
    * `2` for Depth-First Search (DFS)
    * `3` for Greedy Best-First Search

3.  After your selection, the maze will be displayed in a graphical window, showing the agent traversing the path found by the chosen algorithm. The traversed path and the path cost (number of steps) will be printed to the console.

### Maze and Movement Details

* **Empty blocks** (where the agent can move) are represented by '1'.
* **Filled blocks** (walls) are represented by '0'.
* Movements are prioritized in the following order: **Up**, **Left**, **Right**, and then **Down**.

---

# Labirinto Inteligente

---

## Descrição

Este projeto implementa um **agente de busca baseado em grafos** para resolver um labirinto, utilizando diferentes algoritmos de busca: **Busca em Largura (BFS)**, **Busca em Profundidade (DFS)** e **Greedy Best-First Search**. O objetivo do agente é encontrar o caminho do ponto inicial até o destino em um número fixo de movimentos. A implementação é modular, permitindo fácil alteração de sensores, atuadores e características do ambiente.

O labirinto é representado por uma grade 12x12, onde '0' representa paredes e '1' representa caminhos livres. O agente começa na célula (4, 11) e busca chegar à célula (10, 0).

---

## Instalação

Para executar este projeto, você precisará ter o **Python** e a biblioteca **Pygame** instalados.

1.  **Clone o repositório** (ou faça o download dos arquivos do projeto).
2.  **Instale o Pygame** (se ainda não tiver):

    ```bash
    pip install pygame
    ```

---

## Uso

1.  **Execute o script Python**:

    ```bash
    python labirintos.py
    ```

2.  Ao iniciar, o programa solicitará que você **escolha um algoritmo de busca**:

    * `1` para Busca em Largura (BFS)
    * `2` para Busca em Profundidade (DFS)
    * `3` para Greedy Best-First Search

3.  Após a escolha, o labirinto será exibido em uma janela gráfica, mostrando o agente percorrendo o caminho encontrado pelo algoritmo selecionado. O caminho percorrido e o custo do caminho (número de passos) serão impressos no console.

### Exemplo de Labirinto e Movimentação

* **Blocos vazios** (onde o agente pode se mover) são representados por '1'.
* **Blocos preenchidos** (paredes) são representados por '0'.
* Os movimentos são feitos na seguinte ordem de preferência: **Cima**, **Esquerda**, **Direita** e **Baixo**.

---
