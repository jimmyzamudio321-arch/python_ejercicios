#Crearemos una mascota con energia que se pueda rellenar o consumir

class mascota():

    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = int(energia)
    
    def estado(self):
        print(f" {self.nombre} tiene {self.energia} / 100 de energia")
    def comer(self):
        if self.energia > 90:
            print(f"{self.nombre} tiene suficiente energia por lo que no puede comer")
        else:
            self.energia = self.energia + 10
            print(f"{self.nombre} esta comiendo")
    def jugar(self):
        if self.energia < 20:
            print(f'{self.nombre} esta cansado, no puede jugar')
        else:
            self.energia = self.energia - 20
            print(f"{self.nombre} esta jugando")
    def hacer_popo(self):
        self.energia = self.energia - 1
        print(f'{self.nombre} hizo popo')
    def dormir(self):
        self.energia = 100
        print(f'{self.nombre} durmio y esta lleno de energia')
def salir():
    global bucle 
    bucle = False
    print('saliendo del sistema')

nombre_usuario = input('ingrese el nombre de la mascota: ')
mi_mascota = mascota(nombre_usuario, 100)
opciones = {
    1: mi_mascota.estado,
    2: mi_mascota.comer,
    3: mi_mascota.jugar,
    4: mi_mascota.dormir,
    5: mi_mascota.hacer_popo,
    6: salir
}
print(f'que quiere hacer con {mi_mascota.nombre}')
print("1. ver estado")
print("2. darle de comer")
print("3. jugar con el")
print("4. dejarlo dormir")
print('5. llevarlo a hacer popo')
print("6. salir")

bucle = True
while bucle:
    try:
        opcion = int(input('escoja la opcion: '))
        if opcion in opciones:
            opciones[opcion]()
        else:
            print('usted ingreso una opcion no valida')
    except ValueError:
        print('error, caracteres incorrectos')




