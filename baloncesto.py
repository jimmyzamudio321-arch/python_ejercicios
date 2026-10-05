"""
¿De qué trata el programa?
Es una aplicación para administrar un torneo deportivo local.
 El programa le muestra un menú al usuario y le permite realizar las siguientes acciones:

Registrar Equipos y Jugadores: Permite ingresar el nombre de un equipo,
 añadir a sus jugadores y asignarles un número de camiseta (sin permitir números repetidos).

Registrar Partidos: Permite anotar el enfrentamiento entre dos equipos con sus marcadores
 (puntos de cada uno), determinando quién ganó y quién perdió para actualizar sus estadísticas.

Ver Tabla de Posiciones y Resultados: Muestra la lista de equipos con sus victorias y derrotas acumuladas,
 además del historial de todos los partidos que se han jugado.

Validación de Errores: Si el usuario ingresa letras en lugar de números o escribe un equipo que no existe,
 el programa no se detiene; le muestra un mensaje de advertencia y le permite intentarlo de nuevo.
"""

#DATOS INICIALES
INFO_TORNEO = ("TORNEO_2026", "BOGOTA")
CAMISETAS_REGISTRADAS = set()            
EQUIPOS = {}                             
HISTORIAL_PARTIDOS = []                  

opciones = {
    1:"registrar nuevo equipo",
    2:"registrar resultado de partido",
    3:"ver tabla de posiciones y resultados",
    4:"salir"
}

bucle = True

while bucle:
    print(f"SISTEMA DE TORNEO {INFO_TORNEO[0]}, {INFO_TORNEO[1]}")
    print("1. Registrar nuevo equipo")
    print("2. Registrar resultado de partido")
    print("3. Ver tabla de posiciones y resultados")
    print("4. Salir")
    
    try:
        opcion = int(input("ingresa la opcion: "))
        if opcion in opciones:
            if opcion == 1:
                equipo = input("ingrese el nombre del equipo: ")
                EQUIPOS[equipo] = {
                    "jugadores": [],
                    "victorias": 0,
                    "derrotas": 0,
                }
                jugadores = "si"
                while jugadores == "si":
                    new_jugador = input("ingrese el nombre del nuevo jugador: ")
                    cam = True
                    while cam:
                        camiseta = int(input("ingrese el numero de camiseta: "))
                        if camiseta in CAMISETAS_REGISTRADAS:
                            print("el numero de camiseta ya esta registrada")
                        else:
                            CAMISETAS_REGISTRADAS.add(camiseta)
                            EQUIPOS[equipo]["jugadores"].append({
                                "nombre del jugador":new_jugador,
                                "numero de camiseta":camiseta,
                            })
                            cam = False
                    else:
                        jugadores = input("¿desea registrar mas jugadores? si/no: ")
                else:
                    print("jugador registrado")
            elif opcion == 2:
                primer_equipo = input("ingrese el primer equipo del partido: ")
                segundo_equipo = input("ingrese el segundo equipo del partido: ")

                if primer_equipo in EQUIPOS and segundo_equipo in EQUIPOS:
                    puntos1 = int(input(f"ingrese los puntos de {primer_equipo}"))
                    puntos2 = int(input(f"ingrese los puntos de {segundo_equipo}"))
                    if puntos1 > puntos2:
                        EQUIPOS[primer_equipo]['victorias'] += 1
                        EQUIPOS[segundo_equipo]['derrotas'] += 1
                        print(f'gano {primer_equipo}')
                    elif puntos1 < puntos2:
                        EQUIPOS[primer_equipo]['derrotas'] += 1
                        EQUIPOS[segundo_equipo]['victorias'] += 1
                        print(f'gano {segundo_equipo}')
                    else:
                        print('el resultado no puede quedar en empate')

                    HISTORIAL_PARTIDOS.append((primer_equipo, puntos1, segundo_equipo, puntos2))
                else:
                    print('uno o ambos equipos no estan registrados')
            elif opcion == 3:
                print('tabla de posiciones')
                if not EQUIPOS:
                    print("no hay equipos registrados")
                else:
                    for nombre, datos in EQUIPOS.items():
                        print(f"Equipo: {nombre} | Victorias: {datos['victorias']} | Derrotas: {datos['derrotas']}")
                        print("  Jugadores:")
                        for j in datos["jugadores"]:
                            print(f" #{j['numero de camiseta']} {j['nombre del jugador']}")

                print("HISTORIAL DE PARTIDOS")
                if not HISTORIAL_PARTIDOS:
                    print("No se han jugado partidos.")
                else:
                    for p in HISTORIAL_PARTIDOS:
                        print(f"{p[0]} {p[1]} vs {p[3]} {p[2]}")
            elif opcion == 4:
                print("Saliendo del sistema de torneo...")
                bucle = False
    except ValueError:
        print("error, sintaxix incorrecta")