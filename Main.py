class Nodo:
	# Representa cada elemento da lista encadeada.
	def __init__(self, valor):
		self.valor = valor
		self.proximo = None


class Lista:
	# Estrutura principal da atividade.
	def __init__(self):
		self.inicio = None
		self.fim = None

	def inserir_final(self, valor):
		novo = Nodo(valor)
		if self.inicio is None:
			self.inicio = novo
			self.fim = novo
			return
		self.fim.proximo = novo
		self.fim = novo

	def carregar_valores(self, valores):
		# Reinicia a lista e carrega novamente os dados.
		self.inicio = None
		self.fim = None
		for valor in valores:
			self.inserir_final(valor)

	def para_lista(self):
		valores = []
		atual = self.inicio
		while atual is not None:
			valores.append(atual.valor)
			atual = atual.proximo
		return valores

	def exibir(self):
		print(self.para_lista())

	def _validar_nao_negativos(self, valores):
		for valor in valores:
			if not isinstance(valor, int) or valor < 0:
				raise ValueError(
					"counting_sort e radix_sort exigem apenas inteiros nao negativos"
				)

	def merge_sort(self):
		valores = self.para_lista()

		def ordenar(vetor):
			if len(vetor) <= 1:
				return vetor

			meio = len(vetor) // 2
			esquerda = ordenar(vetor[:meio])
			direita = ordenar(vetor[meio:])
			return intercalar(esquerda, direita)

		def intercalar(esquerda, direita):
			resultado = []
			i = 0
			j = 0

			while i < len(esquerda) and j < len(direita):
				if esquerda[i] <= direita[j]:
					resultado.append(esquerda[i])
					i += 1
				else:
					resultado.append(direita[j])
					j += 1

			resultado.extend(esquerda[i:])
			resultado.extend(direita[j:])
			return resultado

		ordenado = ordenar(valores)
		self.carregar_valores(ordenado)

	def quick_sort(self):
		valores = self.para_lista()

		def ordenar(vetor):
			if len(vetor) <= 1:
				return vetor

			pivo = vetor[-1]
			menores_ou_iguais = []
			maiores = []

			for valor in vetor[:-1]:
				if valor <= pivo:
					menores_ou_iguais.append(valor)
				else:
					maiores.append(valor)

			return ordenar(menores_ou_iguais) + [pivo] + ordenar(maiores)

		ordenado = ordenar(valores)
		self.carregar_valores(ordenado)

	def counting_sort(self):
		valores = self.para_lista()
		if not valores:
			return

		self._validar_nao_negativos(valores)

		maior = max(valores)
		contagem = [0] * (maior + 1)

		for valor in valores:
			contagem[valor] += 1

		ordenado = []
		for numero, frequencia in enumerate(contagem):
			ordenado.extend([numero] * frequencia)

		self.carregar_valores(ordenado)

	def radix_sort(self):
		valores = self.para_lista()
		if not valores:
			return

		self._validar_nao_negativos(valores)

		maior = max(valores)
		exp = 1

		while maior // exp > 0:
			baldes = [[] for _ in range(10)]

			for valor in valores:
				digito = (valor // exp) % 10
				baldes[digito].append(valor)

			valores = []
			for balde in baldes:
				valores.extend(balde)

			exp *= 10

		self.carregar_valores(valores)

#não fiz um rand de valores fiquei com preguiça vai assim chumbado
if __name__ == "__main__":
	dados = [170, 45, 75, 90, 802, 24, 2, 66, 45, 0, 999]

	lista = Lista()
	lista.carregar_valores(dados)
	print("Original:")
	lista.exibir()

	lista.merge_sort()
	print("Merge Sort:")
	lista.exibir()

	lista.carregar_valores(dados)
	lista.quick_sort()
	print("Quick Sort:")
	lista.exibir()

	lista.carregar_valores(dados)
	lista.counting_sort()
	print("Counting Sort:")
	lista.exibir()

	lista.carregar_valores(dados)
	lista.radix_sort()
	print("Radix Sort:")
	lista.exibir()
