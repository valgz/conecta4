def find_one(list, needle):
    
    '''Devuelve true si encuentra una o mas ocurrencias de needle en list.'''
    
    return find_n(list, needle, 1)

def find_n(list, needle, n):
    
    '''
    Devuelve True si en list hay n o mas ocurrencias de needle
    False si hay menos o si n < 0
    '''
    
    #Si n > 0...
    if n >= 0:
        #Inicializamos el indice y el contador
        index = 0
        count = 0
        #Mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
            #Si lo enonctramos, actualizamos el contador.
            if needle == list[index]:
                count += 1
            #Avanzamos al siguiente elemento.
            index += 1
        #Devolvemos el resultado de comparar con n
        return count >= n
    else:
        return False

def find_streak(list, needle, n):
    ''' 
    Devuelve True si encuentra en list n o mas needle seguidos
    False, en cualquier otro caso
    '''
    #Si n >= 0
    if n >= 0:
        #Inicializo el indice, contador, indicador de racha
        index = 0
        count = 0
        streak = False
        #Mientras no haya encontrado a n seguidos y la lista no se haya acabado..
        while count < n and index < len(list):
            #Si lo encuentro, activo el indicador de rachas y actualizo el contador
            if needle == list[index]:
                streak = True
                count += 1
            #Si no lo encuentro, desactivo el indicador de racha y reinicio el contador.
            else:
                streak = False
                count = 0
            #Avanzo al siguiente elemento
            index += 1
        #Devolvemos el resultado de comparar el contador con n siempre y cuando estemos en racha.
        return count >= n and streak
    #Para valores de n < 0:
    else:
        return False
