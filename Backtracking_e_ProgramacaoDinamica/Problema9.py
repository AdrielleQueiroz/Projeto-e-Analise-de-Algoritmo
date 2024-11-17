# CAIXEIRO VIAJANTE

def caixeiro(vertices_visitados = [0], arestas_visitadas = [], custo_atual = 0, valor_atual = 0, no_atual = 0):
    # O algoritmo percorre apenas os vértices que possuem uma aresta em comum com próximo vértice a ser analisado
    for i in range(vertices):#vértice adjacente
        # verifica se é diferente do nó atual e se uma aresta está  conectando o vertice atual ao adjacente
        if(i != no_atual and matriz_adjacencia[no_atual][i] > 0):
            # Atualiza o custo e o valor 
            custo_operacao = matriz_adjacencia[no_atual][i] + custo_atual
            valor_operacao = valor_atual + valores[i]
            # Verifica-se se o custo total da rota com a inclusão do vértice adjacente ainda está dentro do orçamento
            if(custo_operacao <= orcamento):
                # Verifica-se se a aresta entre o vértice atual e o vértice adjacente já foi utilizada na rota 
                if(set([no_atual, i]) not in arestas_visitadas):
                    # Verifica-se se o vértice adjacente já foi visitado na rota
                    if(i not in vertices_visitados):
                        # INCLUI O VÉRTICE E ARESTA COMO VISITADOS
                        vertices_visitados.append(i)
                        arestas_visitadas.append(set([no_atual, i]))#ele garante que a aresta é representada de forma única
                        caixeiro(vertices_visitados[:], arestas_visitadas[:], custo_operacao, valor_operacao, i)
                        # REMOVE O VÉRTICE E ARESTA DEPOIS DE CHAMAR O MÉTODO
                        vertices_visitados.pop(-1)
                        arestas_visitadas.pop(-1)
                    elif(i == 0):
                        # SE O VÉRTICE DESTINO JÁ FOI VISITADO MAS É O PRIMEIRO VÉRTICE ENTÃO FINALIZA O CAMINHO
                        caminho_final = vertices_visitados[:]
                        caminho_final.append(0)
                        completos.append([caminho_final, custo_operacao, valor_operacao])
orcamento = 10

valores = [10, 20, 30, 40]
# PREENCHER COM O CUSTO CASO HAJA UMA ARESTA ENTRE I E J 
# PREENCHER COM ZERO CASO NÃO HAJA ARESTA ENTRE I E J
matriz_adjacencia =[[0, 1, 2, 5], 
                    [1, 0, 6, 4], 
                    [2, 6, 0, 4], 
                    [5, 4, 4, 0]]
vertices = len(matriz_adjacencia) #Esta linha atribui o número de vértices (cidades) no grafo à variável vertices.
completos = [] # cria uma lista vazia para armazenar as rotas válidas encontradas pelo algoritmo.

#completos armazena todas as rotas válidas encontradas durante a execução da função caixeiro()
#Essas rotas são armazenadas como listas contendo o caminho percorrido, o custo total e o valor total obtido para cada rota válida

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

caixeiro()
# #IMPRIME TODOS OS CAMINHOS QUE SATISFAZEM:
# #   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
# #   2) OBEDECEM AO VALOR DO ORÇAMENTO;
# print('------------------------------------------------------------------')
# print('TODOS OS CAMINHOS:')
# print('------------------------------------------------------------------')
# for i in range(len(completos)):
#     print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
#     print('Custo: ', completos[i][1])
#     print('Valor: ', completos[i][2], end="\n\n")
# print('------------------------------------------------------------------')

#VALOR ÓTIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
#   2) OBEDECEM AO VALOR DO ORÇAMENTO;
#   3) TEM O MENOR VALOR DE CUSTO;
completos.sort(key = lambda x:x[1])#Ordena os caminhos na lista completos pelo custo (custo mínimo primeiro).
i = 0 
print('------------------------------------------------------------------')
print('VALOR ÓTIMO:')
print('------------------------------------------------------------------')
print('Caminho:', ' '.join([letras[x] for x in completos[i][0]]))
print('Custo mínimo:', completos[i][1])
print('Valor:', completos[i][2])
print('------------------------------------------------------------------')

#VALOR MÁXIMO
#IMPRIME QUALQUER CAMINHO QUE SATISFAZ:
#   1) COMEÇAM NO VÉRTICE A E TERMINAM NO VÉRTICE A; 
#   2) OBEDECEM AO VALOR DO ORÇAMENTO; 
#   3) TEM O MAIOR VALOR;
completos.sort(key = lambda x:x[2], reverse=True)#Ordena os caminhos na lista completos pelo valor (valor máximo primeiro).
i = 0
print('VALOR MÁXIMO:')
print('------------------------------------------------------------------')
print('Melhor caminho:', ' '.join([letras[x] for x in completos[i][0]]))#converte os índices dos vértices em letras, usando a lista letras
print('Custo:', completos[i][1])
print('Valor máximo:', completos[i][2])
print('------------------------------------------------------------------')



#O código apresentado utiliza programação dinâmica na resolução do problema do Caixeiro Viajante, pois não há a necessidade de calcular TODA a rota a cada vez que o vértice é analisado,
# ao contrário disso o que é feito é: Os custos e valores totais, vértices e arestas utilizados são armazenados em memória 
#por meio do empilhamento de memória da recursão, ou seja, sem necessidade de recalcular um trecho de rota que pertencem a diferentes "caminhos" analisados. 
#A função caixeiro se chama recursivamente para explorar diferentes rotas possíveis sem recalcular seu custo e valor novamente, 
#apenas utilizado o que já foi calculado até o vértice que está sendo analisado na rota

#Imagine que o caminho explorado a partir de i não leve a uma solução válida (por exemplo, excede o orçamento ou não retorna ao vértice inicial).
#Ao desfazer as escolhas, o algoritmo volta ao estado anterior e pode explorar outros caminhos a partir de no_atual.
#Sem remover o vértice e a aresta, o algoritmo exploraria o mesmo caminho repetidamente, perdendo tempo e eficiência.
