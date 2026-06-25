import re

ESTADOS_PACIENTE_VALIDOS = ("Ambulatorio", "Internado", "Alta medica")
ESTADOS_CAMA_VALIDOS = ("Libre", "Ocupada", "Mantenimiento")
SECTORES_VALIDOS = ("Guardia", "Clinica medica", "UTI", "Pediatria")


def validar_texto_no_vacio(texto):
    #Valida que el texto no este vacio
    return texto.strip() != ""


def validar_texto_largo(texto, minimo, maximo):
    #Valida que un texto tenga un largo dentro de un rango
    texto = texto.strip()

    if len(texto) < minimo or len(texto) > maximo:
        return False
    else:
        return True


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
    #Valida que el DNI tenga 7 u 8 numeros usando regex
    dni = dni.strip()

    if re.match(r"^[0-9]{7,8}$", dni):
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
    #Valida que el nombre tenga solo letras y espacios usando regex
    nombre = nombre.strip()

    if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{2,40}$", nombre):
        return True
    else:
        return False


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

        if edad >= 0 and edad <= 120:
            return True
        else:
            return False
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
    #Valida que el diagnostico no este vacio y tenga un largo razonable
    diagnostico = diagnostico.strip()

    if validar_texto_no_vacio(diagnostico) and validar_texto_largo(diagnostico, 3, 100):
        return True
    else:
        return False


def pedir_diagnostico(mensaje):
    #Pide un diagnostico valido
    diagnostico = input(mensaje).strip()

    while not validar_diagnostico(diagnostico):
        print("Error. El diagnostico no puede estar vacio y debe tener entre 3 y 100 caracteres.")
        diagnostico = input(mensaje).strip()

    return diagnostico


def validar_alergias(alergias):
    #Valida el campo de alergias
    alergias = alergias.strip()

    if validar_texto_no_vacio(alergias) and validar_texto_largo(alergias, 2, 100):
        return True
    else:
        return False


def pedir_alergias(mensaje):
    #Pide una alergia valida
    alergias = input(mensaje).strip()

    while not validar_alergias(alergias):
        print("Error. Ingrese una alergia valida o escriba Ninguna.")
        alergias = input(mensaje).strip()

    return alergias


def validar_observacion(observacion):
    #Valida una observacion clinica
    observacion = observacion.strip()

    if validar_texto_no_vacio(observacion) and validar_texto_largo(observacion, 3, 200):
        return True
    else:
        return False


def pedir_observacion(mensaje):
    #Pide una observacion valida
    observacion = input(mensaje).strip()

    while not validar_observacion(observacion):
        print("Error. Ingrese una observacion valida.")
        observacion = input(mensaje).strip()

    return observacion


def validar_evolucion(evolucion):
    #Valida el campo evolucion
    evolucion = evolucion.strip()

    if validar_texto_no_vacio(evolucion) and validar_texto_largo(evolucion, 3, 200):
        return True
    else:
        return False


def pedir_evolucion(mensaje):
    #Pide una evolucion valida
    evolucion = input(mensaje).strip()

    while not validar_evolucion(evolucion):
        print("Error. Ingrese una evolucion valida.")
        evolucion = input(mensaje).strip()

    return evolucion


def validar_opcion(opcion_texto, minimo, maximo):
    #Valida una opcion de menu dentro de un rango
    opcion_texto = opcion_texto.strip()

    try:
        opcion = int(opcion_texto)

        if opcion >= minimo and opcion <= maximo:
            return True
        else:
            return False
    except ValueError:
        return False


def pedir_opcion(mensaje, minimo, maximo):
    #Pide una opcion valida de menu
    opcion_texto = input(mensaje).strip()

    while not validar_opcion(opcion_texto, minimo, maximo):
        print("Error. Ingrese una opcion valida.")
        opcion_texto = input(mensaje).strip()

    return int(opcion_texto)


def validar_estado_paciente(estado):
    #Valida que el estado del paciente este dentro de los permitidos
    estado = estado.strip().lower()

    if estado == "ambulatorio" or estado == "internado" or estado == "alta medica":
        return True
    else:
        return False

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


def validar_numero_cama(numero_cama_texto):
    #Valida que el numero de cama sea mayor a 0
    numero_cama_texto = numero_cama_texto.strip()

    try:
        numero_cama = int(numero_cama_texto)

        if numero_cama > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def pedir_numero_cama(mensaje):
    #Pide un numero de cama valido
    numero_cama_texto = input(mensaje).strip()

    while not validar_numero_cama(numero_cama_texto):
        print("Error. Ingrese un numero de cama valido.")
        numero_cama_texto = input(mensaje).strip()

    return int(numero_cama_texto)


def validar_estado_cama(estado_cama):
    #Valida que el estado de cama este dentro de los permitidos
    estado_cama = estado_cama.strip().title()

    if estado_cama in ESTADOS_CAMA_VALIDOS:
        return True
    else:
        return False


def pedir_estado_cama():
    #Permite elegir el estado de una cama
    print("Seleccione el estado de la cama:")
    print("1 - Libre")
    print("2 - Ocupada")
    print("3 - Mantenimiento")

    opcion = pedir_opcion("Opcion: ", 1, 3)

    if opcion == 1:
        return "Libre"
    elif opcion == 2:
        return "Ocupada"
    else:
        return "Mantenimiento"


def validar_sector(sector):
    #Valida que el sector este dentro de los permitidos
    sector = sector.strip().title()

    if sector in SECTORES_VALIDOS:
        return True
    else:
        return False


def pedir_sector():
    #Permite elegir el sector de una cama
    print("Seleccione el sector:")
    print("1 - Guardia")
    print("2 - Clinica medica")
    print("3 - UTI")
    print("4 - Pediatria")

    opcion = pedir_opcion("Opcion: ", 1, 4)

    if opcion == 1:
        return "Guardia"
    elif opcion == 2:
        return "Clinica medica"
    elif opcion == 3:
        return "UTI"
    else:
        return "Pediatria"
