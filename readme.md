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
