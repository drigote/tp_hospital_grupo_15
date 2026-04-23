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

    if not solo_numeros(edad_texto):
        return False

    edad = int(edad_texto)

    if edad >= 0 and edad <= 120:
        return True
    else:
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

    if solo_numeros(opcion_texto):
        opcion = int(opcion_texto)

        if opcion >= minimo and opcion <= maximo:
            return True
        else:
            return False
    else:
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
