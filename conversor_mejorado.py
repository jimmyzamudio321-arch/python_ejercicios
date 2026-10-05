def conversor(monto, moneda_origen, moneda_destino):
    moneda_origen = float(moneda_origen)
    moneda_destino = float(moneda_destino)
    monto_dolares = monto / moneda_origen
    return monto_dolares * moneda_destino

tasas = {
    "dolar": 1,
    "euro": 0.86,
    "peso_mexicano": 16.95,
    "peso_colombiano":3200,
    "yuan":6.71,
    "libra_esterlina":1.35,
    "peso_argentino":1508

}

opciones = {
    1: "dolar",
    2: "peso_colombiano",
    3: "peso_mexicano",
    4: "euro",
    5: "yuan",
    6: "libra_esterlina",
    7: "peso_argentino",

}

bucle = "si"

while bucle == "si":
    print("___________________")
    print("conversor de monedas" )
    print("___________________")
    print("1. dolar")
    print("2. peso colombiano")
    print("3. peso mexicano")
    print("4. euro")
    print("5. yuan")
    print("6. libra esterlina")
    print("7. peso argentino")

    try:
        moneda_origen = float(input("ingresa la moneda de origen: "))
        moneda_destino = float(input("ingresa la moneda de destino: "))
       
        if moneda_origen in opciones and moneda_destino in opciones:
            if moneda_origen == moneda_destino:
                print("la moneda de origen no se puede convertir por si misma")
            else:
                monto = float(input("ingrese el monto a convertir: "))
                
                clave_origen = opciones[moneda_origen]
                clave_destino = opciones[moneda_destino]
                print(f"El valor del {opciones[moneda_origen]}, a {opciones[moneda_destino]} es {conversor(monto, tasas[clave_origen], tasas[clave_destino])}")

        else:     
            print("ingrese una opcion correcta")
        bucle = input("¿desea seguir convirtiendo? si/no: ")
                    
    except ValueError:
        print("error ingresa un numero")
else:
    print("saliendo del convertidor")