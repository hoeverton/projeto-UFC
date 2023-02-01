from lutador import Lutador

class Luta:

    def __init__(self, l1, l2):
        
        self.__desafiado = l1
        self.__desafiante = l2
        self.__aprovada = False 
        

    
    
    def marcarLuta(self):

        categorias_l1 = self.__desafiado.get_categorias()
        categorias_l2 = self.__desafiante.get_categorias()
    

        if categorias_l1 != categorias_l2:
            self.__aprovada = True
            print('Luta APROVADA')

        else:
            print('Luta inválida os participantes dever ser da mesma categoria')    
                             
        
        

    def luta(self):
        
        if self.__aprovada == True:
            self.luta = range(0,3)
            
            if self.luta == 0:
                self.__desafiado.ganharLuta()
                self.__desafiante.perderLuta()

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

