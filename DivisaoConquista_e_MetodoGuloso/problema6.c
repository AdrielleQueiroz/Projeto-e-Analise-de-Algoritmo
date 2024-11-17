#include <stdio.h>
#include <stdlib.h>

#define MAX_INTERVALOS 1000

typedef struct { // Definição de uma estrutura para representar intervalos
    int inicio;
    int fim;
} Intervalo;

int particionar(Intervalo arr[], int baixo, int alto) {
    Intervalo pivo = arr[alto];
    int i = baixo - 1; // Índice do menor elemento
    for (int j = baixo; j <= alto - 1; j++) {
        if (arr[j].inicio < pivo.inicio) {
            i++;
            Intervalo temp = arr[i]; // Troca arr[i] e arr[j]
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    Intervalo temp = arr[i + 1]; //Após o fim do loop, o pivô é trocado com o elemento na posição i + 1.
    arr[i + 1] = arr[alto];
    arr[alto] = temp;
    return (i + 1); // Retorna o índice do pivô após a partição
}

void quick_sort(Intervalo arr[], int baixo, int alto) { // Função para ordenar o array de intervalos
    if (baixo < alto) {
        int pi = particionar(arr, baixo, alto); // Obtém o índice do pivô após a partição
        quick_sort(arr, baixo, pi - 1);
        quick_sort(arr, pi + 1, alto);
    }
}

void colorir_intervalos(Intervalo *intervalos, int numIntervalos) { // Função para colorir os intervalos
    quick_sort(intervalos, 0, numIntervalos - 1); // Ordena os intervalos usando o quicksort. 

    char *cores[10] = {"Vermelho", "Amarelo", "Azul", "Verde", "Laranja", "Roxo", "Marrom", "Rosa", "Ciano", "Branco"};
    int cores_usadas[MAX_INTERVALOS]; // Array para armazenar as cores usadas por cada intervalo
    for (int i = 0; i < numIntervalos; i++) { //não atribuídas (-1)
        cores_usadas[i] = -1;
    }

    int proximaCor = 0;// a próxima cor a ser usada
    for (int i = 0; i < numIntervalos; i++) {
        int inicio = intervalos[i].inicio;
        int fim = intervalos[i].fim;
        int cores_utilizadas[MAX_INTERVALOS]; // Array para armazenar as cores usadas pelos intervalos que se intersectam com o intervalo atual
        for (int j = 0; j < i; j++) { // intervalos anteriores
            if (intervalos[j].fim > inicio) { // Se o intervalo anterior se intersecta com o intervalo atual
                cores_utilizadas[j] = cores_usadas[j]; // Armazena a cor usada pelo intervalo anterior
            } else {
                cores_utilizadas[j] = -1; //marca como não atribuída
            }
        }
        int corDisponivel = 0; // Variável para armazenar a próxima cor disponível
        for (int j = 0; j < i; j++) { //cores usadas pelos intervalos anteriores
            if (cores_utilizadas[j] == corDisponivel) { // Se a cor estiver sendo usada
                corDisponivel++; // Tenta a próxima cor disponível
                j = -1; // Reinicia o loop para verificar se a próxima cor também está sendo usada
            }
        }
        cores_usadas[i] = corDisponivel; // Atribui a próxima cor disponível ao intervalo atual
        proximaCor = (proximaCor > corDisponivel) ? proximaCor : corDisponivel; // Atualiza o número total de cores usadas
    }

    printf("\n");
    for (int i = 0; i < numIntervalos; i++) { // Imprime os intervalos com suas respectivas cores
        printf("Intervalo (%d, %d): Cor %s\n", intervalos[i].inicio, intervalos[i].fim, cores[cores_usadas[i]]);
    }
    printf("\nForam usadas %d cores para colorir %d intervalos.", proximaCor + 1, numIntervalos); // Imprime o total de cores usadas
}

int main() {
    int numIntervalos;
    printf("Insira o número de intervalos: ");
    scanf("%d", &numIntervalos); // Solicita ao usuário o número de intervalos

    Intervalo *intervalos = (Intervalo *)malloc(numIntervalos * sizeof(Intervalo)); // Aloca memória para os intervalos
    if (intervalos == NULL) {
        printf("Falha na alocação de memória.\n");
        return 1;
    }

    printf("Insira os intervalos no formato inicio fim:\n");
    for (int i = 0; i < numIntervalos; i++) { // Solicita ao usuário os intervalos
        printf("Intervalo %d: ", i + 1);
        scanf("%d %d", &intervalos[i].inicio, &intervalos[i].fim);
    }

    colorir_intervalos(intervalos, numIntervalos); // Chama a função para colorir os intervalos

    free(intervalos);
    return 0;
}

//lógica de atribuição de cores pode ser considerada gulosa, pois atribui a próxima cor disponível a cada intervalo sem considerar futuras escolhas.
//a cor que ainda não foi usada por nenhum intervalo que se intersecta com o intervalo atual) para cada intervalo. 
//Isso é feito de maneira gulosa, ou seja, a decisão é tomada com base na informação disponível no momento, sem considerar as consequências futuras.