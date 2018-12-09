import collections

class Lista():
    def __init__(self, seq=None):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__iterando = None
        self.__erro = 'índice fora dos limites da lista'

        if seq is not None and isinstance(seq, collections.Iterable):
            for e in seq:
                self.inserir_fim(e)
        elif seq is not None:
            raise TypeError('O objeto fornecido não é iterável.')

    class No:
        def __init__(self, conteudo):
            self.conteudo = conteudo
            self.proximo = None
            self.anterior = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.conteudo
        else:
            raise StopIteration

    def __len__(self):
        return self.__tamanho

    def __inicializar_valores_fatiamento(self, item):

        if item.start is None:
            start = 0
        else:
            start = item.start

        if item.stop is None:
            stop = len(self)
        else:
            stop = item.stop

        if item.step is None:
            step = 1
        else:
            step = item.step

        if start < 0:
            start += len(self)
            if start < 0:
                start = 0

        if stop < 0:
            stop += len(self)

        if step == 0:
            raise ValueError('Step do fatiamento não pode ser zero')

        return start, stop, step

    def __getitem__(self, item):
        if isinstance(item, slice):
            _lista = Lista()

            start, stop, step = self.__inicializar_valores_fatiamento(item)

            i = start
            while 0 <= i < stop:
                if i>=len(self):
                    break
                _lista.inserir_fim(self[i])
                i += step

            return _lista
        else:
            if item < 0:
                item += len(self)

            if item < 0 or item >= len(self):
                raise IndexError(self.__erro)

            i = 0
            atual = self.__primeiro
            while i <= item:
                if atual is None:
                    break

                if i == item:
                    return atual.conteudo

                atual = atual.proximo
                i+=1

    def __setitem__(self, item, value):
        if isinstance(item, slice):
            raise Exception('não disponivel')
        else:
            if item < 0:
                item += len(self)

            if item < 0 or item >= len(self):
                raise IndexError(self.__erro)

            i = 0
            atual = self.__primeiro
            while i <= item:
                if atual is None:
                    break

                if i == item:
                    return atual.conteudo
                    break

                atual = atual.proximo
                i+=1
