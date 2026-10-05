### Tuplas en Python ###

# 1. Definición y Declaración
# A diferencia de las listas [], las tuplas se definen con paréntesis ()
my_tuple = tuple()
my_other_tuple = ()

# Tupla con datos de ejemplo (edad, estatura, nombre, apellido, apodo)
my_tuple = (25, 1.77, "Alex", "Garcia", "Demo")
my_other_tuple = (17, 60, 30)

print(my_tuple)
print(type(my_tuple))  # Muestra el tipo: <class 'tuple'>


# 2. Acceso a elementos y búsqueda
# El acceso mediante índices funciona exactamente igual que en las listas
print(my_tuple[0])   # Muestra 17 (primer elemento)
print(my_tuple[-1])  # Muestra "Demo" (último elemento)

# Intentar acceder a un índice que no existe genera un error:
# print(my_tuple[5])  # IndexError
# print(my_tuple[-6]) # IndexError

# .count(x) cuenta cuántas veces aparece un elemento exacto en la tupla
print(my_tuple.count("Alex"))  # Salida: 1

# .index(x) busca un valor y devuelve la posición (índice) de su PRIMERA aparición
print(my_tuple.index("Garcia")) # Salida: 3
print(my_tuple.index("Alex"))   # Salida: 2 (encuentra la primera coincidencia)

# INMUTABILIDAD: A diferencia de una lista, las tuplas NO se pueden modificar una vez creadas
# my_tuple[1] = 1.80  # TypeError: 'tuple' object does not support item assignment


# 3. Concatenación
# Se pueden sumar dos tuplas para generar una NUEVA tupla
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# 4. Subtuplas (Slicing)
# Extrae un rango de elementos [inicio:fin_no_incluido] creando una nueva tupla
print(my_sum_tuple[3:6])


# 5. Conversión a Lista para Modificar (Truco de mutabilidad)
# Si realmente necesitas modificar una tupla, primero la conviertes a lista con list()
my_tuple = list(my_tuple)
print(type(my_tuple))  # Cambia a: <class 'list'>

# Ahora que es una lista, ya permite modificaciones:
my_tuple[4] = "Demo"       # Cambiamos el 5to elemento por "Demo"
my_tuple.insert(1, "Azul") # Insertamos "Azul" en la posición 1

# Finalmente la reconvertimos a tupla con tuple()
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))  # Vuelve a ser: <class 'tuple'>


# 6. Eliminación

# NO se puede borrar un elemento individual de una tupla:
# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion

# Sí se puede eliminar la variable completa de la memoria usando del:
del my_tuple

# Si intentas imprimirla tras borrarla, dará error porque ya no existe:
# print(my_tuple)  # NameError: name 'my_tuple' is not defined