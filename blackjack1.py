

import random
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}

lista_cartas = list(cartas) #creo una nueva lista con unicamente los valores de las cartas del diccionario
print("Estas son las cartas de la partida  -->  ",lista_cartas)


#PARTE DEL JUGADOR
n=0
numcartas=0
sumacartasjugador=0
#le doy la opcion al jugador de devolver las cartas al crupier si no le gustan y que este le entregue otras dos de la baraja
while True:
    numcartas=numcartas+1   
    carta=random.choice(lista_cartas)  
    print("Esta es su carta --> ",carta)
    if numcartas>=11:         # hago esto para que el momento en el que el jugador ya haya pedido 11 cartas , no pueda pedir de nuevo dos mas
        respuesta="no"
    else:                      # mientras sea menor que 11 entonces este podrá pedir al que reparta cartas que le entregue  dos mas
        respuesta=input("¿desea escoger otra carta?:")    
    if respuesta=="no":
        n=n+1
        sumacartasjugador=sumacartasjugador+cartas[carta]
    if n==2:
        carta2=carta
        valorcarta2=cartas[carta]
        break
    elif n==1:
        carta1=carta
        valorcarta1=cartas[carta1]

#aqui elimino estas dos cartas de las que podrá escoger la banca
lista_cartas.remove(carta1)
lista_cartas.remove(carta2)

print(f"Tus primera carta es {carta1} --> su puntuacion es {valorcarta1}\n tu segunga carta es {carta2} -->su puntuacion es {valorcarta2}")
print(f">>>La suma de las puntuaciones del jugador es {sumacartasjugador}<<<")


print("Las cartas de la banca son ahora  ➤➤➤ :",lista_cartas)

#PARTE DE LA BANCA  (doy por supuesto que a la banca que se le asigan unas cartas y en nigún momento podrá escoger otras)
cartabanca1=random.choice(lista_cartas)
lista_cartas.remove(cartabanca1)         #elimino esta carta para que no se me repita en el choice
cartabanca2=random.choice(lista_cartas)
valor_cartabanca1=cartas[cartabanca1]
valor_cartabanca2=cartas[cartabanca2]
sumacartasbanca=valor_cartabanca1+valor_cartabanca2
print(f"La primera carta de la banca es {cartabanca1} --> su puntuacion es {valor_cartabanca1} \n la segunda carta de la banca carta es {cartabanca2} -->su puntuacion es {valor_cartabanca2}")
print(f">>>La suma de las puntaciones de la banca es {sumacartasbanca}<<<")

#¿Quién gana la partida?
if sumacartasjugador >=22:
    print("Perdiste, tus cartas sumamban 22 o mas....")
if sumacartasbanca>sumacartasjugador:
    print("Vaya, la banca ha ganado")
if sumacartasbanca<sumacartasjugador:
    print("!Has ganado!")
if sumacartasbanca==sumacartasjugador:
    print("empate...")













