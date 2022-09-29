import pytest
from linear_board  import *
from settings import BOARD_LENGTH, VICTORY_STREAK

def test_empty_board():
    empty = LinearBoard()
    assert empty != None #Primero verificar que el objeto existe.
    assert empty.is_full() == False #Luego verifica que el tablero no esta lleno.
    assert empty.is_victory('x') == False #Verifica que no hay victoria.

def test_add():
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STREAK):
        b.add('x')
    
    assert b.is_victory('o') == False
    assert b.is_victory('x') == True

def test_tie():
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x', 'o')

def test_add_to_full():
    full = LinearBoard()
    for i in range(BOARD_LENGTH):
        full.add('x')

    full.add('x')
    assert full.is_full()