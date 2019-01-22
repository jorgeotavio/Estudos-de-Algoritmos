class ArvoreBinaria:
    def __init__(self):
        self._raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.esq = None
            self.dir = None
            self.val = valor

    def minimo(self):
        atual = self._raiz
        while atual.esq is not None:
            atual = atual.esq
        return atual.valor

    def maximo(self):
        atual = self._raiz
        while atual.dir is not None:
            atual = atual.dir
        return atual.valor

    def buscar(self, valor):
        atual = self._raiz

        while atual is not None and valor != atual.valor:
            if valor < atual.valor:
                atual = atual.esq
            else:
                atual = atual.dir

        return atual

    def inserir(self, valor):
        pai_atual = None
        atual = self._raiz
        novo = self.No(valor)

        while atual is not None:
            pai_atual = atual

            if novo.valor < atual.valor:
                atual = atual.esq
            else:
                atual = atual.dir

        novo.pai = pai_atual

        if pai_atual is None:
            self._raiz = novo
        elif novo.valor < pai_atual.valor:
            pai_atual.esq = novo
        else:
            pai_atual.direita = novo
