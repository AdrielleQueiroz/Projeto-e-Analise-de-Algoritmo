import sys
import time
from collections import defaultdict 

# Define o limite de recursão para 100.000
sys.setrecursionlimit(100000)

# Parâmetros iniciais
N, K = 4, 4
numberSolutions = 0 #Contador de soluções válidas encontradas
time_init = time #Número de segundos que o programa fica procurando resposta
LIMIT_TIME = 10
LIMIT_ADJACENT = 4 #Limite de células adjacentes a serem consideradas para restrição de cores
LIMIT_SOLUTIONS_SHOW = 1 #Número de soluções que ele mostra, nesse caso apenas a 1

# Dicionário para armazenar(todos os sub tabuleiros diferentes) submatrizes 2x2 vistas
sub = defaultdict(list) #é um dicionário onde a chave é a string s e o valor é uma lista de tuplas representando as posições onde essa configuração foi encontrada

X = [1, 0, -1, 0, -1, -1, 1, 1]  # representa as mudanças na coordenada da linha
Y = [0, 1, 0, -1, -1, 1, 1, -1]  # Y representa as mudanças na coordenada da coluna

#Exibe a matriz na tela de forma formatada
def show_matrix(matrix):
    print("===================")
    for row in matrix:
        print(' '.join(map(str, row)))
    print("===================")

# Verifica se não há células adjacentes com a mesma cor
def check_adjacentes(i, j, matrix):
    global LIMIT_ADJACENT #limite dos vizinhos que devem ser considerados
    for d in range(LIMIT_ADJACENT):
        if 0 <= i + X[d] < N and 0 <= j + Y[d] < N:  # matriz Super Infer
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i + X[d]][j + Y[d]]: #se está vazia e as comp cores
                return False #acélula adjacente com a mesma cor, portanto, a pintura atual não é válida.
    return True #indicando que a pintura é válida.

#Verificar se as diagonais principais e secundárias da matriz satisfazem as restrições de cor.
def check_diagonals(matrix):
    for i in range(N):#i varia de 0 a n-1
        if (matrix[i][i] != 0 and matrix[i][N-i-1] != 0 and matrix[i][N-i-1] != matrix[i][i]): #possuem cores diferentes cores válidas
            return False
    return True

#cria uma string única para cada configuração de cores em uma submatriz 2x2
def get_sub_board_2x2(i, j, matrix):
    s = str(matrix[i][j]) + str(matrix[i-1][j]) + str(matrix[i-1][j-1]) + str(matrix[i][j-1]) #concatenando as representações de string das quatro células da submatriz 2x2.
    return s #representação das cores na submatriz 2x2

#verifica se uma submatriz 2x2 já foi encontrada antes
def check_sub_board_2x2(i, j, matrix):
    if i == 0 or j == 0: # Se está na primeira linha ou coluna, não verifica
        return True
    s = get_sub_board_2x2(i, j, matrix)
    #verifica se a submatriz 2x2 representada por s já foi encontrada antes.
    if len(sub[s]) > 0: #, significa que já encontramos essa configuração de submatriz 
        return False # Restrição violada
    return True # Nenhuma restrição violada

#Adicionar configurações de submatrizes 2x2 ao dicionário sub durante a exploração da solução, garantindo que não haja sobreposição ou repetição
def add_board_2x2(i, j, matrix):
    if i == 0 or j == 0:#verifico se posso adicionar
        return
    s = get_sub_board_2x2(i, j, matrix)
    sub[s].append((i, j))#Esta linha adiciona a posição (i, j) da submatriz 2x2 ao dicionário sub.

#Remove configurações de submatrizes 2x2 ao dicionário sub durante a exploração da solução, garantindo que não haja sobreposição ou repetição
def rm_board_2x2(i, j, matrix):
    if i == 0 or j == 0:
        return
    s = get_sub_board_2x2(i, j, matrix)
    if len(sub[s]) == 0: # significa que não há nenhuma instância registrada dessa submatriz 2x2 no dicionário sub.
        return
    sub[s].pop()#remove o último elemento dessa lista

def next_node(i, j):
    # última coluna da linha i, vou para a próxima linha
    if j == N - 1:
        return (i + 1, 0)
    # caso contrário vou para a próxima coluna
    else:
        return (i, j + 1)

def solve(i, j, matrix):
    global numberSolutions, LIMIT_TIME, time_init
    # atingiu o limite de tempo
    if time.time() - time_init >= LIMIT_TIME:
        return 0
    # caso base: se chegou ao final da matriz
    if i == N and j == 0:
        numberSolutions += 1 # Incrementa o contador de soluções válidas
        if numberSolutions <= LIMIT_SOLUTIONS_SHOW:
            show_matrix(matrix) # Mostra a matriz se a flag estiver ativada
        return 1  # Retorna 1 solução encontrada
    # recusão
    ans = 0
    for c in range(1, K + 1):
        matrix[i][j] = c  # pinta na cor c
        # verifica se pintando a célula na cor c as restrições ainda estão sendo atendidas para avançar para a próxima célula
        if check_sub_board_2x2(i, j, matrix) and check_adjacentes(i, j, matrix) and check_diagonals(matrix):
            add_board_2x2(i, j, matrix)  # Adiciona a submatriz 2x2 ao dicionário
            next_i, next_j = next_node(i, j)  # Determina o próximo nó
            ans += solve(next_i, next_j, matrix)# Chamada recursiva para o próximo nó
            rm_board_2x2(i, j, matrix) # Remove a submatriz 2x2 do dicionário
        matrix[i][j] = 0  # remove a cor c, deixando branca novamente
    return ans

matrix = [[0] * N for _ in range(N)]#cria uma matriz N x N preenchida com 0
time_init = time.time()
result = solve(0, 0, matrix) if N % 2 != 0 else 0 # se n for impa ele chama solve caso contrario ele add 0 ao resultado
print(f"A matriz possui {result} configuracoes validas")