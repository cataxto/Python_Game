# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#Punto1: Leer todos los estudiantes
def leer_estudiantes(archivo):
    estudiantes={}
    t_estudiantes=open(archivo,'r')
    for i in t_estudiantes:
        t=i.strip('\n') #Separa cada linea
        est= t.split(';') #En cada linea hay el separador ;, que separa nombre y cedula
        clave=int(est[0])
        valor=est[1]
        estudiantes[clave]=valor
    t_estudiantes.close()
    return estudiantes

estudiantes=leer_estudiantes('students.txt')
#print(estudiantes)    

#Punto2: Leer todas las materias
def leer_cursos(archivo):
    cursos={}
    t_cursos=open(archivo,'r')
    for i in t_cursos:
        c=i.strip('\n') #Separa cada linea
        cur=c.split(':') #Seprar en trozos de info cada linea
        info_extraida=cur[0] #La info de la materia esta en la posicion 0 de cada lista
        lista_info_asignatura=info_extraida.split(';')
        clave=lista_info_asignatura[0]
        info=lista_info_asignatura[1:]
        for j in range(len(info)): #Pasando a entero el numero de horas y creditos de cada asign
            info[j]=int(info[j])
        dtemp={}
        if len(cur)>1:
            for i in range(1,len(cur)): #Crear subdiccionario de inscritos con sus notas
                temp=cur[i].split(';')
                for i in range(len(temp)): #Para asignar int a cedula a float a notas
                    if i==0:
                        temp[i]=int(temp[i])
                    else:
                        temp[i]=float(temp[i])
                dtemp[temp[0]]=temp[1:]
            info.append(dtemp)
        cursos[clave]=info
    t_cursos.close()
    return cursos

asignaturas=leer_cursos('subjects.txt')
#print(asignaturas)


#asignaturas=list(asignaturas['fisica mecanica'][2].keys())



#Punto 3: estudiantes matriculados por curso
#def leer_inscritosXcurso(archivo):
#    cursos_insc={}
#    materia1=[]
#    l_est=[]
#    t_cursos=open(archivo,'r')
#    for i in t_cursos:
#        c=i.strip('\n') #Separa cada linea
#        cur=c.split(':')
#        materia0=cur[0]
#        materia1.append(materia0[:materia0.find(';')])
#        est_con_notas=cur[1:] #Muestra inscritos con sus notas
#        est=[] #Pero, solo necesitamos inscritos, se otera sobre est_con_notas
#        for lista in est_con_notas:
#                estudiante_lista=int(lista[:lista.find(';')]) #Se extrae solo el numero de cedula
#                est_nom=estudiantes[estudiante_lista]
#                est.append([estudiante_lista,est_nom]) 
#        l_est.append(est)
#    cursos_insc=dict(zip(materia1,l_est))
#    t_cursos.close()
#    return cursos_insc
#
#inscritos_curso=leer_inscritosXcurso('subjects.txt')
#print(inscritos_curso)

def leer_InscritosXCurso2(diccionario):
    inscritos={}
    for i in asignaturas:
        info=[]
        if len(list(asignaturas[i]))==2:
            info.append('No hay estudiantes registrados')
        else:
            for j in list(asignaturas[i][2].keys()):
                est_nom=estudiantes[j]
                info.append([j,est_nom])
        inscritos[i]=info    
    return inscritos

inscritos_curso=leer_InscritosXCurso2(asignaturas)
#print(inscritos_curso)


#Punto 4
def agregar_estudiante(cedula,nombre):
    #cedula=int(input('Diligencia cedula del estudiante a asginar '))
    #nombre=input('Diligencia nombre del estudiante a asignar ')
    estudiantes[cedula]=nombre  #FALTA UNA VEZ TERMINE ACTUALICE EL .TXT #################################################################3
    return estudiantes

#estudiantes_agregados=agregar_estudiante()
#print(estudiantes_agregados)

#Punto 5
def agregar_curso(curso,creds,nnotas):
    #curso=input('Diligencia el nombre del curso a asignar: ')
    #horas_curso=int(input('Diligencia numero de creditos: '))
    #creds_curso=int(input('Diligencia numero de notas obtenidas: '))
    asignaturas[curso]=[creds,nnotas] #FALTA UNA VEZ TERMINE ACTUALICE EL .TXT ###################################################
    return asignaturas

#cursos_agregados=agregar_curso()
#print(cursos_agregados)    

#Punto 6
def porc_gano_perdio(diccionario):
    porcs_asignatura={}
    for i in asignaturas:
        info=[]
        if len(list(asignaturas[i]))==2:
            info.append('No hay estudiantes registrados')
        else:
            gano=0
            perdio=0
            inscritos=list(asignaturas[i][2].keys())
            list_est={}
            for j in inscritos:        
              calif=round(np.mean(asignaturas[i][2][j]),2)
              list_est[j]=calif
              if calif>=3.0:
                  gano+=1
              else:
                  perdio+=1
            porc_gano=round(gano/len(inscritos),2)*100
            porc_perdio=round(perdio/len(inscritos),2)*100
            info.append(porc_gano)
            info.append(porc_perdio)
            info.append(list_est)
        porcs_asignatura[i]=info
    return porcs_asignatura
                  
estado_asignaturas=porc_gano_perdio(asignaturas)    
#print(estado_asignaturas)

#Punto 7
def estudianteXasignaturas(diccionario):
    est_asigna={}
    for i in estudiantes:
      asign=[]
      for j in asignaturas: 
        if (len(asignaturas[j])!=2) and (i in asignaturas[j][2]):
            #print(i,j)
            asign.append(j)
      if len(asign)==0:
          est_asigna[i]='No tiene materias inscritas'
      else:
          est_asigna[i]=asign
    return est_asigna

estudiantes_asignaturas=estudianteXasignaturas(asignaturas)
#print(estudiantes_asignaturas)    

#Punto 8
def PromedioXEstudiante(destudiantes, dasignatura):
    destudiantes_asignaturas=estudianteXasignaturas(asignaturas)
    destado_asignaturas=porc_gano_perdio(asignaturas) 
    est_promedioacad={}
    for estudiante in destudiantes:
        total_creds=0
        total_suma_prod=0
        if destudiantes_asignaturas[estudiante]!='No tiene materias inscritas':
            for curso_inscrito in destudiantes_asignaturas[estudiante]:
                calif=float(destado_asignaturas[curso_inscrito][2][estudiante])
                credito=int(dasignatura[curso_inscrito][0])
                suma_prod=calif*credito
                total_suma_prod+=suma_prod
                total_creds+=credito
            promedio_acad=round(total_suma_prod/total_creds,2)
            est_promedioacad[estudiante]=promedio_acad
        else:
            promedio_acad=0
            est_promedioacad[estudiante]=promedio_acad
    return est_promedioacad

estudiantes_promedio=PromedioXEstudiante(estudiantes, asignaturas)
#print(estudiantes_promedio)        
#        
##Punto 9
def Inscribir_AlumnoXCurso(curso,idalum):
    #curso=input('Ingrese nombre de la asignatura ').lower()
    #idalum=int(input('Ingrese identificacion del alumno a inscribir '))
    inscritos_curso=leer_InscritosXCurso2(asignaturas)
    if curso not in asignaturas.keys():
            print('Esta asignatura no esta ofertada')
    if idalum not in estudiantes.keys():
        print('Esta identificacion no esta registrada')
        #break
    else:
        nomalum=estudiantes[idalum]
    if curso in asignaturas and idalum in estudiantes:
        if len(asignaturas[curso])==2:
                print('No hay estudiantes registrados inicialmente')
                inscritos_curso[curso]=[idalum,nomalum]
                print('Ingreso exitoso')
                notas1=[]
                asignaturas[curso].append({})
                for i in range(asignaturas[curso][1]):
                    nota=float(input('Digite nota '+str(i+1)+' del estudiante: '))
                    notas1.append(nota)
                asignaturas[curso][2][idalum]=notas1
        elif  idalum not in asignaturas[curso][2]:
                inscritos_curso[curso].append([idalum,nomalum])
                print('Ingreso exitoso')
                notas1=[]
                #asignaturas[curso].append([])
                for i in range(asignaturas[curso][1]):
                    nota=float(input('Digite nota '+str(i+1)+' del estudiante: '))
                    notas1.append(nota)
                asignaturas[curso][2][idalum]=notas1
        else:
            print('El alumno ya esta registrado en el curso')
    return inscritos_curso
        #agrgar el estudiante en el 3 component del valor del diccionario y pedir notas o sino ceor
#inscribir_alumnoXurso=Inscribir_AlumnoXCurso()      
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    