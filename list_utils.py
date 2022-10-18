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


def first_elements(list_of_lists):
    '''
    Recibe una lista de listas y devuelve una lista 
    con los primeros elementos de la original
    '''
    return nth_elements(list_of_lists, 0)


def nth_elements(list_of_lists, position):
    '''
    Recibe una lista de listas y devuelve una lista 
    con los enesimos elementos de la original
    '''
    result = []
    for lst in list_of_lists:
        result.append(lst[position])
    return result


def transpose(matrix):
    '''
    Recibe una matriz y devuelve su transpuesta
    '''
    transposed = []
    for i in range(len(matrix[0])):
        sublist = nth_elements(matrix, i)
        transposed.append(sublist)
    return transposed


def displace(lst, distance, filler=None):
    res = ''
    if distance == 0:
        res = lst
    elif distance > 0:
        filling = [filler] * distance
        res = filling + lst
        res = res[:-distance]
    else:
        filling = [filler] * abs(distance)
        res = lst + filling
        res = res[abs(distance):]
    return res


def displace_matrix(m, filler=None):
    new_m = []
    for i in range(len(m)):
        new_m.append(displace(m[i], i - 1, filler))
    return new_m


def replace(lst, predicate, new_value):
    new_list = []
    for element in lst:
        if predicate(element):
            new_list.append(new_value)
        else:
            new_list.append(element)
    return new_list


def replace_matrix(matrix, predicate, new_element):
    accum = []
    for sublist in matrix:
        accum.append(replace(sublist, predicate, new_element))
    return accum


def reverse_list(l):
    return list(reversed(l))


def reverse_matrix(matrix):
    return list(map(lambda sublist: reverse_list(sublist), matrix))

    '''
    accum = []
    for sublist in matrix:
        accum.append(reverse_list(sublist))
    return accum
    '''