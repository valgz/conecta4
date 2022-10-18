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

def test_first_elements():
    original = [[0, 7, 3], [4, 0, 1]]

    assert first_elements(original) == [0, 4]
    assert first_elements([[2, 3, 5], [1, 9, 3], [0, 5, 6]]) == [2, 1, 0]
    assert first_elements([[9, 8], [2, 1], [7, 6]]) == [9, 2, 7]


def test_transpose():
    a = [[2, 3, 5], [1, 9, 3], [0, 5, 6]]
    b = [['a', 'x'], ['b', 'y']]
    original = [[0, 7, 3], [4, 0, 1]]
    transposed = [[0,4], [7, 0], [3, 1]]
    
    assert transpose(a) == [[2, 1, 0], [3, 9, 5], [5, 3, 6]]
    assert transpose(b) == [['a', 'b'], ['x', 'y']]
    assert transpose(original) == transposed
    assert transpose(transpose(original)) == original


def test_zero_distance_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [4, 5], ['x', 'o', 'c']

    assert displace([], 0) == []
    assert displace(l1, 0) == l1
    assert displace(l2, 0) == l2
    assert displace(l3, 0) == l3 


def test_positive_distance_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [[4, 5], ['x', 'o', 'c']]
    l4 = [9, 6, 5]

    assert displace([], 2) == []
    assert displace(l1, 2) == [None, None, 1, 2, 3, 4]
    assert displace(l2, 3, '-') == ['-']
    assert displace(l3, 1, '#') == ['#', [4, 5]]
    assert displace(l4, 3, 0) == [0, 0, 0]


def test_negative_distance_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [[4, 5], ['x', 'o', 'c']]
    l4 = [9, 6, 5]

    assert displace([], -2) == []
    assert displace(l1, -2) == [3, 4, 5, 6, None, None]
    assert displace(l2, -3, '-') == ['-']
    assert displace(l3, -1, '#') == [['x', 'o', 'c'], '#']
    assert displace(l4, -3, 0) == [0, 0, 0]


def test_reverse_list():
    assert reverse_list([]) == []
    assert reverse_list([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]


def test_reverse_matrix():
    assert reverse_matrix([]) == []
    assert reverse_matrix([[0, 1, 2, 3], [0, 1, 2, 3]]) == [
        [3, 2, 1, 0], [3, 2, 1, 0]]
    