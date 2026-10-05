def suma(num1, num2):
    print(f"la suma entre {num1} y {num2} es: ", num1 + num2)

def resta(num1, num2):
    print(f"la resta entre {num1} y {num2} es: ", num1 - num2)

def multiplicacion(num1, num2):
    print(f"la multiplicacion entre {num1} y {num2} es: ", num1 * num2)

def division(num1, num2):
    if num2 == 0:
        print("el numero no se puede dividir por 0")
    else:
        print(f"la division entre {num1} y {num2} es: ", num1 / num2)

bucle = "si"

while bucle == "si":
    print(" CALCULADORA")
    print("1. suma")
    print("2. Resta")
    print("3. multiplicacion")
    print("4. division")


    try:
        opcion = float(input("inregese el numero de la operacion: "))
        if opcion == 1:
            num1, num2 = float(input("ingrese el primer numero: ")), float(input("ingrese el segundo numero: "))
            suma(num1, num2)
        elif opcion == 2:
            num1, num2 = float(input("ingrese el primer numero: ")), float(input("ingrese el segundo numero: "))
            resta(num1, num2)
        elif opcion == 3:
            num1, num2 = float(input("ingrese el primer numero: ")), float(input("ingrese el segundo numero: "))
            multiplicacion(num1, num2)
        elif opcion == 4:
            num1, num2 = float(input("ingrese el primer numero: ")), float(input("ingrese el segundo numero: "))
            division(num1, num2)
        else:
            print("opcion no valida")
        bucle = input("¿desea seguir operando? si/no: ")
    except ValueError:
        print("error, digita el numero de la operacion")
        bucle = input("¿desea seguir operando? si/no: ")

print("saliendo de la calculadora")







        
        
            
    