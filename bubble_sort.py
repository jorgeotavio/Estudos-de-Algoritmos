#Código desenvolvido por Jorge Otávio
#Bubble sort

def bubble_sort(vetor):
    if len(vetor) <= 1:
        return vetor

    for j in range(len(vetor)):
        for i in range(len(vetor)-1):
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

    return vetor