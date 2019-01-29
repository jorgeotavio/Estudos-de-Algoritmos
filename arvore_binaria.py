class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.esquerda = None
            self.direita = None
            self.valor = valor

        def __str__(self):
            return str(self.valor)

        def __repr__(self):
            return self.__str__()

    def minimo(self, atual=None):
        if atual is None:
            atual = self.__raiz

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def maximo(self, atual=None):
        if atual is None:
            atual = self.__raiz

        while atual.direita is not None:
            atual = atual.direita

        return atual

    def buscar(self, valor):
        atual = self.__raiz

        while atual is not None and valor != atual.valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return atual

    def buscar_recursivo(self, valor):

        def recursao(atual, valor):

            if valor == atual.valor or atual is None:
                return atual

            if valor < atual.valor:
                return recursao(atual.esquerda, valor)
            else:
                return recursao(atual.direita, valor)

        return recursao(self.__raiz, valor)

    def inserir(self, valor):
        pai_atual = None
        atual = self.__raiz  # começando pela raiz
        novo = self.No(valor)  # criando o novo nó com o valor

        while atual is not None:
            pai_atual = atual

            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai_atual

        if pai_atual is None:
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            pai_atual.esquerda = novo
        else:
            pai_atual.direita = novo

    def sucessor(self, valor):
        atual = self.buscar(valor)

        if atual is None:
            return atual

        if atual.direita is not None:
            return self.minimo(atual.direita)

        pai_atual = atual.pai

        while pai_atual is not None and atual == pai_atual.direita:
            atual = pai_atual
            pai_atual = pai_atual.pai

        if pai_atual is None:
            return pai_atual

        return pai_atual

    def predecessor(self, valor):
        atual = self.buscar(valor)

        if atual is None:
            return atual

        if atual.esquerda is not None:
            return self.maximo(atual.esquerda)

        pai_atual = atual.pai

        while pai_atual is not None and atual == pai_atual.esquerda:
            atual = pai_atual
            pai_atual = pai_atual.pai

        if pai_atual is None:
            return pai_atual

        return pai_atual

    def apagar(self, valor):
        sera_removido = self.buscar(valor)

        if sera_removido.esquerda is None:
            self.recortar(sera_removido, sera_removido.direita)
        elif sera_removido.direita is None:
            self.recortar(sera_removido, sera_removido.esquerda)
        else:
            sucessor = self.sucessor(sera_removido.valor)

            if sucessor.pai != sera_removido:
                self.recortar(sucessor, sucessor.direita)

                sucessor.direita = sera_removido.direita
                sucessor.direita.pai = sucessor

            self.recortar(sera_removido, sucessor)

            sucessor.esquerda = sera_removido.esquerda
            sucessor.esquerda.pai = sucessor

    def recortar(self, sera_removido, sera_recortado):
        if sera_removido.pai is None:
            self.__raiz = sera_recortado
        elif sera_removido == sera_removido.pai.esquerda:
            sera_removido.pai.esquerda = sera_recortado
        else:
            sera_removido.pai.direita = sera_recortado

        if sera_recortado is not None:
            sera_recortado.pai = sera_removido.pai

    def listar(self):
        lista = []

        def em_ordem(atual):
            if atual is not None:
                em_ordem(atual.esquerda)
                lista.append(atual.valor)
                em_ordem(atual.direita)

        em_ordem(self.__raiz)

        return lista