def promn(notas):
    return sum(notas) / len(notas)


print("promedio de notas")
notas = []
notas.append(float(input("ingrese su primera nota: ")))
notas.append(float(input("ingrese su segunda nota: ")))
notas.append(float(input("ingrese su tercera nota: ")))
promedio_notas = promn(notas)
if promedio_notas >= 3.0:
    print(f"El estudiante aprobo con un promedio de {promedio_notas} ")
else:
    print(f"El estudiante reprobo con un promedio de {promedio_notas} ")





