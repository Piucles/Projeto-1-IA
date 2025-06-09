import pygame
import time
import heapq

# Função para percorrer o grafo usando BFS até um destino
def largura(grafo, start, destino):
    visitados = set()
    fila = [start]
    percurso = []

    while fila:
        atual = fila.pop(0)
        if atual not in visitados:
            visitados.add(atual)
            percurso.append(atual)

            if atual == destino:
                return percurso

            fila.extend(grafo.get(atual, []))

    return percurso

# Função para percorrer o grafo usando DFS até um destino
def profundidade(grafo, start, destino):
    visitados = set()
    pilha = [start]
    percurso = []

    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            percurso.append(atual)

            if atual == destino:
                return percurso

            for vizinho in reversed(grafo.get(atual, [])):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return percurso

# Função para calcular a distância de Manhattan
def manhattan(pos, destino):
    return abs(pos[0] - destino[0]) + abs(pos[1] - destino[1])

# Função de Greedy Best-First Search
def percorrer_greedy_best_first_search(grafo, start, destino):
    visitados = set()
    fila = []
    heapq.heappush(fila, (manhattan(start, destino), start))
    percurso = []

    while fila:
        _, atual = heapq.heappop(fila)

        if atual not in visitados:
            visitados.add(atual)
            percurso.append(atual)

            if atual == destino:
                return percurso

            for vizinho in grafo.get(atual, []):
                if vizinho not in visitados:
                    heapq.heappush(fila, (manhattan(vizinho, destino), vizinho))

    return percurso

# Função para desenhar o labirinto e o caminho com Pygame
def desenhar_labirinto_com_caminho(matriz, caminho, fim, largura=40, altura=40):
    pygame.init()
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Configuração da tela
    screen = pygame.display.set_mode((colunas * largura, linhas * altura))
    pygame.display.set_caption("Labirintos")

    # Cores
    COR_PAREDE = (0, 0, 0)
    COR_CAMINHO = (255, 255, 255)
    COR_CELULA_VISITADA = (0, 255, 0)
    COR_DESTINO = (255, 0, 0)
    COR_INICIO = (0, 0, 255)

    # Função para desenhar célula
    def desenhar_celula(x, y, cor):
        pygame.draw.rect(screen, cor, (y * largura, x * altura, largura, altura))
        pygame.draw.rect(screen, (0, 0, 0), (y * largura, x * altura, largura, altura), 2)

    # Desenha o labirinto
    for x in range(linhas):
        for y in range(colunas):
            cor = COR_PAREDE if matriz[x][y] == 0 else COR_CAMINHO
            desenhar_celula(x, y, cor)

    # Desenha o caminho percorrido
    for index, (x, y) in enumerate(caminho):
        if index == 0:
            desenhar_celula(x, y, COR_INICIO)
        elif (x, y) == fim:
            desenhar_celula(x, y, COR_DESTINO)
        else:
            desenhar_celula(x, y, COR_CELULA_VISITADA)
        pygame.display.update()
        time.sleep(0.2)

    # Mantém a janela aberta até o usuário fechar
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Função para converter uma matriz em um grafo
def matriz_para_grafo(matriz):
    grafo = {}
    linhas = len(matriz)
    colunas = len(matriz[0])

    def posicao_valida(x, y):
        return 0 <= x < linhas and 0 <= y < colunas and matriz[x][y] == 1

    for x in range(linhas):
        for y in range(colunas):
            if matriz[x][y] == 1:
                vizinhos = []
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if posicao_valida(nx, ny):
                        vizinhos.append((nx, ny))
                grafo[(x, y)] = vizinhos

    return grafo

# Matriz representando o labirinto
matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Converte matriz para grafo
grafo = matriz_para_grafo(matriz)

# Coordenadas inicial e final
start = (4, 11)
destino = (10, 0)

# Executa o algoritmo selecionado
print("Escolha o algoritmo:")
print("1 - Largura (Breadth-First Search)")
print("2 - Profundidade (Depth-First Search)")
print("3 - Greedy Best-First Search")

escolha = int(input("Digite sua escolha (1, 2 ou 3): "))

if escolha == 1:
    caminho = largura(grafo, start, destino)
    algoritmo = "BFS"
elif escolha == 2:
    caminho = profundidade(grafo, start, destino)
    algoritmo = "DFS"
elif escolha == 3:
    caminho = percorrer_greedy_best_first_search(grafo, start, destino)
    algoritmo = "Greedy Best-First Search"
else:
    print("Escolha inválida!")
    exit()

# Imprime o caminho e o custo
print(f"Algoritmo usado: {algoritmo}")
print("Caminho percorrido:", caminho)
print(f"Custo do caminho: {len(caminho) - 1}")

# Desenha o labirinto com o caminho
desenhar_labirinto_com_caminho(matriz, caminho, destino)
