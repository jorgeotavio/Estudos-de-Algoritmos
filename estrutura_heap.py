#Código desenvolvido por Jorge Otávio
#Estrutura Heap

class Heap:

    def __init__(self, heap = None):
        if heap is None: 
            self.__heap = []
        else:
            self.__heap = heap

    def __getitem__(self, i):
        return self.__heap[i]

    def __len__(self):
        return self.__heap.__len__()

    def __str__(self):
        return str(self.__heap)

    @property
    def heap(self):
        return self.__heap

    @heap.setter
    def heap(self, obj):
        self.__heap = list(obj)

    def pai(self,i):
        _pai = (i-1)/2
        if _pai >= 0:
            return int(_pai)
        else:
            return None

    def esquerda(self, i):
        _esquerda = (i*2)+1
        if _esquerda < len(self):
            return _esquerda
        else:
            return None

    def direita(self, i):
        _direita = (i*2+1)+1
        if _direita < len(self):
            return _direita
        else:
            return None

    def construir_heap(self):
        i = (len(self) // 2) - 1
        while i >= 0:
            self.heapify(i)
            i-=1

    def heapify(self, i):
        e = self.esquerda(i)
        d = self.direita(i)

        maior = i
        if e is not None and self[e] > self[i]:
            maior = e

        if d is not None and self[d] > self[maior]:
            maior = d

        if maior != i:
            self.__heap[i], self.__heap[maior] = self.__heap[maior], self.__heap[i]
            self.heapify(maior)

    def extrair_maximo(self):
        if len(self) > 0:
            maximo = self[0]
            self.__heap[0] = self.__heap[-1]
            del self.__heap[-1]
            self.heapify(0)
            return maximo
        else:
            return None

    def sort(self):
        self.construir_heap()
        ordenado = []
        i = len(self) - 1
        while i >= 0:
            ordenado.insert(0, self.extrair_maximo())
            i -= 1
        self.__heap = ordenado
        return ordenado

    def aumentar_chave(self, i, chave):
        if chave > self[i]:
            self.__heap[i] = chave
            while i > 0 and self[self.pai(i)] < self[i]:
                self.__heap[i], self.__heap[self.pai(i)] = self.__heap[self.pai(i)], self.__heap[i]
                i = self.pai(i)

    def inserir(self, chave):
        self.__heap.append(chave - 1)
        self.aumentar_chave(len(self)-1, chave)
