class Lutador:

    def __init__(self,nome, nascionalidade, idade, altura, peso, vitorias, derrotas, empates) -> None:
        
        self.__nome = nome
        self.__nascionalidade = nascionalidade
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso
        
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empates = empates

        self.__categoria = None
        

    def apresentar(self):

       ##print('Pesando: {peso}, ele é {nacionalidade},tem {vitorias} vitorias, {derrotas} derrotas e {empates} Apresentammos o lutador {nome}')    
         print('Pesando {}Kg ele e {} tem {} vitorias, {} derrotas e {} empates '.format(self.__peso, self.__nascionalidade, self.__vitorias, self.__derrotas, self.__empates)) 
         print( 'Senhoras e Senhores com vcs ******** {} *******'.format(self.__nome))   
    
    def status(self):

        print('----------------------------------------------------------')
        print('                     CHEGOU HORA!!!!!!!             ')
        print('----------------------------------------------------------')
    def ganharLuta(self):

        self.__vitorias = self.__vitorias + 1

    def perderLuta(self):

        self.__derrotas = self.__derrotas + 1
        
    
    def empatarLuta(self):
        
        self.__empates = self.__empates + 1

    def get_nome(self):

        return self.__nome

    def set_nome(self,nome):

        self.__nome = nome    

    def get_nascionalidade(self):

        return self.__nacionalidade

    def set_nascionalidade(self,nascionalidade):

        self.__nascionalidade = nascionalidade       

    def get_idade(self):

        return self.__idade

    def set_idade(self,idade):

        self.__idade = idade    

    def get_altura(self):

        return self.__altura

    def set_altura(self,altura):

        self.__altura = altura

    def get_peso(self):

        return self.__peso

    def set_peso(self,peso):

        self.__nome = peso
        self.set_categoria() ## por hora sem parametro

    def get_categorias(self):

        return self.__categoria

    def set_categoria(self):

      if self.__peso < 52.2:
        self.__categoria = 'Inválido'
      elif self.__peso <= 70.3:
        self.__categoria = 'Leve'    
      elif self.__peso <= 83.9:
        self.__categoria = 'Médio'
      elif self.__peso <= 120.2:
        self.__categoria = 'Pesado'
      else: self.__categoria = 'Inválido'    

    def get_vitorias(self):

        return self.__vitorias

    def set_vitorias(self,vitorias):

        self.__vitorias = vitorias

    def get_empates(self):

        return self.__empates

    def set_empates(self,empates):

        self.__empates = empates    
        
    
        
   