import re

normalizar_nombre = lambda texto: texto.strip().title()
normalizar_texto = lambda texto: texto.strip()

ESTADOS_PACIENTE_VALIDOS = ("Ambulatorio", "Internado", "Alta medica")
ESTADOS_CAMA_VALIDOS = ("Libre", "Ocupada", "Mantenimiento")
SECTORES_VALIDOS = ("Guardia", "Clinica medica", "UTI", "Pediatria")

#-----------------------DATOS-----------------------
pacientes = {}
 
turnos = {
    "08:00": "Libre",
    "09:00": "Libre",
    "10:00": "Libre",
    "11:00": "Libre",
    "12:00": "Libre"
}
 
camas = {
    1: "Libre",
    2: "Libre",
    3: "Libre",
    4: "Libre",
    5: "Libre"
}
 
horarios = list(turnos.keys())

#------------------FUNCIONES------------------


def contar_lista(lista):
    #Cuenta la cantidad de elementos de una lista
    contador = 0
    for _ in lista:
        contador = contador + 1
    return contador


def buscar_paciente(dni_buscado):
    #Busca un paciente por DNI y devuelve su indice o -1 si no existe
    dni_buscado = dni_buscado.strip()
    for dni in pacientes:
        if dni == dni_buscado:
            return dni
    return -1


def registrar_paciente(dni, nombre, edad, diagnostico, estado_inicial="Ambulatorio"):
    #Registra un paciente nuevo si el DNI no existe
    if dni in pacientes:
        return False

    pacientes[dni] = {
        "nombre": normalizar_nombre(nombre),
        "edad": edad,
        "diagnostico": normalizar_texto(diagnostico),
        "estado": estado_inicial,
        "alergias": "Ninguna",
        "observaciones": "Sin observaciones",
        "evolucion": "Sin evolucion"
    }
    return True


def mostrar_paciente(dni_buscado):
    #Muestra por pantalla los datos de un paciente buscado por DNI
    if dni_buscado not in pacientes:
        print("No se encontro ningun paciente.")
    else:
        p = pacientes[dni_buscado]

        print("----- DATOS DEL PACIENTE -----")
        print("DNI:", dni_buscado)
        print("Nombre:", p["nombre"])
        print("Edad:", p["edad"])
        print("Diagnostico:", p["diagnostico"])
        print("Estado:", p["estado"])
        print("------------------------------")


def mostrar_todos_los_pacientes():
    #Muestra todos los pacientes registrados
    if not pacientes:
        print("No hay pacientes cargados.")
    else:
        print("----- LISTA DE PACIENTES -----")
        resumenes = list(map(lambda dni: f"DNI: {dni} - Nombre: {pacientes[dni]['nombre']} - Estado: {pacientes[dni]['estado']}", pacientes))
        for resumen in resumenes:
            print(resumen)
        print("------------------------------")


def actualizar_diagnostico(dni_buscado, nuevo_diagnostico):
    #Actualiza el diagnostico de un paciente
    if dni_buscado not in pacientes:
        return False
    pacientes[dni_buscado]["diagnostico"] = normalizar_texto(nuevo_diagnostico)
    return True

def cambiar_estado(dnis, estados, dni_buscado, nuevo_estado):
    #Cambia el estado general de un paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        estados[indice] = normalizar_texto(nuevo_estado).title()
        return True


def internar_paciente(dni_buscado):
    #Pasa el estado del paciente a Internado
    if dni_buscado not in pacientes:
        return -1
    elif pacientes[dni_buscado]["estado"] == "Internado":
        return 0
    else:
        pacientes[dni_buscado]["estado"] = "Internado"
        return 1

def dar_alta(dni_buscado):
    #Pasa el estado del paciente a Alta medica y libera la cama si tiene una
    if dni_buscado not in pacientes:
        return -1
    elif pacientes[dni_buscado]["estado"] == "Alta medica":
            return 0
    else:
        pacientes[dni_buscado]["estado"] = "Alta medica"

        for nro_camas, ocupante in camas.items():
            if ocupante == dni_buscado:
                camas[nro_camas] = "Libre"
                break

        return 1



def mostrar_pacientes_internados():
    #Muestra unicamente los pacientes que estan en estado de Internado
    internados = list(filter(lambda p: p["estado"] == "Internado", pacientes.values()))

    if not internados:
        print("No hay pacientes internados.")
    else:
        print("----- PACIENTES INTERNADOS -----")
        internados = [(dni, paciente) for dni, paciente in pacientes.items() if paciente["estado"] == "Internado"]
        for dni,paciente in internados:
            print(f"DNI: {dni} - Nombre: {paciente['nombre']} - Estado: {paciente['estado']}")
        print("--------------------------------")

#------------------REGISTRO CLINICO------------------

def actualizar_alergias(dni_buscado, nuevas_alergias):
    #Actualiza las alergias de un paciente
    if dni_buscado not in pacientes:
        return False
    pacientes[dni_buscado]["alergias"] = normalizar_texto(nuevas_alergias)
    return True

def agregar_observacion(dni_buscado, nueva_observacion):
    #Agrega una observacion al registro del paciente
    if dni_buscado not in pacientes:
        return False

    texto_nuevo = normalizar_texto(nueva_observacion)
    actual = pacientes[dni_buscado]["observaciones"]

    if actual == "" or actual == "Sin observaciones":
        pacientes[dni_buscado]["observaciones"] = texto_nuevo
    else:
        pacientes[dni_buscado]["observaciones"] = actual + " | " + texto_nuevo
    return True


def agregar_evolucion(dni_buscado, nueva_evolucion):
    #Agrega una evolucion al registro del paciente
    if dni_buscado not in pacientes:
        return False

    texto_nuevo = normalizar_texto(nueva_evolucion)
    actual = pacientes[dni_buscado]["evolucion"]

    if actual == "" or actual == "Sin evolucion":
        pacientes[dni_buscado]["evolucion"] = texto_nuevo
    else:
        pacientes[dni_buscado]["evolucion"] = actual + " | " + texto_nuevo
    return True

def mostrar_registro_clinico(dni_buscado):
    #Muestra el registro clinico ampliado de un paciente
    if dni_buscado not in pacientes:
        print("No se encontro ningun paciente con ese DNI.")
    else:
        print("----- REGISTRO CLINICO -----")
        p = pacientes[dni_buscado]
        print("DNI:", dni_buscado)
        print("Nombre:", p["nombre"])
        print("Diagnostico:", p["diagnostico"])
        print("Alergias:", p["alergias"])
        print("Observaciones:", p["observaciones"])
        print("Evolucion:", p["evolucion"])
        print("----------------------------")


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
    estado = estado.strip().title()

    if estado in ESTADOS_PACIENTE_VALIDOS:
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

#------------------GESTION DE CAMAS------------------

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


def mostrar_camas():
    #Muestra el estado de las camas
    print("--- ESTADO DE LAS CAMAS ---")
    for nro, ocupante in camas.items():
        print(f"Cama {nro} -> {ocupante}")


def asignar_cama():
    #Asigna una cama a un paciente internado
    dni = pedir_dni("Ingrese el DNI del paciente a asignar cama: ")

    if dni not in pacientes:
        print("No se encontro ningun paciente con ese DNI.")
        return
    elif pacientes[dni]["estado"] != "Internado":
        print("El paciente no esta internado, no se le puede asignar una cama.")
        return

    for nro, ocupante in camas.items():
        if ocupante == dni:
            print(f"El paciente ya tiene asignada la cama {nro}.")
            return

    for nro, ocupante in camas.items():
        if ocupante == "Libre":
            camas[nro] = dni
            print(f"Cama {nro} asignada correctamente.")
            return

    print("No hay camas disponibles para asignar.")


def liberar_cama():
    #Libera una cama ocupada por un paciente
    dni = pedir_dni("Ingrese el DNI del paciente a liberar cama: ")

    for nro, ocupante in camas.items():
        if ocupante == dni:
            camas[nro] = "Libre"
            print(f"Cama {nro} liberada correctamente.")
            return

    print("No se encontro ninguna cama asignada a ese paciente.")

#------------------GESTION DE TURNOS------------------

def mostrar_turnos():
    #Muestra todos los turnos con su estado
    print("--- ESTADO DE LOS TURNOS ---")
    for hora, estado in turnos.items():
        print(hora, "->", estado)


def asignar_turnos():
    #Asigna un turno si el horario existe y esta libre
    hora = pedir_horario("Ingrese la hora del turno: ")
    nombre = pedir_nombre("Ingrese el nombre del paciente: ")

    if turnos[hora] == "Libre":
        turnos[hora] = nombre
        print("Turno asignado correctamente.")
    else:
        print("El turno ya esta ocupado por", turnos[hora])


def pedir_horario(mensaje):
    #Pide un horario valido dentro de los horarios del sistema
    hora = input(mensaje).strip()

    while hora not in horarios:
        print("Error. Ingrese un horario valido.")
        print("Horarios validos:", horarios)
        hora = input(mensaje).strip()

    return hora


def modificar_turno():
    #Modifica un turno existente por otro horario libre
    hora_actual = pedir_horario("Ingrese la hora del turno a modificar: ")

    if turnos[hora_actual] == "Libre":
        print("El turno esta libre, no se puede modificar.")
        return
    nombre_paciente = turnos[hora_actual]
    print("Turno actual asignado a:", nombre_paciente)

    hora_nueva = pedir_horario("Ingrese la nueva hora del turno: ")

    if hora_nueva == hora_actual:
        print("Ingreso el mismo horario.")
        return
    elif turnos[hora_nueva] == "Libre":
        turnos[hora_nueva] = nombre_paciente
        turnos[hora_actual] = "Libre"
        print("Turno modificado correctamente.")
    else:
        print("El nuevo horario ya esta ocupado.")


def cancelar_turno():
    #Cancela un turno si el horario existe y esta ocupado
    hora = pedir_horario("Ingrese la hora del turno a cancelar: ")

    if turnos[hora] != "Libre":
        turnos[hora] = "Libre"
        print("Turno cancelado correctamente.")
    else:
        print("El turno ya esta libre, no se puede cancelar.")


def menu_registro_clinico():
    #Muestra el menu del registro clinico
    opcion = -1

    while opcion != 0:
        print("\\n--- REGISTRO CLINICO ---")
        print("1 - Actualizar alergias")
        print("2 - Agregar observacion")
        print("3 - Agregar evolucion")
        print("4 - Mostrar registro clinico")
        print("0 - Volver al menu de pacientes")

        opcion = pedir_opcion("Opcion: ", 0, 4)

        if opcion == 1:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nuevas_alergias = pedir_alergias("Ingrese las alergias del paciente: ")

            if actualizar_alergias(dni, nuevas_alergias):
                print("Alergias actualizadas exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 2:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nueva_observacion = pedir_observacion("Ingrese la observacion: ")

            if agregar_observacion(dni, nueva_observacion):
                print("Observacion agregada exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 3:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nueva_evolucion = pedir_evolucion("Ingrese la evolucion: ")

            if agregar_evolucion(dni, nueva_evolucion):
                print("Evolucion agregada exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 4:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            mostrar_registro_clinico(dni)


def menu_camas():
    #Muestra el menu de gestion de camas
    opcion = -1

    while opcion != 0:
        print("\\n--- GESTION DE CAMAS ---")
        print("1 - Ver camas")
        print("2 - Asignar cama a paciente internado")
        print("3 - Liberar cama")
        print("0 - Volver al menu de pacientes")
        opcion = pedir_opcion("Opcion: ", 0, 3)

        if opcion == 1:
            mostrar_camas()
        elif opcion == 2:
            asignar_cama()
        elif opcion == 3:
            liberar_cama()


def menu_pacientes():
    #Muestra el menu de gestion de pacientes
    subopcion = -1

    while subopcion != 0:
        print("\\n--- GESTION DE PACIENTES ---")
        print("1 - Registrar paciente")
        print("2 - Buscar paciente")
        print("3 - Mostrar todos los pacientes")
        print("4 - Actualizar diagnostico")
        print("5 - Dar alta")
        print("6 - Mostrar pacientes internados")
        print("7 - Internar paciente")
        print("8 - Gestion de camas")
        print("9 - Registro clinico")
        print("0 - Volver al menu principal")

        subopcion = pedir_opcion("Opcion: ", 0, 9)

        if subopcion == 1:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nombre = pedir_nombre("Ingrese el nombre del paciente: ")
            edad = pedir_edad("Ingrese la edad del paciente: ")
            diagnostico = pedir_diagnostico("Ingrese el diagnostico del paciente: ")
            estado = pedir_estado_inicial()

            if registrar_paciente(dni, nombre, edad, diagnostico, estado):
                print("Paciente registrado exitosamente.")
            else:
                print("Ya existe un paciente con ese DNI.")

        elif subopcion == 2:
            dni = pedir_dni("Ingrese el DNI del paciente a buscar: ")
            mostrar_paciente(dni)

        elif subopcion == 3:
            mostrar_todos_los_pacientes()

        elif subopcion == 4:
            dni = pedir_dni("Ingrese el DNI del paciente a actualizar: ")
            nuevo_diagnostico = pedir_diagnostico("Ingrese el nuevo diagnostico: ")

            if actualizar_diagnostico(dni, nuevo_diagnostico):
                print("Diagnostico actualizado exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 5:
            dni = pedir_dni("Ingrese el DNI del paciente a dar de alta: ")
            resultado = dar_alta(dni)

            if resultado == 1:
                print("Paciente dado de alta exitosamente.")
            elif resultado == 0:
                print("El paciente ya tiene el alta medica.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 6:
            mostrar_pacientes_internados()

        elif subopcion == 7:
            dni = pedir_dni("Ingrese el DNI del paciente a internar: ")
            resultado = internar_paciente(dni)

            if resultado == 1:
                print("Paciente internado exitosamente.")
            elif resultado == 0:
                print("El paciente ya estaba internado.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 8:
            menu_camas()

        elif subopcion == 9:
            menu_registro_clinico()

        elif subopcion == 0:
            print("Volviendo al menu principal...")


def main():
    #Controla el menu principal del sistema
    opcion = -1

    while opcion != 0:
        print("\\n--- MENU PRINCIPAL ---")
        print("[1] Ver turnos")
        print("[2] Reserva de turnos")
        print("[3] Modificar turnos")
        print("[4] Cancelacion de turnos")
        print("[5] Gestion de pacientes")
        print("[0] Salir")

        opcion = pedir_opcion("Opcion: ", 0, 5)

        if opcion == 1:
            print("\\n--- TURNOS ---")
            mostrar_turnos()

        elif opcion == 2:
            asignar_turnos()

        elif opcion == 3:
            modificar_turno()

        elif opcion == 4:
            cancelar_turno()

        elif opcion == 5:
            menu_pacientes()

        elif opcion == 0:
            print("Saliendo del sistema...")


if __name__ == "__main__":
    main()
