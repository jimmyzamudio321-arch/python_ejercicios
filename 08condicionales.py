### Condicionales (Conditionals) ###

# 1. Condicional simple (if)
# Evalúa si una condición es verdadera (True). Si lo es, ejecuta el bloque indentado.
my_condition = False

if my_condition:  # Es lo mismo que escribir: if my_condition == True:
    print("Se ejecuta la condición del if")  # No se ejecuta porque es False


# Reasignamos valor a la variable (5 * 5 = 25)
my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")  # No se ejecuta (25 != 10)


# 2. Control de flujo compuesto (if, elif, else)
# Permite evaluar múltiples condiciones en secuencia:
# - `if`: Primera condición a comprobar.
# - `elif`: (Else If) Se evalúa si el `if` anterior fue False.
# - `else`: Se ejecuta únicamente si NINGUNA de las condiciones anteriores se cumplió.

if my_condition > 10 and my_condition < 20:
    # Usa el operador lógico 'and': ambas condiciones deben ser True
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    # Esta condición es True (25 == 25), por lo que se ejecuta este bloque y finaliza la estructura
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")  # Código fuera de la estructura condicional


# 3. Inspección de valor y valores "Truthy / Falsy"
# En Python, ciertos valores actúan como False en un condicional:
# (cadenas vacías "", el número 0, listas/sets/dicts vacíos [], {}, None).

my_string = ""

# El operador `not` invierte el valor booleano:
# `not my_string` es True porque la cadena está vacía ("")
if not my_string:
    print("Mi cadena de texto es vacía")

# Comparación directa de cadenas de texto
my_string = "Mi cadena de texto"

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")  # No se ejecuta porque son distintas