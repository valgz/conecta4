import pytest
from list_utils import *

def test_find_one():
    #Se le llama 'needle' (aguja), porque es lo que estamos buscando.
    needle = 1
    #Luego se crean varios casos de prueba. En el primero no hay needle,
    #en el segundo esta al principio, etc.
    none = [0, 0, 5, 's']
    beginning = [1, None, 9, 6, 0, 0]
    end = ['x', '0', 1]
    several = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]
    #Finalmente se prueba.
    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(beginning, needle)
    assert find_one(several, needle)

def test_find_n():
    #Evaluamos si en la lista dada [], 
    #esta el elemento y la contidad de veces (lo que esta fuera de los corchetes)
    assert find_n([2, 3, 4, 5, 6], 2, -1) == False
    assert find_n([1, 2, 3, 4, 5], 42, 2) == False
    assert find_n([1, 2, 3, 4, 5], 1, 2) == False
    assert find_n([1, 2, 3, 2, 4, 5], 2, 2)
    assert find_n([1, 2, 3, 4, 5, 4, 6, 4, 7, 4, 6], 4, 2)
    #Este ultimo caso tambien debe cumplirse por que es N ó MAS VECES.
    assert find_n([1, 2, 3, 4], 'x', 0)  == True

def test_find_streak():
    assert find_streak([1, 2, 3, 4, 5], 4, -1) == False
    assert find_streak([1, 2, 3, 4, 5], 42, 2) == False
    assert find_streak([1, 2, 3, 4], 4, 1)
    assert find_streak([1, 2, 3, 1, 2], 2, 3) == False
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 3)
    assert find_streak([5, 5, 5, 1, 2, 3, 4], 5, 3)
    assert find_streak([1, 2, 5, 5, 5, 3, 4], 5, 3)
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 4) == False