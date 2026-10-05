import math

while True:

    print(" CALCULADORA DE FIGURAS GEOMÉTRICAS")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Cubo")
    print("6. Cilindro")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        perimetro = 4 * lado
        area = lado ** 2
        print("\nRESULTADOS")
        print("Perímetro:", perimetro)
        print("Área:", area)

    elif opcion == "2":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        perimetro = 2 * (base + altura)
        area = base * altura
        print("\nRESULTADOS")
        print("Perímetro:", perimetro)
        print("Área:", area)

    elif opcion == "3":
        lado1 = float(input("Ingrese el lado 1: "))
        lado2 = float(input("Ingrese el lado 2: "))
        lado3 = float(input("Ingrese el lado 3: "))
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        perimetro = lado1 + lado2 + lado3
        area = (base * altura) / 2
        print("\nRESULTADOS")
        print("Perímetro:", perimetro)
        print("Área:", area)

    elif opcion == "4":
        radio = float(input("Ingrese el radio: "))
        perimetro = 2 * math.pi * radio
        area = math.pi * radio ** 2
        print("\nRESULTADOS")
        print("Perímetro:", round(perimetro, 2))
        print("Área:", round(area, 2))

    elif opcion == "5":
        lado = float(input("Ingrese el lado del cubo: "))
        volumen = lado ** 3
        print("\nRESULTADOS")
        print("Volumen:", volumen)

    elif opcion == "6":
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = math.pi * radio ** 2 * altura
        print("\nRESULTADOS")
        print("Volumen:", round(volumen, 2))

    elif opcion == "7":
        print("\nGracias por utilizar el programa.")
        break

    else:
        print("\nOpción no válida. Intente nuevamente.")
