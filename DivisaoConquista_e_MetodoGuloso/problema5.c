//Adrielle Maria Alves Queiroz
//Problema: dado um vetor de entrada com elementos de um tipo qualquer, utilize a divisão e conquista para encontrar o elemento mais frequente:
//Ordenar o vetor de entrada primeiro, para depois determinar o elemento mais frequente, não conta;
//O algoritmo proposto pelo aluno não pode ser apenas para vetores com elementos de um tipo de dados específico, como inteiros ou caracteres.

#include <stdio.h>
#include <stdlib.h>

// Estrutura genérica para contar elementos
typedef struct {
    void *elemento;
    int contagem;
} ElementoContado;

// Função para mesclar duas partes ordenadas do vetor
void merge(ElementoContado vetor[], int inicio,  int meio, int fim, int (*comparar)(const void *, const void *)) {
    int tamanho_esquerda = meio - inicio + 1;
    int tamanho_direita = fim - meio; //Neste caso, não adicionamos 1 porque meio é o último índice do subvetor esquerdo

    ElementoContado *vetor_esquerda = (ElementoContado *)malloc(tamanho_esquerda * sizeof(ElementoContado));
    ElementoContado *vetor_direita = (ElementoContado *)malloc(tamanho_direita * sizeof(ElementoContado));

    // Copiando dados para os vetores esquerdo e direito
    for (int i = 0; i < tamanho_esquerda; i++) {
        vetor_esquerda[i] = vetor[inicio + i];
    }
    for (int j = 0; j < tamanho_direita; j++) {
        vetor_direita[j] = vetor[meio + 1 + j];
    }

    //Esses índices são usados para rastrear a posição atual nos vetores esquerdo, direito e original
    int indice_esquerda = 0, indice_direita = 0, indice_mistura = inicio;
    // Mesclando os vetores esquerdo e direito de volta ao vetor original
    while (indice_esquerda < tamanho_esquerda && indice_direita < tamanho_direita) { //continua enquanto os índices indice_esquerda e indice_direita forem menores que tamanho_esquerda e tamanho_direita
        if (comparar(vetor_esquerda[indice_esquerda].elemento, vetor_direita[indice_direita].elemento) <= 0) {
            vetor[indice_mistura] = vetor_esquerda[indice_esquerda];
            indice_esquerda++;
        } else {
            vetor[indice_mistura] = vetor_direita[indice_direita];
            indice_direita++;
        }
        indice_mistura++;
    }

    // Copiando os elementos restantes do vetor esquerdo, se houver
    while (indice_esquerda < tamanho_esquerda) {
        vetor[indice_mistura] = vetor_esquerda[indice_esquerda];
        indice_esquerda++;
        indice_mistura++;
    }

    // Copiando os elementos restantes do vetor direito, se houver
    while (indice_direita < tamanho_direita) {
        vetor[indice_mistura] = vetor_direita[indice_direita];
        indice_direita++;
        indice_mistura++;
    }

    free(vetor_esquerda);
    free(vetor_direita);
}

// Função recursiva para ordenar o vetor usando mergesort
void mergesort(ElementoContado vetor[], int inicio, int fim, int (*comparar)(const void *, const void *)) {
    if (inicio < fim) {
        int meio = inicio + (fim - inicio) / 2;

        mergesort(vetor, inicio, meio, comparar);//primeiro
        mergesort(vetor, meio + 1, fim, comparar);//segunda

        merge(vetor, inicio, meio, fim, comparar);//combina
    }
}

// Função para imprimir os elementos mais frequentes. Tamanho_elemento em byte
void imprimirElementosMaisFrequentes(void *vetor, int tamanho, size_t tamanho_elemento, int (*comparar)(const void *, const void *)) {
    ElementoContado *elementos_contados = (ElementoContado *)malloc(tamanho * sizeof(ElementoContado));
    for (int i = 0; i < tamanho; i++) { // Para cada elemento no vetor original, armazena um ponteiro para esse elemento
        // no vetor 'elementos_contados'.
        elementos_contados[i].elemento = (char *)vetor + i * tamanho_elemento;
        elementos_contados[i].contagem = 0;
    }

    mergesort(elementos_contados, 0, tamanho - 1, comparar);  //ordenar o vetor elementos_contados com base na comparação dos elementos.


    int contador = 1;//acompanhar a contagem de frequências
    for (int i = 0; i < tamanho - 1; i++) {
        if (comparar(elementos_contados[i].elemento, elementos_contados[i + 1].elemento) == 0) { //Se o elemento atual for igual ao anterior, incrementa contador.
            contador++;
        } else {
            printf("(");
            printf("%c", *((char *)elementos_contados[i].elemento));
            printf(", %d) ", contador);
            contador = 1;
        }
    }
    
    //Imprime o último elemento e sua contagem.
    printf("(");
    printf("%c", *((char *)elementos_contados[tamanho - 1].elemento));
    printf(", %d)\n", contador);

    free(elementos_contados);
}

// Função de comparação para caracteres
int compararCaracteres(const void *a, const void *b) {
    char *caractere1 = (char *)a; // Converte os ponteiros void para ponteiros de char
    char *caractere2 = (char *)b;
    return *caractere1 - *caractere2; // Compara os caracteres e retorna a diferença
}

int main() {
    char vetor[] = {'A', 'B', 'A', 'C','B', 'D'};
    //char vetor[] = {'A', 'B', 'A', 'C', 'A', 'B', 'A', 'D'};

    //Obtém o tamanho do vetor (tamanho) dividindo o tamanho total em bytes pelo tamanho de cada elemento.
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    imprimirElementosMaisFrequentes(vetor, tamanho, sizeof(char), compararCaracteres);

    return 0;
}