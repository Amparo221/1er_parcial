#sin pacientes
def sin_pacientes(matriz: list[list])->bool:
    """
    Verifica si la lista de pacientes esta vacia e imprime un mensaje si lo esta.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        bool: True si esta vacia, False en caso contrario.
    """
    if not matriz:
        print("----------------------------------------------\nLa matriz está vacía, cargue pacientes antes de continuar.\n----------------------------------------------")
        return True
    return False


#cargar pacientes
def cargar_pacientes(matriz: list[list], cantidad: int)->None:
    """
    Carga pacientes en la lista segun la cantidad indicada por el usuario.

    Parametros:
        matriz (list): La lista de pacientes.
        cantidad (int): La cantidad de pacientes a cargar.
    
    Retorno:
        None
    """
    x=0
    while x < cantidad:
        while True:
            num = input("Ingrese el numero de historia clinica: ")
            if num.isdigit():
                num_h_clinica = int(num)
                break
            else:
                print("ERROR: Ingrese un numero entero valido.")

        nombre = str(input("Ingrese el nombre del paciente: "))
        while nombre == "":
            print("ERROR: El nombre no puede estar vacio.")
            nombre = input("Ingrese el nombre del paciente: ")

        while True:
            edad_input = input("Ingrese la edad del paciente: ")
            if edad_input.isdigit():
                edad = int(edad_input)
                break
            else:
                print("ERROR: Ingrese un numero entero valido para la edad.")

        diagnostico = str(input("Ingrese el diagnostico del apciente:"))
        while diagnostico == "":
            print("ERROR: El diagnostico no puede estar vacio.")
            diagnostico = input("Ingrese el diagnostico del paciente: ")

        while True:
            dias_input = input("Ingrese la cantidad de dias de internacion: ")
            if dias_input.isdigit():
                d_internacion = int(dias_input)
                break
            else:
                print("ERROR: Ingrese un numero entero valido para los dias.")

        print("----------------------------------------------")
        paciente = [num_h_clinica, nombre, edad, diagnostico, d_internacion]
        matriz[len(matriz):] = [paciente]
        x+=1


#mostrar pacientes
def mostrar_pacientes(matriz: list[list])->None:
    """
    Muestra todos los pacientes contenidos en la lista.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        None
    """
    for i in range(len(matriz)):
        print(matriz[i])
    print("----------------------------------------------")

#Buscar pacientes
def buscar_paciente(matriz: list[list])->None:
    """
    Busca un paciente segun su numero de historia clinica e imprime sus datos.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        None
    """
    elemento=int(input("Ingrese el numero de historia clinica del paciente a buscar: "))
    for i in range(len(matriz)):
        if matriz[i][0] == elemento:
            paciente=matriz[i]
            print(f"El paciente que busco es {paciente}")
            return 
    print("No se pudo encontrar el paciente, vuelva a intentar.")


#Ordenar pacientes
def ordenar_pacientes(matriz: list[list])->list[list]:
    """
    Ordena los pacientes por numero de historia clinica en forma ascendente.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        list: Lista de pacientes ordenada.
    """
    longitud = len(matriz)
    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if matriz[j][0] > matriz[j + 1][0]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    return matriz


#Mostrar paciente con mas dias de internacion
def mas_dias(matriz: list[list])->None:
    """
    Muestra el o los pacientes con la mayor cantidad de dias de internacion.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        None
    """
    max_dias = float("-inf")

    for i in range(len(matriz)):
        if matriz[i][4] > max_dias:
            max_dias = matriz[i][4]

    print("El/los pacientes con mas dias de internacion son: ")
    for i in range(len(matriz)):
        if matriz[i][4] == max_dias:
            print(matriz[i])
    print("----------------------------------------------")


#Mostrar paciente con menos dias de internacion
def menos_dias(matriz: list[list])->None:
    """
    Muestra el o los pacientes con la menor cantidad de dias de internacion.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        None
    """
    min_dias = float("inf")

    for i in range(len(matriz)):
        if matriz[i][4] < min_dias:
            min_dias = matriz[i][4]

    print("El/los pacientes con menos dias de internacion son: ")
    for i in range(len(matriz)):
        if matriz[i][4] == min_dias:
            print(matriz[i])
    print("----------------------------------------------")


#cantidad de pacientes con mas de 5 dias de internacion
def mas_de_5(matriz: list[list]):
    """
    Muestra la cantidad de pacientes con mas de 5 dias de internacion.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        None
    """
    contador=0
    for i in range(len(matriz)):
        if matriz[i][4] > 5:
            contador+=1
    if contador == 0:
        return print("No pacientes con mas de 5 dias de internacion")
    else:
        return print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")


#Promedio de dias de internacion de todos los pacientes
def promedio_internacion(matriz: list[list])->int:
    """
    Calcula el promedio de dias de internacion de todos los pacientes.

    Parametros:
        matriz (list): La lista de pacientes.
    
    Retorno:
        float: El promedio de dias de internacion.
    """
    longitud = len(matriz)
    total_dias=0
    for i in range(len(matriz)):
        total_dias+=matriz[i][4]
    promedio=total_dias/longitud
    return promedio