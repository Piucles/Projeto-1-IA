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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''

from collections import deque

# Definindo o labirinto
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


# Definindo os parâmetros do problema
estado_inicial = (4, 11)
objetivo = (10, 0)
movimentos = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Cima, Esquerda, Direita, Baixo

def busca_em_largura(matriz, estado_inicial, objetivo):
    fila = deque([estado_inicial])
    visitados = set()
    caminho = {estado_inicial: None}
    
    while fila:
        estado_atual = fila.popleft()
        
        if estado_atual == objetivo:
            return reconstruir_caminho(caminho, estado_inicial, objetivo)
        
        for movimento in movimentos:
            novo_estado = (estado_atual[0] + movimento[0], estado_atual[1] + movimento[1])
            
            if (0 <= novo_estado[0] < len(matriz) and
                0 <= novo_estado[1] < len(matriz[0]) and
                matriz[novo_estado[0]][novo_estado[1]] == 1 and
                novo_estado not in visitados):
                
                fila.append(novo_estado)
                visitados.add(novo_estado)
                caminho[novo_estado] = estado_atual
    
    return None

def reconstruir_caminho(caminho, inicio, fim):
    atual = fim
    caminho_reconstruido = []
    
    while atual is not None:
        caminho_reconstruido.append(atual)
        atual = caminho[atual]
    
    caminho_reconstruido.reverse()
    return caminho_reconstruido

# Executando a busca em largura
caminho = busca_em_largura(matriz, estado_inicial, objetivo)
print("Caminho encontrado:", caminho)

#imprimindo o labirinto
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if (i, j) in caminho:
            print("x", end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()

print("Número de passos:", len(caminho) - 1)

