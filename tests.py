import exercises

# Ejercicio 2
def test_sum_list():
    list = [1, 2, 3, 4]

    print("\nEjercicio 2: \n" \
        "Lista usada:" + str(list) + "\n" \
        "Suma Total: " + str(exercises.sum_list(list)))
    

# Ejercicio 4
def test_average_age():
    dict = {
        "Juan": 25,
        "María": 31,
        "Carlos": 19,
        "Ana": 28,
        "Luis": 42
    }

    print("\nEjercicio 4: \n" \
        "Diccionario usado:" + str(dict) + "\n" \
        "Edad Promedio: " + str(exercises.age_average(dict)))

# Ejercicio 6
def test_invert_tuple():
    tuple = (1, 2, 3, 4)

    print("\nEjercicio 6: \n" \
        "Tupla usada: " + str(tuple) + "\n" \
        "Tupla invertida: " + str(exercises.invert_tuple(tuple)))

# Ejercicio 8
def test_apply_discount():
    products = {
        "Kilo de Papa": 3200,
        "Cartor de Huevos AAA": 10000,
        "Litro de Aceite de Oliva": 4500
    }

    print("\nEjercicio 8: \n" \
        "Diccionario usado:\n" + str(products) + "\n")
    
    exercises.apply_discount(products)
    print("Diccionario con Descuento Aplicado:\n" + str(products))

# Ejercicio 10
def test_combine_lists():
    pedro_daughters = ["Pata", "Peta", "Pita", "Pota", "Ana"]
    pedro_daughters_pets = ["Ornitorrinco", "Chihuahua", "Pez Dorado", "Gato Siames", "Anaconda"]

    print("\nEjercicio 10: \n" \
        "Lista con las Hijas de Pedro:\n" + str(pedro_daughters) + "\n\n" \
        "Lista con las Mascotas de las Hijas de Pedro:\n" + str(pedro_daughters_pets) + "\n\n" \
        "Diccionario con las Combinacion de las listas:\n" + str(exercises.combine_lists(pedro_daughters, pedro_daughters_pets)))

def run_tests():

    test_sum_list()
    
    test_average_age()
    
    test_invert_tuple()
    
    test_apply_discount()

    test_combine_lists()


run_tests()