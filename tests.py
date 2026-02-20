import exercises


# Ejericio 1
def test_custom_greating():
    print("\nEjercicio 1: \n")
    name = input("Ingresa un nombre: ")
    print("Nombre usado: " + name)
    print("Saludo:")
    exercises.custom_greating(name)


# Ejercicio 2
def test_sum_list():
    list = [1, 2, 3, 4]

    print(
        "\nEjercicio 2: \n"
        "Lista usada:" + str(list) + "\n"
        "Suma Total: " + str(exercises.sum_list(list))
    )


# Ejercicio 3
def test_count_tuple_element():
    tup = (1, 2, 2, 3)
    value = 2

    print(
        "\nEjercicio 3: \n"
        "Tupla usada: " + str(tup) + "\n"
        "Valor a contar: " + str(value) + "\n"
        "Veces que aparece: " + str(exercises.count_tuple_element(tup, value))
    )


# Ejercicio 4
def test_average_age():
    dict = {"Gabriel": 25, "Rozo": 31, "José": 19, "Oriana": 28, "Luis": 42}

    print(
        "\nEjercicio 4: \n"
        "Diccionario usado:" + str(dict) + "\n"
        "Edad Promedio: " + str(exercises.age_average(dict))
    )


# Ejercicio 5
def test_get_pairs():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(
        "\nEjercicio 5: \n"
        "Lista usada: " + str(list) + "\n"
        "Pares: " + str(exercises.get_pairs(list))
    )


# Ejercicio 6
def test_invert_tuple():
    tuple = (1, 2, 3, 4)

    print(
        "\nEjercicio 6: \n"
        "Tupla usada: " + str(tuple) + "\n"
        "Tupla invertida: " + str(exercises.invert_tuple(tuple))
    )


# Ejercicio 7
def test_create_dic_with_vect():
    list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    print(
        "\nEjercicio 7: \n"
        "Lista usada: " + str(list) + "\n"
        "Diccionario con conteo de elementos: "
        + str(exercises.create_dic_with_vect(list))
    )


# Ejercicio 8
def test_apply_discount():
    products = {
        "Kilo de Papa": 3200,
        "Cartor de Huevos AAA": 10000,
        "Litro de Aceite de Oliva": 4500,
    }

    print("\nEjercicio 8: \nDiccionario usado:\n" + str(products) + "\n")

    exercises.apply_discount(products)
    print("Diccionario con Descuento Aplicado:\n" + str(products))


# Ejercicio 9
def test_get_approved_students():
    students = [
        {"nombre": "Carlos", "nota": 3.5},
        {"nombre": "Luna", "nota": 5.0},
        {"nombre": "David", "nota": 2.8},
        {"nombre": "Sebas", "nota": 4.0},
        {"nombre": "Steven", "nota": 3.9},
    ]

    print(
        "\nEjercicio 9: \n"
        "Lista de estudiantes:\n" + str(students) + "\n\n"
        "Estudiantes Aprobados:\n" + str(exercises.get_approved_students(students))
    )


# Ejercicio 10
def test_combine_lists():
    pedro_daughters = ["Pata", "Peta", "Pita", "Pota", "Ana"]
    pedro_daughters_pets = [
        "Pato",
        "Morrocoy",
        "Pez Luna",
        "Ornitorrinco",
        "Anaconda",
    ]

    print(
        "\nEjercicio 10: \n"
        "Lista con las Hijas de Pedro:\n" + str(pedro_daughters) + "\n\n"
        "Lista con las Mascotas de las Hijas de Pedro:\n"
        + str(pedro_daughters_pets)
        + "\n\n"
        "Diccionario con las Combinacion de las listas:\n"
        + str(exercises.combine_lists(pedro_daughters, pedro_daughters_pets))
    )


def run_tests():
    # Numero 1
    test_custom_greating()

    # Numero 2
    test_sum_list()

    # Numero 3
    test_count_tuple_element()

    # Numero 4
    test_average_age()

    # Numero 5
    test_get_pairs()

    # Numero 6
    test_invert_tuple()

    # Numero 7
    test_create_dic_with_vect()

    # Numero 8
    test_apply_discount()

    # Numero 9
    test_get_approved_students()

    # Numero 10
    test_combine_lists()


run_tests()
