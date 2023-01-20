from lutador import Lutador

class Luta:

    def __init__(self, desafiado, desafiante, rounds) -> None:
        
        self.__desafiado = desafiado
        self.__desafiante = desafiante
        self.__rounds = rounds
        self.__aprovada = False

    
    
    def marcarLuta(self, l1, l2):

        categoria_l1 = l1.get_categorias()
        categoria_l2 = l2.get_categorias()

        assert categoria_l1 is not None, f"ERRO: Categoria não definida para {l1.get_nome()}"
        assert categoria_l2 is not None, f"ERRO: Categoria não definida para {l2.get_nome()}"
        
        if categoria_l1 == categoria_l2:
            self.aprovado = True
            print('Luta APROVADA')

        else:
            print('Luta inválida os participantes dever ser da mesma categoria')    
                             
        
        

    def luta(self):
            
        if self.aprovado == True:
            self.luta = range(0,3)
            if self.luta == 0:
                self.l1 = Lutador.ganharLuta()
                self.l2 = Lutador.perderLuta()

                print('********************************************')
                print()
                print('------------ E o VENCEDOR FOI --------------')
                print()
                print('********************************************')
            
            elif self.luta == 1:
                self.l2 = Lutador.ganharLuta()
                self.l1 = Lutador.perderLuta()

                print('********************************************')
                print()
                print('------------ E o VENCEDOR FOI --------------')
                print()
                print('********************************************')


            else:
                self.l1 = Lutador.empatarLuta()
                self.l2 = Lutador.empatarLuta()

                print('********************************************')
                print()
                print('------------ TEMOS UM EMPATE --------------')
                print()
                print('********************************************')



       

    def get_desafiado(self):

        return self.__desafiado

    def set_desafiado(self,desafiado):

        self.__desafiado = desafiado

    def get_desafiante(self):

        return self.__desafiante

    def set_desafiante(self, desafiante):

        self.__desafiante = desafiante

    
    def get_rounds(self):

        return self.__rounds

    def set_rounds(self, rounds):

        self.__rounds = rounds 

