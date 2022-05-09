import numpy as np

class VetorNaoOrdenado:
  # Construtor
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Cria um array vazio de inteiros
    self.valores = np.empty(self.capacidade, dtype=int) 

  # Método para imprimir os valores - O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print("Vetor vazio!")
    else:
      for i in range(self.ultima_posicao + 1):
        print(f'[{i}] - {self.valores[i]}') 
        #print(self.valores)
        
  # Método para inserir um valor no vetor - O(1)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida!')
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor

  # Método para pesquisar valor  - O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1

  # Metodo para excluir um valor - O(n) 
  def excluir(self, valor):
    # Encontra a posicao do valor, usando o metodo pesquisar já implementado
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1 # Se nao encontrou retorna -1
    else:
      # Faz o remanejamento dos valores
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
      self.ultima_posicao -= 1