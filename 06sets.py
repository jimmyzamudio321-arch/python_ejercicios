### Sets en Python ###

# 1. Definición y Declaración
# Se usa set() para crear un set vacío.
my_set = set()

# CUIDADO: Usar {} vacío crea un DICCIONARIO, no un set.
my_other_set = {}

print(type(my_set))        # Muestra: <class 'set'>
print(type(my_other_set))  # Muestra: <class 'dict'>

# Un set se define con llaves {} conteniendo elementos directos
my_other_set = {"Alex", "Garcia", 25}
print(type(my_other_set))  # Ahora sí es: <class 'set'>
print(len(my_other_set))   # Cantidad de elementos: 3


# 2. Inserción
# .add() añade elementos al set.
my_other_set.add("Demo")

# PROPIEDAD 1: NO ORDENADO
# Los sets no guardan una posición fija. El orden de impresión puede cambiar.
print(my_other_set)

# PROPIEDAD 2: NO ADMITE DUPLICADOS
# Si intentas añadir un elemento que ya existe, Python simplemente lo ignora.
my_other_set.add("Demo")
print(my_other_set)  # "Demo" sigue apareciendo una sola vez


# 3. Búsqueda (Pertenencia)
# La búsqueda con `in` es extremadamente rápida y eficiente en los sets
print("Garcia" in my_other_set)  # Salida: True
print("Pérez" in my_other_set)    # Salida: False


# 4. Eliminación
# .remove(valor) elimina un elemento específico
my_other_set.remove("Garcia")
print(my_other_set)

# .clear() vacía por completo el set
my_other_set.clear()
print(len(my_other_set))  # Salida: 0

# del borra la variable completa de la memoria
del my_other_set
# print(my_other_set)  # NameError: name 'my_other_set' is not defined


# 5. Transformación de Tipos
my_set = {"Alex", "Garcia", 25}

# Convertir un set a lista te permite acceder por índices,
# pero ten en cuenta que el orden inicial puede ser aleatorio.
my_list = list(my_set)
print(my_list)
print(my_list[0])  # Ahora sí permite acceder por índice

my_other_set = {"sql", "java", "Python"}


# 6. Operaciones Matemáticas de Conjuntos
# .union() une los elementos de dos o más sets (eliminando duplicados automáticamente)
my_new_set = my_set.union(my_other_set)

# Puedes encadenar varias uniones seguidas
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

# .difference() devuelve lo que está en el primer set pero NO en el segundo
print(my_new_set.difference(my_set))  # Devuelve solo: {'sql', 'java', 'Python'}