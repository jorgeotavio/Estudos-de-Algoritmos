class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    class No:
        def __init__(self, conteudo):
            self.conteudo = conteudo
            self.proximo = None

    def __len__(self):
        return self.__tamanho

    def __getitem__(self, item):
        if self.primeiro is not None:
            atual = self.primeiro
            indice = 0
            while atual is not None:
                if item == indice:
                    return atual.conteudo

                atual = atual.proximo
                indice += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo
        
        if self.__iterando is not None:
            return self.__iterando.conteudo
        
        raise StopIteration

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        retorno = '['

        for i, e in enumerate(self):
            retorno += repr(e)
            if i < len(self)-1:
                retorno += ','

        retorno += ']'
        return retorno
    
    def __delitem__(self, i):
        if self.primeiro is not None:
            atual = self.primeiro
            self.primeiro = self.primeiro.proximo
            atual.proximo = None
            
            self.__tamanho -= 1
            self.__iterando = None
    
    def inserir(self, conteudo):
        novo = self.No(conteudo)
        
        if self.__tamanho == 0:
            self.primeiro = novo
            self.ultimo = novo
        
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo
            
        self.__tamanho += 1
        self.__iterando = None
    
    def pop(self):
        del self[0]

fila = Fila()

fila.inserir(23)
fila.inserir(4)
fila.inserir(5)
fila.inserir(6)
fila.inserir(19)

fila.pop()

print(fila)

