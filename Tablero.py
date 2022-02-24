# -*- coding: utf-8 -*-


import numpy as np
from random import randint

#Funcion saludo
def saludo(nombre='intro'):
 pal=open(nombre+'.txt')
 for i in pal:
    print(i.strip('\n'))
 pal.close()
 
#Funcion nombre
def nombre_maq(nombrel):
    '''
    Recibe como parametro el nombre del archivo .txt
    Eige al azar el nombre de la maquina desde ese .txt
    Retorna el nombre de la maquina
    '''
    f=open(nombrel+'.txt')
    allnom=f.readlines()
    nom=randint(0,len(allnom)-1)
    nombre_m=str(allnom[nom]).strip()
    return nombre_m

#Tablero inicial de ceros con dimension dada
def board_init(n):
    '''
    Parametro es la dimension del tablero que es matriz cuadrada
    Entrega un tablero vacio
    '''
    tablero=np.zeros((n, n))
    return tablero

#Verificar no hay llenos    
def lleno(tablero):
    '''
    Recibe como parametro el nombre del tablero a validar si esta lleno
    Retorna una variable que se usa como bandera para la validacion. Es False si el tablero esta lleno
    '''
    bj=False
    for i in tablero:
          for j in i:
              if j==0:
                  bj=True
                  break
          else:
              continue
          break
    if bj==False:
        print('Tablero lleno')
    return bj

#Verificar tablero lleno
def board_llenar(tablero,px,n):
    '''
    Parametro:tablero a llenar, posicion deseada del usuario, dimension del tablero
    Valida si la posicion esta llena, de lo contrario, lo llena
    Retorna tablero llenado
    '''
    
    #Posicion del usuario
    i,j=int(px.split(',')[0])-1,int(px.split(',')[1])-1
    while not(tablero[i][j]==0):
        print('Posicion ocupada, ensaye otra' )
        px=input('Usuario, que posicion desea jugar? (Fila, Columna) ')
        i,j=int(px.split(',')[0])-1,int(px.split(',')[1])-1
    tablero[i][j]=1 #Imprime posicion del usuario
    #Posicion de la maquina
    bj=lleno(tablero)
    if bj==True:
        k,l=randint(0,n-1),randint(0,n-1)
        while not(tablero[k][l]==0):
            k,l=randint(0,n-1),randint(0,n-1)
        tablero[k][l]=2 #Imprime posicion de la maquina
    return tablero

#Construir tablero
def tablero_1(board): 
        '''
        Parametro es el tablero a dibujar
        Imprime tableros de X y O
        '''
        linea=''
        separador='  ----'*len(board)
        print(separador)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==1.:
                    linea=linea+'|  X  '
                elif board[i][j]==2.:
                    linea=linea+'|  O  '
                else:
                    linea=linea+'|'+' '*5
            print(linea+'|')
            print(separador)
            linea=''
        print(linea)
        
#Ganador filas
def ganador1(tablero_final,maquina_nom,b1=False):
       '''
       Parametros tablero a evaluar, nombre de la maquina, bandera de ganar igual a  False
       Evalua si hay ganador en una fila, imprime en cual y quien
       Retorna una bandera con False si no hubo ganador, o True en caso contrario
       '''
       #Validacion por filas
       anterior=0
       for i in range(len(tablero_final)):
           if (tablero_final[i][0]==1 or tablero_final[i][0]==2) and b1==False:
               anterior=tablero_final[i][0]
               for j in range(len(tablero_final)):
                   if tablero_final[i][j]==anterior:
                       b1=True
                       anterior=tablero_final[i][j]
                   else:
                       b1=False
                       break
      
               if b1==True:
                   if tablero_final[i][0]==1:
                       print('Usuario es ganador en la fila: ',i+1)
                   else:
                       print(maquina_nom,' es ganador en la fila: ',i+1)
       return b1
 
#Ganador diagonal principal                      
def ganador2(tablero_final,maquina_nom,b2=False):
       '''
       Parametros tablero a evaluar, nombre de la maquina, bandera de ganar igual a  False
       Evalua si hay ganador en diaginal principal, imprime  quien
       Retorna una bandera con False si no hubo ganador, o True en caso contrario
       '''
       if  (tablero_final[0][0]==1 or tablero_final[0][0]==2) and b2==False:
           diag_ant=tablero_final[0][0]  
           for i in range(len(tablero_final)):
                   if tablero_final[i][i]==diag_ant:
                      b2=True
                      diag_ant=tablero_final[i][i]
                   else:
                       b2=False
                       break
           if b2==True:
              if tablero_final[i][i]==1:
                  print('El usuario es ganador en la diagonal principal')
              else:
                  print(maquina_nom,' es ganador en la diagonal principal')
       return b2

#Ganador columnas              
def ganador3(tablero_final,maquina_nom,b3=False):
       '''
       Parametros tablero a evaluar, nombre de la maquina, bandera de ganar igual a  False
       Evalua si hay ganador en una columna, imprime  quien y cual
       Retorna una bandera con False si no hubo ganador, o True en caso contrario
       '''
       for j in range(len(tablero_final)):
           if (tablero_final[0][j]==1 or tablero_final[0][j]==2) and b3==False:
               anterior_col=tablero_final[0][j]
               for i in range(len(tablero_final)):
                   if tablero_final[i][j]==anterior_col:
                       b3=True
                       anterior_col=tablero_final[i][j]
                   else:
                       b3=False
                       break
               if b3==True:
                   if tablero_final[0][j]==1:
                       print('Usuario es ganador en la columna: ',j+1)
                   else:
                       print(maquina_nom,' es ganador en la columna: ',j+1)
       return b3

#Ganador diagonal secundaria                      
def ganador4(tablero_final,maquina_nom,b4=False):
       '''
       Parametros tablero a evaluar, nombre de la maquina, bandera de ganar igual a  False
       Evalua si hay ganador en diaginal secundaria, imprime  quien
       Retorna una bandera con False si no hubo ganador, o True en caso contrario
       '''
       if  (tablero_final[0][-1]==1 or tablero_final[0][-1]==2) and b4==False:
           diags_ant=tablero_final[0][len(tablero_final)-1]  
           for i in range(len(tablero_final)):
                   if tablero_final[i][-1-i]==diags_ant:
                      b4=True
                      diags_ant=tablero_final[i][-1-i]
                   else:
                       b4=False
                       break
           if b4==True:
              if tablero_final[0][-1]==1:
                  print('El usuario es ganador en la diagonal secundaria')
              else:
                  print(maquina_nom,' es ganador en la diagonal secundaria')
       return b4
   

          
            


        

