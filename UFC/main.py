from luta import Luta
from lutador import Lutador

##self,nome, nacionalidade, idade, altura, peso,  vitorias, derrotas, empates) -
l1 = Lutador('Eto', 'Brasileiro', 35, 1.88, 75, 3, 1, 2)
##l1.apresentar()
##l1.status()

l2 = Lutador('Lucy', 'Americano', '30', '1.90', 73, 4, 1, 1)
##l2.apresentar()
##l2.status()
##l2.set_nome('Luccy')
##l2.apresentar()

luta = Luta(l1,l2,3)
luta.marcarLuta(l1,l2)