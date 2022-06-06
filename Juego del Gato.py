import time 
import random
import os

humano=""
ordenador=""


def presentacion_2():
    print("Bienvenido")
    print()
    print("Selecciona una Ficha X / O")
    ficha=""
    while ficha!= "O" and ficha!="X":
        ficha=input("       -->").upper()
    if ficha=="O":
        humano="O"
        ordenador = "X"
    else:
        humano="X"
        ordenador="O"
    return humano, ordenador

def mostrar_tablero(tablero):
    print("Juego del Gato")
    print()
    print("         |           |           |")
    print("1   {}    |2   {}      |3   {}      |".format(tablero[0],tablero[1],tablero[2]))
    print("         |           |           |") 
    print("--------------------------------------")
    print("         |           |           |")
    print("4   {}    |5   {}      |6   {}      |".format(tablero[3],tablero[4],tablero[5]))
    print("         |           |           |")
    print("--------------------------------------")
    print("         |           |           |")
    print("7   {}    |8   {}      |9   {}      |".format(tablero[6],tablero[7],tablero[8]))
    print("         |           |           |")


def serguir_jugador():
    print()
    respuesta = input("¿Otra Partida? (s/n)").lower()
    if respuesta =="S" or respuesta=="s":
        return True
    else:
        return False

def hay_ganador(tablero,jugador):
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
        tablero[3] == tablero[4] == tablero[5] == jugador or \
        tablero[6] == tablero[7] == tablero[8] == jugador or \
        tablero[0] == tablero[3] == tablero[6] == jugador or \
        tablero[1] == tablero[4] == tablero[7] == jugador or \
        tablero[2] == tablero[5] == tablero[8] == jugador or \
        tablero[0] == tablero[4] == tablero[8] == jugador or \
        tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    else:
        return False

def tablero_lleno (tablero):
    for i in tablero:
        if i == " ":
            return False
        else:
            return True

def casilla_libre(tablero, casilla ):
    return tablero[casilla]==" "

def movimiento_jugador(tablero):
    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion= None
    while True:
        if posicion not in posiciones:
            posicion= input("te toca (1-9)")
        else:
            posicion= int (posicion)
            if not casilla_libre(tablero,posicion-1):
                print("esta posicion esta ocupada")
            else:
                return posicion-1

def movimiento_ordenador_dificil(tablero,maquina,usuario):
    for i in range(9):
        copia = list(tablero)
        if  casilla_libre(copia, i):
            copia[i]=maquina   
            if hay_ganador(copia,maquina):
                return i
    
    for i in range(9):
        copia=list(tablero)
        if casilla_libre(copia,i):
            copia[i] = usuario
            if hay_ganador(copia,usuario):
                return i
    if ordenador=="X":
        if tablero[4]==" ":
            return 4
        esquinas_vacias=[]
        for i in [0,2,6,8]:
            if casilla_libre(tablero,i):
                esquinas_vacias.append(i)
        demas_vacias=[]
        for i in [1,3,5,7]:
            if casilla_libre(tablero,i):
                demas_vacias.append(i)
        if len(esquinas_vacias) > 0:
            return random.choice(esquinas_vacias)
        else:
            return random.choice(demas_vacias)
    if ordenador == "O":
        contador =0
        for i in range (9):
            if casilla_libre(tablero,i):
                contador += 1
        if contador==7:
            if tablero[4] == " ":
                return 4
    
    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero,casilla):
            casilla=random.randint(0,8)
        else:
            return casilla

######################################          PRINCIPAL        ###########################
jugando= True
while jugando:
    tablero=[" "]*9
    os.system("cls")
    humano,ordenador = presentacion_2()
    os.system("cls")

    mostrar_tablero(tablero)

    if humano=="O":
        turno ="Humano"
    else:
        turno="Ordenador"
    
    partida=True

    while partida:
        if tablero_lleno(tablero):
            print("EMPATE!!!")
            partida=False

        elif turno=="Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla]=humano
            turno="Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero,humano):
                print("Has Ganado!!!")
                partida=False

        elif turno == "Ordenador":
            print("El Ordenador esta pensando...")
            time.sleep(2)
            casilla= movimiento_ordenador_dificil(tablero,ordenador,humano)
            tablero[casilla]= ordenador
            turno="Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero,ordenador):
                print("Has Perdido!!!")
                partida=False
    jugando=serguir_jugador()