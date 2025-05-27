from pacientes import pacientes
from funciones import *

def menu()->None:
    """
    Muestra el menu principal del sistema de gestion y procesa las opciones del usuario.

    Parametros:
        None
    
    Retorno:
        None
    """
    x=True
    while x:
        respuesta = int(input("Sistema de Gestion de Clinica: \n1.Cargar pacientes. \n2.Mostrar todos los pacientes. \n3.Buscar pacientes por numero de Historia Clinica. \n4.Ordenar pacientes por numero de Historia Clinica. \n5.Mostrar pacientes con mas dias de internacion. \n6.Mostrar pacientes con menos dias de internacion. \n7.Cantidad de pacientes con mas de 5 dias de internacion. \n8.Promedio de dias de internacion de todos los pacientes. \n9.Salir.\n"))

        match respuesta:
            case 1:
               #cargar pacientes
               cant=int(input("Ingrese la cantidad de pacientes a agregar: "))
               cargar_pacientes(pacientes,cant)
            case 2:
                #mostrar todos los pacientes
                if not sin_pacientes(pacientes):
                    print("Los pacientes actualmente en el sistema son: ")
                    mostrar_pacientes(pacientes)
            case 3:
                #Buscar pacientes por numero de Historia clinica
                if not sin_pacientes(pacientes):
                    buscar_paciente(pacientes)
            case 4:
                #Ordenar pacientes por numero de Historia clinica
                if not sin_pacientes(pacientes):
                    pacientes_ordenados = ordenar_pacientes(pacientes)
                    mostrar_pacientes(pacientes_ordenados)
            case 5:
                #Mostrar paciente con mas dias de internacion
                if not sin_pacientes(pacientes):
                    mas_dias(pacientes)   
            case 6:
                #Mostrar paciente con menos dias de internacion
                if not sin_pacientes(pacientes):
                    menos_dias(pacientes)
            case 7:
                #cantidad de pacientes con mas de 5 dias de internacion
                if not sin_pacientes(pacientes):
                    mas_de_5(pacientes)
            case 8:
                #Promedio de dias de internacion de todos los pacientes
                if not sin_pacientes(pacientes):
                    promedio = promedio_internacion(pacientes)
                    print(f"Promedio de días de internación: {promedio}")
                    print("----------------------------------------------")
            case 9:
                print("Saliendo del programa")
                x=False
            case _:
                return print("Ingrese bien el numero")