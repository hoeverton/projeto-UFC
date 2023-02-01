from luta import Luta
from lutador import Lutador

##self,nome, nacionalidade, idade, altura, peso,  vitorias, derrotas, empates) -
l1 = Lutador('Eto', 'Brasileiro', 35, 1.88, 73, 3, 1, 2)
##l1.apresentar()
##l1.status()

l2 = Lutador('Lucy', 'Americano', '30', '1.90', 73, 4, 1, 1)

#l2.categoria = 'valor1'
#print(l2.categoria)
##l2.apresentar()
##print(l2.get_categorias())
##print(l2.get_peso())
##l2.status()
##l2.set_nome('Luccy') 
##l2.apresentar()

luta1 = Luta(l1,l2)
#luta1.marcarLuta()
luta1.luta()
l1.categorias()