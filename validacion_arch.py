ESTADOS_CAMA_VALIDOS = ("Libre", "Ocupada", "Limpieza", "Mantenimiento")
ESTADOS_PACIENTE_VALIDOS = ("Ambulatorio", "Internado", "Alta medica")


def validar_texto_no_vacio(texto):
    #Valida que el texto no este vacio
    return texto.strip() != ""



def solo_numeros(texto):
    #Valida que un texto tenga solo numeros
    texto = texto.strip()

    if texto == "":
        return False

    i = 0
    while i < len(texto):
        if texto[i] < "0" or texto[i] > "9":
            return False
        i = i + 1

    return True



def validar_dni(dni):
    #Valida que el DNI tenga 7 u 8 numeros
    dni = dni.strip()

    if solo_numeros(dni) and (len(dni) == 7 or len(dni) == 8):
        return True
    else:
        return False



def pedir_dni(mensaje):
    #Pide un DNI valido
    dni = input(mensaje).strip()

    while not validar_dni(dni):
        print("Error. El DNI debe tener 7 u 8 numeros.")
        dni = input(mensaje).strip()

    return dni



def validar_nombre(nombre):
    #Valida que el nombre tenga solo letras y espacios
    nombre = nombre.strip()
    letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "

    if len(nombre) < 2:
        return False

    i = 0
    while i < len(nombre):
        if nombre[i] not in letras_validas:
            return False
        i = i + 1

    return True



def pedir_nombre(mensaje):
    #Pide un nombre valido
    nombre = input(mensaje).strip()

    while not validar_nombre(nombre):
        print("Error. Ingrese solo letras y espacios.")
        nombre = input(mensaje).strip()

    return nombre



def validar_edad(edad_texto):
    #Valida que la edad sea un numero entre 0 y 120
    edad_texto = edad_texto.strip()

    try:
        edad = int(edad_texto)
        return edad >= 0 and edad <= 120
    except ValueError:
        return False



def pedir_edad(mensaje):
    #Pide una edad valida
    edad_texto = input(mensaje).strip()

    while not validar_edad(edad_texto):
        print("Error. Ingrese una edad valida entre 0 y 120.")
        edad_texto = input(mensaje).strip()

    return int(edad_texto)



def validar_diagnostico(diagnostico):
    #Valida que el diagnostico no este vacio
    return validar_texto_no_vacio(diagnostico)



def pedir_diagnostico(mensaje):
    #Pide un diagnostico valido
    diagnostico = input(mensaje).strip()

    while not validar_diagnostico(diagnostico):
        print("Error. El diagnostico no puede estar vacio.")
        diagnostico = input(mensaje).strip()

    return diagnostico



def validar_opcion(opcion_texto, minimo, maximo):
    #Valida una opcion de menu dentro de un rango
    opcion_texto = opcion_texto.strip()

    try:
        opcion = int(opcion_texto)
        return opcion >= minimo and opcion <= maximo
    except ValueError:
        return False



def pedir_opcion(mensaje, minimo, maximo):
    #Pide una opcion valida de menu
    opcion_texto = input(mensaje).strip()

    while not validar_opcion(opcion_texto, minimo, maximo):
        print("Error. Ingrese una opcion valida.")
        opcion_texto = input(mensaje).strip()

    return int(opcion_texto)



def pedir_estado_inicial():
    #Permite elegir el estado inicial del paciente
    print("Seleccione el estado inicial del paciente:")
    print("1 - Ambulatorio")
    print("2 - Internado")

    opcion = pedir_opcion("Opcion: ", 1, 2)

    if opcion == 1:
        return "Ambulatorio"
    else:
        return "Internado"



def validar_alergias(alergias):
    #Valida el campo de alergias
    return validar_texto_no_vacio(alergias)



def pedir_alergias(mensaje):
    #Pide las alergias del paciente
    alergias = input(mensaje).strip()

    while not validar_alergias(alergias):
        print("Error. Ingrese las alergias o escriba Ninguna.")
        alergias = input(mensaje).strip()

    return alergias



def validar_observacion(observacion):
    #Valida una observacion clinica
    return validar_texto_no_vacio(observacion)



def pedir_observacion(mensaje):
    #Pide una observacion valida
    observacion = input(mensaje).strip()

    while not validar_observacion(observacion):
        print("Error. La observacion no puede estar vacia.")
        observacion = input(mensaje).strip()

    return observacion



def validar_evolucion(evolucion):
    #Valida una evolucion clinica
    return validar_texto_no_vacio(evolucion)



def pedir_evolucion(mensaje):
    #Pide una evolucion valida
    evolucion = input(mensaje).strip()

    while not validar_evolucion(evolucion):
        print("Error. La evolucion no puede estar vacia.")
        evolucion = input(mensaje).strip()

    return evolucion



def validar_sector(sector):
    #Valida que el sector no este vacio
    return validar_texto_no_vacio(sector)



def pedir_sector(mensaje):
    #Pide un sector valido para camas o internacion
    sector = input(mensaje).strip()

    while not validar_sector(sector):
        print("Error. El sector no puede estar vacio.")
        sector = input(mensaje).strip()

    return sector



def validar_numero_cama(numero_cama_texto):
    #Valida que el numero de cama sea entero positivo
    numero_cama_texto = numero_cama_texto.strip()

    try:
        numero_cama = int(numero_cama_texto)
        return numero_cama > 0
    except ValueError:
        return False



def pedir_numero_cama(mensaje):
    #Pide un numero de cama valido
    numero_cama_texto = input(mensaje).strip()

    while not validar_numero_cama(numero_cama_texto):
        print("Error. Ingrese un numero de cama valido.")
        numero_cama_texto = input(mensaje).strip()

    return int(numero_cama_texto)



def validar_estado_cama(estado):
    #Valida el estado de una cama
    estado = estado.strip().title()
    return estado in ESTADOS_CAMA_VALIDOS



def pedir_estado_cama():
    #Permite elegir el estado de una cama
    print("Seleccione el estado de la cama:")
    print("1 - Libre")
    print("2 - Ocupada")
    print("3 - Limpieza")
    print("4 - Mantenimiento")

    opcion = pedir_opcion("Opcion: ", 1, 4)

    if opcion == 1:
        return "Libre"
    elif opcion == 2:
        return "Ocupada"
    elif opcion == 3:
        return "Limpieza"
    else:
        return "Mantenimiento"



def validar_estado_paciente(estado):
    #Valida el estado general del paciente
    estado = estado.strip().title()
    return estado in ESTADOS_PACIENTE_VALIDOS



def validar_lista_sin_duplicados(lista):
    #Valida que una lista no tenga elementos repetidos
    return len(lista) == len(set(lista))



def obtener_opciones_estado_cama():
    #Devuelve los estados posibles de cama
    return ESTADOS_CAMA_VALIDOS



def obtener_opciones_estado_paciente():
    #Devuelve los estados posibles del paciente
    return ESTADOS_PACIENTE_VALIDOS
