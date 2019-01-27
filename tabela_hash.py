class TabelaHash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__qnt_elementos = 0
        self.__tabela = []
        self.__inicializar_tabela()

    class Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    def keys(self):
        chaves = []
        for lista in self.__tabela:
            for elemento in lista:
                chaves.append(elemento.chave)

        return chaves

    def values(self):
        valores = []
        for lista in self.__tabela:
            for elemento in lista:
                valores.append(elemento.valor)

        return valores

    def items(self):
        itens = []
        for lista in self.__tabela:
            for elemento in lista:
                tupla = elemento.chave, elemento.valor
                itens.append(tupla)

        return itens

    def __iter__(self):
        return iter(self.keys())

    def __len__(self):
        return self.__qnt_elementos

    def __contains__(self, key):
        try:
            self.__pegar_elemento_interno(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key):
        elemento = self.__pegar_elemento_interno(key)
        return elemento.valor

    def __setitem__(self, key, value):
        self.__atualizar_chave(key, value)

    def __delitem__(self, key):
        índice = self.__função_hash(key)
        for i, elemento in enumerate(self.__tabela[índice]):
            if elemento.chave == key:
                del self.__tabela[índice][i]
                self.__qnt_elementos -= 1
                return

        raise KeyError(key)

    def __str__(self):
        retorno = '{'

        i = 0
        for chave, valor in self.items():
            retorno += chave.__repr__()
            retorno += ': '
            retorno += valor.__repr__()

            if i < len(self) - 1:
                retorno += ', '

            i += 1

        retorno += '}'
        return retorno

    def __repr__(self):
        return self.__str__()

    def __pegar_elemento_interno(self, key):
        índice = self.__função_hash(key)
        for elemento in self.__tabela[índice]:
            if elemento.chave == key:
                return elemento

        raise KeyError(key)

    def __atualizar_chave(self, key, value):
        try:
            elemento = self.__pegar_elemento_interno(key)

            elemento.valor = value
        except KeyError:
            índice = self.__função_hash(key)
            novo_elemento = self.Elemento(key, value)
            self.__tabela[índice].append(novo_elemento)
            self.__qnt_elementos += 1

    def __inicializar_tabela(self):
        for i in range(self.__tamanho):
            self.__tabela.append([])

    def __função_hash(self, chave):
        return hash(chave) % self.__tamanho


notas = TabelaHash(11)
pessoa = TabelaHash(11)

notas['1va'] = 7.9
notas['2va'] = 7.2
notas['3va'] = 8.6

pessoa['nome'] = 'igu'
pessoa['idade'] = 31
pessoa['profissão'] = 'Professor'
pessoa['notas'] = notas

pessoa['nome'] = 'nels'
pessoa['idade'] = 18
pessoa['profissão'] = 'alunoi'
pessoa['notas'] = notas

print(pessoa['profissão'])
print(len(pessoa))
print('notas' in pessoa)
print(pessoa)
print()
for e in pessoa.keys():
    print(e)

# aluno = {'nome': 'Fulano da Silva', 'idade': 30}
#
# for e in aluno.values():
#     print(e)
