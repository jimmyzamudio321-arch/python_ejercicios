### Diccionarios en Python ###

# 1. Definición y Declaración
# Se pueden declarar usando dict() o llaves {} vacías
my_dict = dict()
my_other_dict = {}

print(type(my_dict))        # Muestra: <class 'dict'>
print(type(my_other_dict))  # Muestra: <class 'dict'>

# Un diccionario guarda elementos en pares "Clave": "Valor" (Key: Value)
my_other_dict = {
    "Nombre": "Alex",
    "Apellido": "Garcia",
    "Edad": 25,
    1: "Python"             # Las claves también pueden ser números
}

# Los valores pueden ser de cualquier tipo (strings, ints, sets, etc.)
my_dict = {
    "Nombre": "Alex",
    "Apellido": "Garcia",
    "Edad": 25,
    "Lenguajes": {"Python", "SQL"}, # Valor de tipo Set
    1: 1.73
}

print(my_other_dict)
print(my_dict)

# len() devuelve la cantidad de claves (pares clave-valor) que contiene
print(len(my_other_dict)) # Salida: 4
print(len(my_dict))       # Salida: 5


# 2. Búsqueda y Acceso
# Se accede al VALOR mediante su CLAVE entre corchetes [clave]
print(my_dict[1])         # Muestra: 1.73
print(my_dict["Nombre"])   # Muestra: "Alex"

# CUIDADO: El operador `in` busca en las CLAVES, NO en los valores
print("Garcia" in my_dict)   # Salida: False (porque "Garcia" es un valor, no una clave)
print("Apellido" in my_dict)  # Salida: True (porque "Apellido" sí es una clave)


# 3. Inserción
# Para añadir un nuevo elemento, asignas un valor a una clave que NO exista aún
my_dict["Zona"] = "Centro"
print(my_dict)


# 4. Actualización
# Si asignas un valor a una clave que YA existe, se sobrescribe su contenido
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])  # Salida: "Pedro"


# 5. Eliminación
# del elimina un par clave-valor específico usando su clave
del my_dict["Zona"]
print(my_dict)


# 6. Otras Operaciones y Métodos Útiles

# .items() devuelve una lista de tuplas con cada par (clave, valor)
print(my_dict.items())

# .keys() devuelve únicamente el listado de claves
print(my_dict.keys())

# .values() devuelve únicamente el listado de valores
print(my_dict.values())

# dict.fromkeys() crea un nuevo diccionario usando una lista/tupla para las claves.
# Por defecto, asigna None a todos los valores si no se especifica uno.
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)  # {'Nombre': None, 1: None, 'Piso': None}

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Si le pasas otro diccionario como base, copia solo sus claves (con valor None)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Si agregas un segundo argumento, asigna ese valor por defecto a TODAS las claves
my_new_dict = dict.fromkeys(my_dict, "Demo")
print(my_new_dict)  # Todas las claves tendrán como valor "Demo"


# 7. Conversión entre Tipos
my_values = my_new_dict.values()
print(type(my_values)) # Tipo: <class 'dict_values'>

print(my_new_dict.values())

# Truco para obtener los valores únicos usando dict.fromkeys y convirtiendo a lista
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

# Al convertir un diccionario a Tupla o Set, se obtienen únicamente las CLAVES
print(tuple(my_new_dict)) # Tupla con las claves de my_new_dict
print(set(my_new_dict))   # Set con las claves de my_new_dict