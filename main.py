from VetorNaoOrdenado import VetorNaoOrdenado

if __name__ == '__main__':
  vetor = VetorNaoOrdenado(5)
  vetor.imprime()
  vetor.insere(2)
  vetor.insere(3)
  vetor.insere(8)
  vetor.insere(7)
  vetor.insere(11)
  vetor.imprime()
  vetor.insere(4)
  print(vetor.pesquisar(3))
  vetor.excluir(2)
  vetor.imprime()