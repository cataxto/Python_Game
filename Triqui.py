# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:40:45 2020

@author: Catalina
"""

import Tablero as t


#Primero, 
t.saludo()

#Nombre del contricante
maquina_noml=t.nombre_maq('listas')
print('Tu contrincante es: ',maquina_noml)

#definamos dimension del tablero
n=int(input('Dimension del tablero: ' ))
tablero=t.board_init(n)
tableroi=t.tablero_1(tablero)

#Jugar!!!
b1=False
b2=False
b3=False
b4=False
bj=True
vez=True
while (b1==False and b2==False and b3==False and b4==False and bj==True) or vez==True:
    px=input('Definamos esta jugada, cual es su posicion del usuario: fila y columna: ')
    tablero1=t.board_llenar(tablero=tablero,px=px,n=n) #Llenar de 1 y 0
    tableroi=t.tablero_1(tablero1) #Imprimir tablero
    b1=t.ganador1(tablero1,maquina_nom=maquina_noml) #Ganador
    b2=t.ganador2(tablero1,maquina_nom=maquina_noml) #Ganador
    b3=t.ganador3(tablero1,maquina_nom=maquina_noml) #Ganador
    b4=t.ganador4(tablero1,maquina_nom=maquina_noml) #Ganador
    bj=t.lleno(tablero1) #Tablero lleno
    if (b1==True or b2==True or b3==True or b4==True or bj==False):
        d=input('Desea jugar otra vez? Si o No ').lower()
        vez=False
        if d=='si':
            vez=True
            tablero=t.board_init(n)
        
    

