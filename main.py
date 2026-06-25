import re
import archivos_json as json_archivos


# ------------------ NORMALIZACION ------------------
normalizar_nombre = lambda texto: texto.strip().title()
normalizar_texto = lambda texto: texto.strip()


# ------------------ CONSTANTES DE VALIDACION ------------------
ESTADOS_PACIENTE_VALIDOS = ("Ambulatorio", "Internado", "Alta medica")
ESTADOS_CAMA_VALIDOS = ("Libre", "Ocupada", "Mantenimiento")
SECTORES_VALIDOS = ("Guardia", "Clinica medica", "UTI", "Pediatria")


# ------------------ DATOS DEL SISTEMA ------------------
dnis = []
nombres = []
edades = []
diagnosticos = []
estados = []

alergias = []
observaciones = []
evoluciones = []

turnos = ["Libre", "Libre", "Libre", "Libre", "Libre"]
horarios = ["08:00", "09:00", "10:00", "11:00", "12:00"]

camas = ["Libre", "Libre", "Libre", "Libre", "Libre"]
numeros_camas = [1, 2, 3, 4, 5]

def reemplazar_lista(lista_original, lista_nueva):
    #Reemplaza el contenido de una lista sin cambiar la variable original
    lista_original.clear()

    for dato in lista_nueva:
        lista_original.append(dato)


# ------------------ VALIDACIONES ------------------
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
    sector = sector.strip().lower()

    if sector == "guardia" or sector == "clinica medica" or sector == "uti" or sector == "pediatria":
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


# ------------------ GESTION DE PACIENTES ------------------
def contar_lista(lista):
    #Cuenta la cantidad de elementos de una lista
    contador = 0
    for _ in lista:
        contador = contador + 1
    return contador


def buscar_paciente(dnis, dni_buscado):
    #Busca un paciente por DNI y devuelve su indice o -1 si no existe
    dni_buscado = dni_buscado.strip()

    i = 0
    while i < len(dnis) and dnis[i] != dni_buscado:
        i = i + 1

    if i < len(dnis):
        return i
    else:
        return -1


def registrar_paciente(dnis, nombres, edades, diagnosticos, estados,
                       dni, nombre, edad, diagnostico, estado_inicial="Ambulatorio"):
    #Registra un paciente nuevo si el DNI no existe
    if buscar_paciente(dnis, dni) != -1:
        return False

    dnis.append(normalizar_texto(dni))
    nombres.append(normalizar_nombre(nombre))
    edades.append(edad)
    diagnosticos.append(normalizar_texto(diagnostico))
    estados.append(estado_inicial)

    return True


def mostrar_paciente(dnis, nombres, edades, diagnosticos, estados, dni_buscado):
    #Muestra por pantalla los datos de un paciente buscado por DNI
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        print("No se encontro ningun paciente con ese DNI.")
    else:
        print("----- DATOS DEL PACIENTE -----")
        print("DNI:", dnis[indice])
        print("Nombre:", nombres[indice])
        print("Edad:", edades[indice])
        print("Diagnostico:", diagnosticos[indice])
        print("Estado:", estados[indice])
        print("------------------------------")


def obtener_resumenes_pacientes(dnis, nombres, estados):
    #Se usa para mostrar todos los pacientes de una forma mas ordenada
    return list(map(lambda i: f"DNI: {dnis[i]} - Nombre: {nombres[i]} - Estado: {estados[i]}", range(len(dnis))))


def mostrar_todos_los_pacientes(dnis, nombres, estados):
    #Muestra todos los pacientes registrados
    total = contar_lista(dnis)

    if total == 0:
        print("No hay pacientes cargados.")
    else:
        print("----- LISTA DE PACIENTES -----")
        resumenes = obtener_resumenes_pacientes(dnis, nombres, estados)

        for resumen in resumenes:
            print(resumen)

        print("------------------------------")


def actualizar_diagnostico(dnis, diagnosticos, dni_buscado, nuevo_diagnostico):
    #Actualiza el diagnostico de un paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        diagnosticos[indice] = normalizar_texto(nuevo_diagnostico)
        return True


def cambiar_estado(dnis, estados, dni_buscado, nuevo_estado):
    #Cambia el estado general de un paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        estados[indice] = normalizar_texto(nuevo_estado).title()
        return True


def internar_paciente(dnis, estados, dni_buscado):
    #Pasa el estado del paciente a Internado
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return -1
    elif estados[indice] == "Internado":
        return 0
    else:
        estados[indice] = "Internado"
        return 1


def dar_alta(dnis, estados, dni_buscado):
    #Pasa el estado del paciente a Alta medica
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return -1
    else:
        if estados[indice] == "Alta medica":
            return 0
        else:
            estados[indice] = "Alta medica"
            return 1


def esta_internado(dnis, estados, dni_buscado):
    #Devuelve True si el paciente esta internado
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        return estados[indice] == "Internado"


def obtener_indices_internados(estados):
    #Devuelve los indices de pacientes internados usando filter() y lambda
    return list(filter(lambda i: estados[i] == "Internado", range(len(estados))))


def mostrar_pacientes_internados(dnis, nombres, estados):
    #Muestra unicamente los pacientes que estan en estado de Internado
    indices_internados = obtener_indices_internados(estados)

    if len(indices_internados) == 0:
        print("No hay pacientes internados.")
    else:
        print("----- PACIENTES INTERNADOS -----")

        for i in indices_internados:
            print(f"DNI: {dnis[i]} - Nombre: {nombres[i]} - Estado: {estados[i]}")

        print("--------------------------------")


def actualizar_alergias(dnis, alergias, dni_buscado, nuevas_alergias):
    #Actualiza las alergias de un paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        alergias[indice] = normalizar_texto(nuevas_alergias)
        return True


def agregar_observacion(dnis, observaciones, dni_buscado, nueva_observacion):
    #Agrega una observacion al registro del paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        texto_nuevo = normalizar_texto(nueva_observacion)

        if observaciones[indice] == "" or observaciones[indice] == "Sin observaciones":
            observaciones[indice] = texto_nuevo
        else:
            observaciones[indice] = observaciones[indice] + " | " + texto_nuevo

        return True


def agregar_evolucion(dnis, evoluciones, dni_buscado, nueva_evolucion):
    #Agrega una evolucion al registro del paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        return False
    else:
        texto_nuevo = normalizar_texto(nueva_evolucion)

        if evoluciones[indice] == "" or evoluciones[indice] == "Sin evolucion":
            evoluciones[indice] = texto_nuevo
        else:
            evoluciones[indice] = evoluciones[indice] + " | " + texto_nuevo

        return True


def mostrar_registro_clinico(dnis, nombres, diagnosticos, alergias, observaciones, evoluciones, dni_buscado):
    #Muestra el registro clinico ampliado de un paciente
    indice = buscar_paciente(dnis, dni_buscado)

    if indice == -1:
        print("No se encontro ningun paciente con ese DNI.")
    else:
        print("----- REGISTRO CLINICO -----")
        print("DNI:", dnis[indice])
        print("Nombre:", nombres[indice])
        print("Diagnostico:", diagnosticos[indice])
        print("Alergias:", alergias[indice])
        print("Observaciones:", observaciones[indice])
        print("Evolucion:", evoluciones[indice])
        print("----------------------------")


# ------------------ TURNOS ------------------
def pedir_horario(mensaje):
    #Pide un horario valido dentro de los horarios disponibles
    hora = input(mensaje).strip()

    while hora not in horarios:
        print("Error. Ingrese un horario valido.")
        print("Horarios validos:", horarios)
        hora = input(mensaje).strip()

    return hora


def mostrar_turnos():
    #Muestra todos los turnos con su estado
    print("\n--- ESTADO DE LOS TURNOS ---")

    for i in range(len(horarios)):
        print(horarios[i], "->", turnos[i])


def asignar_turno():
    #Asigna un turno si el horario esta libre
    hora = pedir_horario("Ingrese la hora del turno: ")
    nombre = pedir_nombre("Ingrese el nombre del paciente: ")

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] == "Libre":
                turnos[i] = nombre
                print("Turno asignado correctamente.")
            else:
                print("El turno ya esta ocupado.")
            return


def modificar_turno():
    #Modifica un turno existente por otro horario libre
    hora_actual = pedir_horario("Ingrese la hora del turno a modificar: ")

    for i in range(len(horarios)):
        if horarios[i] == hora_actual:
            if turnos[i] == "Libre":
                print("Ese turno esta libre, no hay nada para modificar.")
                return

            nombre_paciente = turnos[i]
            print("Turno actual asignado a:", nombre_paciente)

            hora_nueva = pedir_horario("Ingrese la nueva hora del turno: ")

            if hora_nueva == hora_actual:
                print("Ingreso el mismo horario.")
                return

            j = 0
            while j < len(horarios):
                if horarios[j] == hora_nueva:
                    if turnos[j] == "Libre":
                        turnos[j] = nombre_paciente
                        turnos[i] = "Libre"
                        print("Turno modificado correctamente.")
                    else:
                        print("El nuevo horario ya esta ocupado.")
                    return
                j = j + 1


def cancelar_turno():
    #Cancela un turno si el horario esta ocupado
    hora = pedir_horario("Ingrese la hora del turno a cancelar: ")

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] != "Libre":
                turnos[i] = "Libre"
                print("Turno cancelado correctamente.")
            else:
                print("El turno ya esta libre.")
            return


# ------------------ CAMAS ------------------
def mostrar_camas():
    #Muestra el estado de las camas
    print("\n--- ESTADO DE LAS CAMAS ---")

    for i in range(len(camas)):
        print("Cama", numeros_camas[i], "->", camas[i])


def liberar_cama_por_dni(dni):
    #Libera una cama buscando por DNI
    for i in range(len(camas)):
        if camas[i] == dni:
            camas[i] = "Libre"
            return True

    return False


def asignar_cama():
    #Asigna una cama libre a un paciente internado
    dni = pedir_dni("Ingrese el DNI del paciente a asignar cama: ")
    indice_paciente = buscar_paciente(dnis, dni)

    if indice_paciente == -1:
        print("No se encontro ningun paciente con ese DNI.")
        return

    if estados[indice_paciente] != "Internado":
        print("El paciente no esta internado, no se le puede asignar una cama.")
        return

    for i in range(len(camas)):
        if camas[i] == dni:
            print("El paciente ya tiene asignada la cama", numeros_camas[i])
            return

    for i in range(len(camas)):
        if camas[i] == "Libre":
            camas[i] = dni
            print("Cama", numeros_camas[i], "asignada correctamente.")
            return

    print("No hay camas disponibles para asignar.")


def liberar_cama():
    #Libera la cama asignada a un paciente
    dni = pedir_dni("Ingrese el DNI del paciente a liberar cama: ")

    if liberar_cama_por_dni(dni):
        print("Cama liberada correctamente.")
    else:
        print("No se encontro ninguna cama asignada a ese paciente.")


def menu_camas():
    #Menu de gestion de camas
    opcion = -1

    while opcion != 0:
        print("\n--- GESTION DE CAMAS ---")
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
        elif opcion == 0:
            print("Volviendo al menu de pacientes...")


# ------------------ REGISTRO CLINICO ------------------
def menu_registro_clinico():
    #Menu del registro clinico
    opcion = -1

    while opcion != 0:
        print("\n--- REGISTRO CLINICO ---")
        print("1 - Actualizar alergias")
        print("2 - Agregar observacion")
        print("3 - Agregar evolucion")
        print("4 - Mostrar registro clinico")
        print("0 - Volver al menu de pacientes")

        opcion = pedir_opcion("Opcion: ", 0, 4)

        if opcion == 1:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nuevas_alergias = pedir_alergias("Ingrese las alergias del paciente: ")

            if actualizar_alergias(dnis, alergias, dni, nuevas_alergias):
                print("Alergias actualizadas exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 2:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nueva_observacion = pedir_observacion("Ingrese la observacion: ")

            if agregar_observacion(dnis, observaciones, dni, nueva_observacion):
                print("Observacion agregada exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 3:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nueva_evolucion = pedir_evolucion("Ingrese la evolucion: ")

            if agregar_evolucion(dnis, evoluciones, dni, nueva_evolucion):
                print("Evolucion agregada exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 4:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            mostrar_registro_clinico(dnis, nombres, diagnosticos, alergias, observaciones, evoluciones, dni)

        elif opcion == 0:
            print("Volviendo al menu de pacientes...")


# ------------------ MENU DE PACIENTES ------------------
def menu_pacientes():
    #Menu de gestion de pacientes
    opcion = -1

    while opcion != 0:
        print("\n--- GESTION DE PACIENTES ---")
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

        opcion = pedir_opcion("Opcion: ", 0, 9)

        if opcion == 1:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nombre = pedir_nombre("Ingrese el nombre del paciente: ")
            edad = pedir_edad("Ingrese la edad del paciente: ")
            diagnostico = pedir_diagnostico("Ingrese el diagnostico del paciente: ")
            estado = pedir_estado_inicial()

            if registrar_paciente(dnis, nombres, edades, diagnosticos, estados,
                                  dni, nombre, edad, diagnostico, estado):
                alergias.append("Ninguna")
                observaciones.append("Sin observaciones")
                evoluciones.append("Sin evolucion")
                print("Paciente registrado exitosamente.")
            else:
                print("Ya existe un paciente con ese DNI.")

        elif opcion == 2:
            dni = pedir_dni("Ingrese el DNI del paciente a buscar: ")
            mostrar_paciente(dnis, nombres, edades, diagnosticos, estados, dni)

        elif opcion == 3:
            mostrar_todos_los_pacientes(dnis, nombres, estados)

        elif opcion == 4:
            dni = pedir_dni("Ingrese el DNI del paciente a actualizar: ")
            nuevo_diagnostico = pedir_diagnostico("Ingrese el nuevo diagnostico: ")

            if actualizar_diagnostico(dnis, diagnosticos, dni, nuevo_diagnostico):
                print("Diagnostico actualizado exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 5:
            dni = pedir_dni("Ingrese el DNI del paciente a dar de alta: ")
            resultado = dar_alta(dnis, estados, dni)

            if resultado == 1:
                liberar_cama_por_dni(dni)
                print("Paciente dado de alta exitosamente.")
            elif resultado == 0:
                print("El paciente ya tiene el alta medica.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 6:
            mostrar_pacientes_internados(dnis, nombres, estados)

        elif opcion == 7:
            dni = pedir_dni("Ingrese el DNI del paciente a internar: ")
            resultado = internar_paciente(dnis, estados, dni)

            if resultado == 1:
                print("Paciente internado exitosamente.")
            elif resultado == 0:
                print("El paciente ya estaba internado.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif opcion == 8:
            menu_camas()

        elif opcion == 9:
            menu_registro_clinico()

        elif opcion == 0:
            print("Volviendo al menu principal...")

def guardar_datos():
    #Guarda los datos principales del sistema en JSON
    if json_archivos.guardar_sistema_json(
        "sistema_hospital.json",
        dnis,
        nombres,
        edades,
        diagnosticos,
        estados,
        alergias,
        observaciones,
        evoluciones,
        turnos,
        horarios,
        camas,
        numeros_camas
    ):
        print("Datos guardados correctamente.")
    else:
        print("No se pudieron guardar los datos.")


def cargar_datos():
    #Carga los datos principales del sistema desde JSON
    datos = json_archivos.cargar_sistema_json("sistema_hospital.json")

    if datos == None:
        print("No se pudieron cargar los datos.")
    else:
        datos_pacientes = datos[0]

        reemplazar_lista(dnis, datos_pacientes[0])
        reemplazar_lista(nombres, datos_pacientes[1])
        reemplazar_lista(edades, datos_pacientes[2])
        reemplazar_lista(diagnosticos, datos_pacientes[3])
        reemplazar_lista(estados, datos_pacientes[4])
        reemplazar_lista(alergias, datos_pacientes[5])
        reemplazar_lista(observaciones, datos_pacientes[6])
        reemplazar_lista(evoluciones, datos_pacientes[7])

        reemplazar_lista(turnos, datos[1])
        reemplazar_lista(horarios, datos[2])
        reemplazar_lista(camas, datos[3])
        reemplazar_lista(numeros_camas, datos[4])

        print("Datos cargados correctamente.")
# ------------------ MENU PRINCIPAL ------------------
def main():
    #Controla el menu principal del sistema
    opcion = -1

    while opcion != 0:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Ver turnos")
        print("2 - Reserva de turnos")
        print("3 - Modificar turnos")
        print("4 - Cancelacion de turnos")
        print("5 - Gestion de pacientes")
        print("6 - Guardar datos")
        print("7 - Cargar datos")
        print("0 - Salir")

        opcion = pedir_opcion("Opcion: ", 0, 7)

        if opcion == 1:
            mostrar_turnos()

        elif opcion == 2:
            asignar_turno()

        elif opcion == 3:
            modificar_turno()

        elif opcion == 4:
            cancelar_turno()

        elif opcion == 5:
            menu_pacientes()

        elif opcion == 6:
            guardar_datos()

        elif opcion == 7:
            cargar_datos()

        elif opcion == 0:
            guardar_datos()
            print("Saliendo del sistema...")

if __name__ == "__main__":
    main()
