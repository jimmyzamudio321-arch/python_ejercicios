### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Alex", "Garcia", 25
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1] #invierte el texto por completo (slicing)
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) #convierte solo la primera letra en mayuscula y el resto en minusculas
print(language.upper()) #convierte todo el texto a mayussculas
print(language.count("t")) #cuenta cuantas veces aparece el caracter "t" en el texto
print(language.isnumeric()) #Devuelve True si todo el texto es un numero, de lo contrario False
print("1".isnumeric()) #Devuelve True porque la cadena contiene un caracter numerico
print(language.lower()) #Convierte todo el texto a minusculas
print(language.lower().isupper()) #Convierte a minusculas y luego evalua si esta en mayusculas(siempre dara False)
print(language.startswith("Py")) #Devuelve True si el texto comienza con los caracteres exactos "Py"
print("Py" == "py")  # No es lo mismo