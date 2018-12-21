#Código desenvolvido por Jorge Otávio
#Selection sort

def selectionSort(vetor):
    for i in range(len(vetor)):
        menor = i

        for j in range(i + 1, len(vetor)):
            if vetor[menor] > vetor[j]:
                menor = j

        temp = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = temp

    return vetor