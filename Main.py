# Atividade 1 – SISTEMA DE PROCESSAMENTO DE DADOS
# Uma empresa de processamento de dados precisa ordenar grandes volumes de valores inteiros não negativos, como identificadores e pontuações.
# Para atender diferentes cenários, o sistema deve oferecer múltiplos algoritmos de ordenação, escolhidos conforme as características dos dados.
# Você deverá implementar uma estrutura de dados baseada em lista encadeada, contendo:
# Uma classe Nodo, que representa cada elemento
# Uma classe Lista, que gerencia a estrutura e oferece métodos de ordenação

# Requisitos
# A classe Lista deve implementar os seguintes métodos:
# merge_sort()
# quick_sort()
# counting_sort()
# radix_sort()
# Todos os métodos devem:
# Ordenar os elementos em ordem crescente
# Manter os dados dentro da própria estrutura Lista
# Restrições
# Os valores são inteiros não negativos
# counting_sort e radix_sort só devem ser usados quando a restrição acima for respeitada

# DATA DE ENTRAGA FINAL DIA 27 DE ABRIL.

# BRANCH 1 Feito em aula dia 13 de abril (todo conteudo executado em aula no projeto)

def selection_sort(lista):
    if not lista:
        return lista
    for i in range(len(lista)):
        min_i = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]
    print(lista)


selection_sort([2, 4, 3, 6, 9, 1, 6, 3])


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_no_final(self, valor):
        novo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
            return
        self.fim.proximo = novo_nodo
        self.fim = novo_nodo

    def exibir(self):
        if self.inicio is None:
            print([])
            return
        atual = self.inicio
        valores = []
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        print(valores)

    def selection_sort(self):
        if self.inicio is None or self.inicio.proximo is None:
            return
        atual = self.inicio
        while atual is not None:
            menor = atual
            busca = atual.proximo
            while busca is not None:
                if busca.valor < menor.valor:
                    menor = busca
                busca = busca.proximo
            if menor is not atual:
                atual.valor, menor.valor = menor.valor, atual.valor
            atual = atual.proximo

