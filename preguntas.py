"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    Data = open('/content/data.csv','r')
    file = Data.readlines()
    data_1 = [i.replace('\n','') for i in file]
    data_1 = [i.replace('"','') for i in file]
    data_1 = [i.split('\t') for i in file]

    suma = 0
    for i in data_1:
        suma = suma + (int(i[1]))
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    Data = open('/content/data.csv','r')
    file = Data.readlines()
    data_1 = [i.replace('\n','') for i in file]
    data_2 = [i.replace('"','') for i in data_1]
    data_3 = [i.split('\t') for i in data_2]

    dictionary = {}
    for i in data_3:
        if i[0] in dictionary.keys():
            dictionary[i[0]] = dictionary[i[0]] + 1
        else:
            dictionary[i[0]] = 1

    lista_dict = sorted(list(zip(dictionary.keys(), dictionary.values())))
    return lista_dict


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    
    """
    Data = open('/content/data.csv','r')
    file = Data.readlines()
    data_1 = [i.replace('\n','') for i in file]
    data_2 = [i.replace('"','') for i in data_1]
    data_3 = [i.split('\t') for i in data_2]

    for i in data_3:
        data_3 = [[row[0], int(row[1])] for row in data_3]
        data_list = sorted(data_3, key=None, reverse=False)

    dictionary = {}
    for i in data_list:
        if i[0] in dictionary:
            dictionary[i[0]] = dictionary[i[0]]+i[1]
        else:
            dictionary[i[0]] = i[1]

    dictionary = [(key, value) for key,value in dictionary.items()]
    return dictionary


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    Data = open('/content/data.csv','r')
    file = Data.readlines()
    data_1 = [i.replace('\n','') for i in file]
    data_2 = [i.split('\t') for i in data_1]
    data_3 = [i[2].split('-') for i in data_2]

    dictionary = {}

    for n in sorted(i[2] for i in data_3):
        if n in dictionary.keys():
            dictionary[n] = dictionary[n] + 1
        else:
            dictionary[n] = 1

    lista = list(dictionary.items())
    return lista


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    Data = open('/content/data.csv','r')
    file = Data.readlines()
    data_1 = [i.replace('\n','') for i in file]
    data_2 = [i.replace('"','') for i in data_1]
    data_3 = [i.split('\t') for i in data_2]

    dictionary = {}
    for i in data_3:
        if i[0] in dictionary.keys():
            dictionary[i[0]].append(int(i[1]))
        else:
            dictionary[i[0]] = [int(i[1])]

    resultado = [(a,max(dictionary[a]),min(dictionary[a])) for a in dictionary.keys()]
    resultado = sorted(resultado, key=lambda tup: tup[0])
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]
    
    data_lista = []
    for a in [i[4].split(',') for i in data]:
        data_lista.extend(a)
    
    dictionary = {}
    for b in data_lista:
        key = b.split(':')[0]
        value = b.split(':')[1]
        if key in dictionary.keys():
            dictionary[key].append(int(value))
        else:
            dictionary[key] = [int(value)]
    data_result = [(key, min(dictionary[key]), max(dictionary[key])) for key in dictionary.keys()]
    sorted(data_result, key=lambda tup: tup[0])
    return sorted(data_result, key=lambda tup: tup[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]
    data = [[row[1], row[0]] for row in data]

    dictionary = {}

    for i in data:
        if i[0] in dictionary:
            dictionary[i[0]] = dictionary[i[0]]+','+i[1]
        else:
            dictionary[i[0]] = i[1]
    tupla_data = sorted(tuple((int(key), value.split(',')) for key, value in dictionary.items()))

    for i in tupla_data:
        print(i)
    return tupla_data


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]

    dictionary = {}
    for i in data:
        key = int(i[1])
        if key in dictionary.keys():
            dictionary[key].append(i[0])
        else: 
            dictionary[key] = [i[0]]
    
    data_result = sorted(list(dictionary.items()))
    data_result = [(b[0], sorted(list(set(b[1])))) for b in data_result]
    return data_result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split('\t') for row in data]
    data = [row[4] for row in data]
    data = [row.split(',') for row in data]
    data = [row for rowx in data for row in rowx]
    data = [row.replace(":", ',') for row in data]
    data = sorted([row.split(',') for row in data], key=None, reverse=False)

    dictionary = {}
    for i in data:
        if i[0] in dictionary:
            dictionary[i[0]] = dictionary[i[0]] + 1
        else:
            dictionary[i[0]] = 1
    return dictionary


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]
    
    data_1 = [(row[0],len(row[3].split(',')),len(row[4].split(',')))for row in data]
    return data_1


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]

    dictionary = {}
    for i in data:
        for a in i[3].split(','):
            if a in dictionary.keys():
                dictionary[a] = dictionary[a] + int(i[1])
            else:
                dictionary[a] = int(i[1])
    
    data_result = list(dictionary.items())
    return dict(sorted(data_result, key=lambda tup: tup[0]))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.replace('"', '') for i in data]
    data = [i.split('\t') for i in data]

    diccionario = {}
    for i in data:
        c = i[4].split(',')
        if i[0] in diccionario.keys():
            diccionario[i[0]] = diccionario[i[0]] + sum([int(e.split(':')[1]) for e in c])
        else:
            diccionario[i[0]] = sum([int(e.split(':')[1]) for e in c])
    resultado = list(diccionario.items())
    resultado = dict(sorted(resultado, key=lambda tup: tup[0]))
    return resultado
