#Código desenvolvido por Jorge Otávio
#Shell sort

def shell_sort(vetor):
    apoio = len(vetor) // 2

    while apoio > 0:
        for i in range(apoio, len(vetor)):
            valor = vetor[i]
            j = i
            while j >= apoio and vetor[j - apoio] > valor:
                vetor[j] = vetor[j - apoio]
                j -= apoio

            vetor[j] = valor

        apoio //= 2