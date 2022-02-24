# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:29:38 2020

@author: Catalina
"""

from Funciones2 import *




band=True

while band==True:
    print(
      
"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*",      
"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", 
"-*-*-*-*-* Sistema de Informacion Academico de Estudiantes y Asignaturas -*-*-*-*-*-*-*-*-*",       
"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*",       
"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-\n\n ",


"Seleccione una de las siguientes opciones:\n",

"    1. Mostrar nombre de estudiantes matriculados\n",
"    2. Mostrar todos los cursos registrados\n",
"    3. Consultar estudiantes matriculados en un curso\n",
"    4. Agregar nuevo estudiante\n",
"    5. Agregar nuevo curso\n",
"    6. Consultar el porcentaje de estudiantes que perdio y aprobo un curso\n",
"    7. Consultar materias matriculadas por un estudiante\n",
"    8. Consultar promedio de un estudiante especifico\n",\
"    9. Matricular estudiante en un curso\n"
)


    opc=int(input("Ingrese opcion elegida: "))
    
    #Opcion 1
    if opc==1:
        print("\n Los estudiantes matriculados son:")
        print("----------------------------------------------")
        print("|  Cedula      |  Nombre de Estudiante       |")
        print("----------------------------------------------")
        for i in estudiantes:
            print("| ",i," | ",estudiantes[i],(25-len(estudiantes[i]))*" ","|")
        print("----------------------------------------------")
            
        
    #Opcion 2
    elif opc==2:
        print("\n La informacion de los cursos registrados es:")
        print("-------------------------------------------------------------")
        print(" |  Nombre de Curso            |  Creditos |  Numero Notas |")
        print("-------------------------------------------------------------")
        for i in asignaturas:
            print(" | ",i,(25-len(i))*" ","|     ",asignaturas[i][0],"   |      ",asignaturas[i][1],"      |")
        print("-------------------------------------------------------------")       


    #Opcion 3
    elif opc==3:
        inscritos_curso=leer_InscritosXCurso2(asignaturas)
        asign=input('Digita el nombre del curso a consultar: ').lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        elem=inscritos_curso[asign]
        if elem[0] != 'No hay estudiantes registrados':
            print("\n En el curso, los estudiantes matriculados son:")
            print("----------------------------------------------")
            print("|  Cedula      |  Nombre de Estudiante       |")
            print("----------------------------------------------")        
            for i in elem:
                print("| ",i[0]," | ",i[1],(25-len(i[1]))*" ","|")
            print("----------------------------------------------")   
        else:
            print("No hay estudiantes inscritos en la asignatura. ")


    #Opcion 4
    elif opc==4:
        cedula=int(input('Diligencia cedula del estudiante a asignar '))
        nombre=input('Diligencia nombre del estudiante a asignar ')
        agregar_estudiante(cedula,nombre)
        print("\n La lista de estudiantes actualizada es :")
        print("----------------------------------------------")
        print("|  Cedula      |  Nombre de Estudiante       |")
        print("----------------------------------------------")
        for i in estudiantes:
            print("| ",i," | ",estudiantes[i],(25-len(estudiantes[i]))*" ","|")
        print("----------------------------------------------")        
        
        
    #Opcion 5
    elif opc==5:       
        curso=input('Diligencia el nombre del curso a asignar: ').lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        creds=int(input('Diligencia numero de creditos: '))
        nnotas=int(input('Diligencia numero de notas del curso: '))
        agregar_curso(curso,creds,nnotas)
        print("\n La informacion actualizada de los cursos registrados es:")
        print("-------------------------------------------------------------")
        print(" |  Nombre de Curso            |  Creditos |  Numero Notas |")
        print("-------------------------------------------------------------")
        for i in asignaturas:
            print(" | ",i,(25-len(i))*" ","|     ",asignaturas[i][0],"   |      ",asignaturas[i][1],"      |")
        print("-------------------------------------------------------------")       


    #Opcion 6
    elif opc==6:    
        estado_asignaturas=porc_gano_perdio(asignaturas)   
        curso=input('Diligencia el nombre del curso a consultar: ').lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        if estado_asignaturas[curso][0]=='No hay estudiantes registrados':
            print('No hay estudiantes registrados')
        else:
            print("\nEn ",curso,", el ",estado_asignaturas[curso][0],"% aprobo el curso")
            print("En ",curso,", el ",estado_asignaturas[curso][1],"% aprobo el curso")
            preg_porc=input("Desea ver el desglose de las notas consolidadas de los estudiantes del curso? Si/No ").lower().replace('í','i')
            if preg_porc=="No":
                print("Continue navegando en el Menu.")
            else:
                print("\n----------------------------------------------------------")
                print("|  Cedula    |  Nombre de Estudiante      | Consolidado |")
                print("----------------------------------------------------------")
                dd=dict(sorted(estado_asignaturas[curso][2].items()))
                for i in dd:
                    print("|",i,"|",estudiantes[i],(25-len(estudiantes[i]))*" ","|",dd[i],(10-len(str(dd[i])))*" ","|")
                print("----------------------------------------------------------")


    #Opcion 7
    elif opc==7:
        estudiantes_asignaturas=estudianteXasignaturas(asignaturas)
        est=int(input('Ingrese identificacion del estudiante a consultar: '))
        if estudiantes_asignaturas[est]=='No tiene materias inscritas':
            print("\nEl estudiante ",estudiantes[est],", no tiene materias inscritas")
        else:
            print("\nEl estudiante ",estudiantes[est],", tiene las siguientes asignaturas registradas: ")
            print("---------------------------------")
            print(" |  Nombre de Curso            | ")
            print("---------------------------------")  
            for i in estudiantes_asignaturas[est]:
                print(" | ",i,(25-len(i))*" ","|")
            print("---------------------------------")
        

    #Opcion 8
    elif opc==8:
        estudiantes_promedio=PromedioXEstudiante(estudiantes, asignaturas)
        est=int(input('Ingrese identificacion del estudiante a consultar: '))
        if estudiantes_asignaturas[est]=='No tiene materias inscritas':
            print("\nEl estudiante ",estudiantes[est],", no tiene materias inscritas, por lo tanto no se puede calcular su promedio")
        else:
            print("\nEl estudiante ",estudiantes[est],", tiene el promedio ", estudiantes_promedio[est]," desglosado asi: ") 
            print("----------------------------------------------------------")
            print(" |  Nombre de Curso            | Creditos | Consolidado |")
            print("----------------------------------------------------------")
            for i in estudiantes_asignaturas[est]:
                print(" | ",i,(25-len(i))*" ","|  ",asignaturas[i][0],"     |",estado_asignaturas[i][2][est],(10-len(str(estado_asignaturas[i][2][est])))*" ","|")
            print("----------------------------------------------------------")
    

    #Opcion 9
    elif opc==9:
        curso=input('Ingrese nombre de la asignatura ').lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        idalum=int(input('Ingrese identificacion del alumno a inscribir '))
        Inscribir_AlumnoXCurso(curso,idalum)        
        
    preg=input("Desea continuar explorando el menu? Si/No: ").lower().replace('í','i')
    
    if preg=='si':
        band=True
    else:
        print('Gracias por navegar en nuestro menu. Feliz semana!!')
        band=False
        
    
curso='vivamos la u'
idalum=1142440653    
    