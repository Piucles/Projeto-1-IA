''' Considere que você tem um labirinto que precisa ser resolvido. O objetivo de um agente é completar o labirinto em um número fixo de movimentos. Sua implementação deve ser modular, de modo que sensores, atuadores e características do ambiente(como o tamanho, por exemplo)possam ser facilmente alterados. Você deve implementar um agente de busca baseado em grafos com verificação de estados visitados.
 Para formular este problema, defina os quatro parâmetros a seguir:
 1. Estado Inicial
 2. Sucessor
 3. Teste de Objetivo
 4. Custo do Caminho 

 Os movimentos só podem ser realizados para blocos vazios, representados por 1, enquanto blocos preenchidos podem ser considerados como 0.

A sequência de movimentos deve ser a ordem: Cima, Esquerda, Direita e Baixo 

Ações disponíveis: Cima, Esquerda, Direita e Baixo

Critério de término: O labirinto é concluído pelo agente 

O labirinto deve ser resolvido usando os algoritmos de Busca em Largura

O ambiente anuncia quando esse critério é alcançado e interrompe a execução

O agente conhece o tamanho do labirinto (uma grade 12x12), o conteúdo da célula em que está e a localização da célula (coordenadas)

o agente dever ser posicionado inicialmente na célula (5,12), conforme descrito na grade do labirinto.

O desempenho do agente é calculado após atingir o critério de término. A medida de desempenho do agente é o número de passos utilizados para completar o labirinto. O labirinto é
 concluído quando o agente chega à célula (11,1)

O ambiente é determinístico e totalmente observável

A percepção é fornecida pelo ambiente e inclui as coordenadas da célula e se a célula atual está vazia ou bloqueada.

matriz = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
'''

# Função para percorrer o grafo usando BFS e parar em uma coordenada alvo
def percorrer_bfs_ate_destino(grafo, start, destino):
    visitados = set()  # Para rastrear nós visitados
    fila = [start]  # Fila para a ordem de visita
    percurso = []  # Para armazenar a ordem do percurso

    while fila:
        atual = fila.pop(0)  # Remove o primeiro nó da fila
        if atual not in visitados:
            visitados.add(atual)  # Marca o nó como visitado
            percurso.append(atual)  # Adiciona ao percurso
            
            # Verifica se o nó atual é o destino
            if atual == destino:
                return percurso
            
            # Adiciona os vizinhos do nó atual na fila
            fila.extend(grafo.get(atual, []))

    return percurso  # Retorna o percurso caso o destino não seja encontrado

# Função para imprimir o labirinto percorrido
def imprimir_labirinto(matriz, caminho):
    # Cria uma cópia da matriz original
    matriz_percorrida = [row[:] for row in matriz]
    
    # Marca as células visitadas no caminho
    for x, y in caminho:
        matriz_percorrida[x][y] = 'X'

    # Imprime a matriz modificada
    print("Labirinto percorrido:")
    for linha in matriz_percorrida:
        print(" ".join(str(c) for c in linha))

# Função para converter uma matriz em um grafo
def matriz_para_grafo(matriz):
    grafo = {}
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    # Função auxiliar para verificar se a posição é válida
    def posicao_valida(x, y):
        return 0 <= x < linhas and 0 <= y < colunas and matriz[x][y] == 1
    
    # Criar os nós e arestas do grafo
    for x in range(linhas):
        for y in range(colunas):
            if matriz[x][y] == 1:  # Só processa células que podem ser visitadas
                vizinhos = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos: cima, baixo, esquerda, direita
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

# Converte a matriz em um grafo
grafo = matriz_para_grafo(matriz)

# Coordenadas inicial e de destino
start = (4, 11)
destino = (10, 0)

# Percorrer o grafo usando BFS até o destino
caminho_bfs = percorrer_bfs_ate_destino(grafo, start, destino)

# Imprime o labirinto percorrido
imprimir_labirinto(matriz, caminho_bfs)

# Imprime o caminho BFS
print("Caminho percorrido até o destino:", caminho_bfs)

# Calcula o custo do caminho (número de passos)
custo = len(caminho_bfs) - 1  # Custo é o número de passos até o destino, ou seja, o tamanho do caminho - 1

# Imprime a mensagem de custo
print(f"Custo do caminho (número de passos): {custo}")



