### Listas en Python ###

# 1. Definición y Declaración
# Se pueden crear listas usando la función list() o corchetes []
my_list = list()
my_other_list = []

print(len(my_list))  # len() devuelve la cantidad de elementos (aquí 0)

# Las listas pueden guardar números, texto, decimales o cualquier tipo de dato
my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))  # Salida: 7

# Lista con datos de ejemplo: edad (25), estatura (1.73), nombre (Alex), apellido (Garcia)
my_other_list = [25, 1.73, "Alex", "Garcia"]

print(type(my_list))       # Muestra el tipo de dato: <class 'list'>
print(type(my_other_list))


# 2. Acceso a elementos e índices
# Los índices positivos empiezan en 0 desde la izquierda
print(my_other_list[0])  # Muestra 25 (primer elemento)
print(my_other_list[1])  # Muestra 1.73

# Los índices negativos cuentan desde atrás (-1 es el último elemento)
print(my_other_list[-1]) # Muestra "Garcia"
print(my_other_list[-4]) # Muestra 25

# .count(x) cuenta cuántas veces aparece un elemento específico
print(my_list.count(30)) # Salida: 2

# Intentar acceder a un índice fuera de rango genera un error (IndexError):
# print(my_other_list[4]) 
# print(my_other_list[-5])

# .index(x) busca un valor y devuelve el número de su índice
print(my_other_list.index("Alex")) # Salida: 2

# Desempaquetado (Unpacking): asigna cada elemento de la lista a una variable en orden
age, height, name, surname = my_other_list
print(name)  # Muestra "Alex"

# Asignación manual usando los índices de la lista
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)   # Muestra 25


# 3. Concatenación
# El operador + une dos listas en una nueva
print(my_list + my_other_list)
# La resta (-) NO está permitida entre listas: print(my_list - my_other_list)


# 4. Modificación de Listas: Inserción, Actualización y Eliminación

# .append() añade un nuevo elemento AL FINAL de la lista
my_other_list.append("Demo")
print(my_other_list)

# .insert(índice, valor) agrega un elemento en la posición exacta que le indiques
my_other_list.insert(1, "Rojo")
print(my_other_list)

# Modificar directamente el valor de una posición usando su índice
my_other_list[1] = "Azul"
print(my_other_list)

# .remove(valor) elimina la primera aparición del valor especificado
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) # Elimina solo el primer 30 que encuentra
print(my_list)

# .pop() elimina y retorna el ÚLTIMO elemento de la lista
print(my_list.pop()) # Muestra el último elemento eliminado (17)
print(my_list)

# .pop(índice) también puede eliminar un elemento en una posición específica
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# del elimina un elemento por su índice directamente sin retornar su valor
del my_list[2]
print(my_list)


# 5. Operaciones Útiles con Listas

# .copy() crea una copia independiente de la lista en memoria
my_new_list = my_list.copy()

# .clear() vacía la lista por completo
my_list.clear()
print(my_list)     # Lista vacía: []
print(my_new_list) # Mantiene los elementos gracias a .copy()

# .reverse() invierte el orden de los elementos
my_new_list.reverse()
print(my_new_list)

# .sort() ordena los elementos de menor a mayor (o por orden alfabético)
my_new_list.sort()
print(my_new_list)


# 6. Slicing (Sublistas)
# Permite obtener un fragmento de la lista usando el sintaxis [inicio:fin]
# Nota: el índice final no se incluye en el resultado
print(my_new_list[1:3])


# 7. Tipado Dinámico
# En Python, las variables pueden cambiar de tipo en cualquier momento
my_list = "Hola Python"
print(my_list)
print(type(my_list)) # Pasa de ser una lista a un string (<class 'str'>)







