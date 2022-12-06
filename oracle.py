from enum import Enum, auto

class ColumnClassification(Enum):

    FULL = auto()
    MAYBE = auto()


class ColumnRecommendation():

    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __eq__(self, other):
        #Si son de clases distintas, son distintos.
        if not isinstance(other, self.__class__):
            return False
        #si son de la misma clase, comparo las propiedades de uno y otro.
        else:
            return (self.index, self.classification) == (other.index, other.classification)

    def __hash__(self):
        return hash((self.index, self.classification))



class BaseOracle():


    def get_recommendation(self, board, player):
        '''
        Return a list of column recommendations
        '''

        recommendations = []
        for i in range(len(board)):
            recommendations.append(self._get_column_recommendation(board, i, player))
        return recommendations


    def _get_column_recommendation(self, board, index, player):
        '''
        Classifies a column as either FULL or MAYBE and returns an ColumnRecommendation
        '''

        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL
        
        return ColumnRecommendation(index, classification) 

