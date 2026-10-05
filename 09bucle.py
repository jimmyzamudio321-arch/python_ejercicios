
### BUCLES (LOOPS) ###

# ==========================================
# 1. BUCLE WHILE
# ==========================================
# El bucle 'while' repite un bloque de código mientras una condición sea verdadera (True).

# Ejemplo 1: Incremento constante y cláusula 'else'
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2  # Incrementamos de 2 en 2 para evitar un bucle infinito
else:  
    # El bloque 'else' en un bucle 'while' es opcional.
    # Se ejecuta ÚNICAMENTE cuando la condición principal se vuelve falsa de forma natural.
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


# Ejemplo 2: Interrupción anticipada con 'break'
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break  # 'break' rompe inmediatamente el bucle. Cuando se usa 'break', el 'else' (si lo hubiera) NO se ejecuta.
    print(my_condition)

print("La ejecución continúa")


# ==========================================
# 2. BUCLE FOR
# ==========================================
# El bucle 'for' se utiliza para iterar sobre una secuencia o colección (listas, tuplas, conjuntos, diccionarios, etc.).

# --- Iterando sobre una Lista ---
# Las listas mantienen el orden de los elementos.
my_list = [17, 20, 8200, 4600, 2026]

for element in my_list:
    print(element)


# --- Iterando sobre una Tupla ---
# Las tuplas son colecciones ordenadas e inmutables.
my_tuple = (25, 1.75, "Alex", "Garcia", "Alex")

for element in my_tuple:
    print(element)


# --- Iterando sobre un Set (Conjunto) ---
# Los sets son colecciones desordenadas de elementos únicos. El orden de impresión puede variar.
my_set = {"Alex", "Garcia", 25, "Bogotá"}

for element in my_set:
    print(element)


# --- Iterando sobre un Diccionario ---
# Al iterar directamente sobre un diccionario, Python recorre sus CLAVES (keys), no los valores.
my_dict = {
    "Nombre": "Alex",
    "Apellido": "Garcia",
    "Edad": 25,
    "Especialidad": "ADSO",
    1: "Python"
}

# Ejemplo 3: Control con 'break' en un diccionario
for element in my_dict:
    print(element)  # Imprime la clave actual
    if element == "Edad":
        break  # Detiene la iteración al llegar a la clave "Edad"
else:
    # Este 'else' NO se ejecutará porque el bucle se interrumpió con 'break'.
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")


# Ejemplo 4: Control con 'continue' en un diccionario
for element in my_dict:
    print(element)
    if element == "Edad":
        continue  # 'continue' salta el resto del código del bloque actual y pasa directamente a la siguiente iteración.
    print("Se ejecuta")
else:
    # Este 'else' SÍ se ejecuta porque el bucle terminó de recorrer todo el diccionario sin encontrar ningún 'break'.
    print("El bucle for para el diccionario ha finalizado")