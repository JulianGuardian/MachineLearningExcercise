"""
TALLER 2: EJERCICIOS DE PYTHON

OBJETIVO DE LA ACTIVIDAD
Que los estudiantes se familiaricen con las funciones vistas sobre python:
"""

"""
1.Crea una función llamada saludo_personalizado que reciba un nombre como parámetro y
muestre un saludo.
Entrada: "Ana"
Salida: Hola Ana, bienvenida al curso.
"""

def custom_greating(name):
    print(f"Hola {name}, ¿cómo estás el día de hoy?")

"""
2.Crea una función suma_lista que reciba una lista de números y devuelva la suma total.
Entrada: [1, 2, 3, 4]
Salida: 10
"""

def sum_list(numbers: list[int]):
    total = 0

    for num in numbers:
        total += num

    return total

"""
3.Crea una función contar_elemento que reciba una tupla y un valor, y devuelva cuántas veces
aparece ese valor.
Entrada: (1,2,2,3), 2
Salida: 2
"""

def count_tuple_element(tup: tuple, value):
    count = 0

    for element in tup:
        if element == value:
            count += 1

    return count

"""
4.Dado un diccionario que almacene nombres y edades, crea una función que reciba el
diccionario y devuelva la edad promedio.
"""

def age_average(ages: dict[str, int]):
    total = 0

    for age in ages.values():
        total += age

    return total / len(ages)

"""
5.Crea una función obtener_pares que reciba una lista y devuelva una nueva lista solo con los
números pares.
Entrada: [1,2,3,4,5,6]
Salida: [2,4,6]
"""
def get_pairs(numbers: list[int]):
    pairs = []

    for num in numbers:
        if num % 2 == 0:
            pairs.append(num)

    return pairs


"""
6.Crea una función que reciba una tupla y devuelva una nueva tupla invertida.
• Entrada: (1,2,3)
• Salida: (3,2,1)
"""

def invert_tuple(tup: tuple):
    return tup[::-1]

"""
7.Crea una función que reciba una lista y devuelva un diccionario donde:
• La clave sea el elemento
• El valor sea la cantidad de veces que aparece
Entrada: [1,2,2,3,1,1]
Salida: {1:3, 2:2, 3:1}
"""

def create_dic_with_vect(list: list):
    dic = {}

    for element in list:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1

    return dic

"""
8.Crea una función que reciba un diccionario de productos y precios, y aplique un descuento del
10% a todos los valores.
"""

def apply_discount(prods: dict[str, float]):
    for prod in prods:
        prods[prod] *= 0.9

"""
9.Crea una función que:
Reciba una lista de diccionarios con estructura:
Devuelva una lista con los nombres de los estudiantes aprobados (nota >= 4.0).
"""

def get_approved_students(students: list[dict[str, float]]):
    approved_students = []

    for student in students:
        if student["nota"] >= 4.0:
            approved_students.append(student["nombre"])

    return approved_students


"""
10.Crear una función que reciba dos listas:
Y devuelve un diccionario combinandolas:
"""

def combine_lists(keys: list, values: list):
    return dict(zip(keys, values))