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

O desempenho do agente é calculado após atingir o critério de término. A medida de desempenho do agente é o número de passos utilizados para completar o labirinto. O labirinto é concluído quando o agente chega à célula (11,1)

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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''

from collections import deque

# Coordenadas ajustadas para o formato Python (0-indexado)
estado_inicial = (4, 11)  # Convertendo (5, 12) para índice de matriz
estado_objetivo = (10, 0)  # Convertendo (11, 1) para índice de matriz

# Definição do labirinto
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Função que retorna os sucessores válidos para o estado atual
def sucessor(estado):
    x, y = estado
    movimentos = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Cima, Esquerda, Direita, Baixo
    sucessores = []

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        # Verifica se o movimento é dentro dos limites da matriz e se é permitido (célula vazia)
        if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] == 1:
            sucessores.append((nx, ny))

    return sucessores

# Testa se o estado atual é o objetivo
def teste_objetivo(estado):
    return estado == estado_objetivo

# Retorna o custo do caminho (número de passos)
def custo_caminho(caminho):
    return len(caminho)

# Algoritmo de busca em largura
def busca_largura(estado_inicial):
    fronteira = deque([[estado_inicial]])  # Fronteira inicial com o caminho contendo o estado inicial
    visitados = set([estado_inicial])  # Conjunto de estados visitados

    while fronteira:
        caminho = fronteira.popleft()  # Remove o caminho mais antigo da fila
        estado = caminho[-1]  # Último estado no caminho

        # Verifica se o estado atual é o objetivo
        if teste_objetivo(estado):
            return caminho

        # Expande os sucessores do estado atual
        for proximo_estado in sucessor(estado):
            if proximo_estado not in visitados:
                visitados.add(proximo_estado)
                fronteira.append(caminho + [proximo_estado])  # Adiciona novo caminho à fronteira

    return None  # Retorna None se nenhum caminho for encontrado

# Execução do algoritmo
caminho = busca_largura(estado_inicial)

# Exibição do resultado
if caminho:
    print("Caminho encontrado:")
    print(caminho)
    print("Custo do caminho:", custo_caminho(caminho))
else:
    print("Nenhum caminho encontrado.")

