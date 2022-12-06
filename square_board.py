from linear_board import LinearBoard
from settings import BOARD_LENGTH
from list_utils import transpose, replace_matrix, displace_matrix, reverse_matrix

class SquareBoard():

    '''
    Representa un tablero cuadrado
    '''

    @classmethod
    def fromList(cls, list_of_lists):   #cls es una referencia a la propia clase, equivalente a self para los objetos.
        '''
        Transforma una lista de listas en una lista de LinearBoards
        '''
        board = cls() 
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board


    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)] 


    #dunders
    def __repr__(self):
        
        matrix = self.as_matrix()

        matrix = replace_matrix(matrix, lambda x : x == None, '-')

        transp = transpose(matrix)

        transp.reverse()

        tmp = '\n'
        for row in transp:
            for element in row:
                tmp = tmp + '\t' + element
            tmp = tmp + '\n'
        
        return f'<{self.__class__}: {tmp}>'
    
    def __len__(self):
        return len(self._columns)
        

    def is_full(self):
        '''
        True si todos los LinearBoards estan llenos
        '''
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
        

    def as_matrix(self):
        '''
        Devuelve una representación en forma de matriz, es decir, lista de listas
        '''
        return list(map(lambda b: b._column, self._columns))    
    #con as_matrix hacemos que con cada LinearBoard del Squareboard aplicamos una función que convierte cada 
    #LinearBoard en una lista, por tanto al aplicar map y luego list se genera una lista de listas.
    

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)


    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result


    def _any_horizontal_victory(self, char):
        #transponemos _columns
        transp = transpose(self.as_matrix()) 
        #creamos un tablero temporal con esa matriz transpuesta
        tmp = SquareBoard.fromList(transp)
        #comprobamos si tiene una victoria temporal
        return tmp._any_vertical_victory(char)

    #Implementando el esta función aplicamos transformaciones. Primero transformamos en matriz, luego creamos una transpuesta,
    #depsués creamos un tablero TEMPORAL basandones en esa matriz transpuesta. Ahora si podemos evaluar usando el metodo de
    #victoria vertical.

    def _any_rising_victory(self, char):
        #obtengo la representación matricial
        matrix = self.as_matrix()
        #invierto la matriz
        matrix = reverse_matrix(matrix)
        #si había victoria ascedente en la original, en la invertida hay descendente
        #creo un tablero temporal con la invertida
        tmp = SquareBoard.fromList(matrix)
        #evalua si hay victoria descendente
        return tmp._any_sinking_victory(char)


    def _any_sinking_victory(self, char):
        #obtengo la representacion matricial del tablero
        matrix = self.as_matrix()
        #se mete un displace_matrix
        matrix = displace_matrix(matrix)
        #si había victoria descedente, ahora es horizontal        
        #creo un tablero temporal con esa matriz desplazada
        tmp = SquareBoard.fromList(matrix)
        #si hay victoria horizontal, en la desplazada, entonces
        #en la original había una descendente.
        return tmp._any_horizontal_victory(char)

    
    




    