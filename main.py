normalizar_nombre = lambda texto: texto.strip().title()
normalizar_texto = lambda texto: texto.strip()


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

    #Registra un paciente nuevo si el DNI no existe. Devuelve True si se registro y False si ya existia
    if buscar_paciente(dnis, dni) != -1:
        return False

    dnis.append(normalizar_texto(dni))
    nombres.append(normalizar_nombre(nombre))
    edades.append(edad)
    diagnosticos.append(normalizar_texto(diagnostico))
    estados.append(estado_inicial)

    return True


def mostrar_paciente(dnis, nombres, edades, diagnosticos, estados, dni_buscado):
    #Muestra por pantalla los datos de UN paciente buscado por DNI
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
    
# ------------------ DATOS ------------------
dnis = []
nombres = []
edades = []
diagnosticos = []
estados = []
turnos = ["Libre", "Libre", "Libre", "Libre", "Libre"]
horarios = ["08:00", "09:00", "10:00", "11:00", "12:00"]


def mostrar_turnos():
    #Muestra todos los turnos con su estado
    print("--- ESTADO DE LOS TURNOS ---")
    for i in range(len(horarios)):
        print(horarios[i], "->", turnos[i])


def asignar_turnos():
    #Asigna un turno si el horario existe y esta libre
    hora = input("Ingrese la hora del turno: ").strip()
    nombre = input("Ingrese el nombre del paciente: ").strip()

    while not validar_texto_no_vacio(nombre):
        print("Error. El nombre no puede estar vacio.")
        nombre = input("Ingrese el nombre del paciente: ").strip()

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] == "Libre":
                turnos[i] = nombre
                print("Turno asignado")
            else:
                print("Turno ocupado")
            return

    print("Horario inexistente")


def cancelar_turno():
    #Cancela un turno si el horario existe y esta ocupado
    hora = input("Ingrese la hora del turno a cancelar: ").strip()

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] != "Libre":
                turnos[i] = "Libre"
                print("Turno cancelado")
            else:
                print("El turno ya esta libre")
            return

    print("Horario inexistente")


def menu_pacientes():
    #Muestra el menu de gestion de pacientes
    subopcion = -1

    while subopcion != 0:
        print("\n--- GESTION DE PACIENTES ---")
        print("1 - Registrar paciente")
        print("2 - Buscar paciente")
        print("3 - Mostrar todos los pacientes")
        print("4 - Actualizar diagnostico")
        print("5 - Dar alta")
        print("6 - Mostrar pacientes internados")
        print("7 - Internar paciente")
        print("0 - Volver al menu principal")

        subopcion = pedir_opcion("Opcion: ", 0, 7)

        if subopcion == 1:
            dni = pedir_dni("Ingrese el DNI del paciente: ")
            nombre = pedir_nombre("Ingrese el nombre del paciente: ")
            edad = pedir_edad("Ingrese la edad del paciente: ")
            diagnostico = pedir_diagnostico("Ingrese el diagnostico del paciente: ")
            estado = pedir_estado_inicial()

            if registrar_paciente(dnis, nombres, edades, diagnosticos, estados,
                                  dni, nombre, edad, diagnostico, estado):
                print("Paciente registrado exitosamente.")
            else:
                print("Ya existe un paciente con ese DNI.")

        elif subopcion == 2:
            dni = pedir_dni("Ingrese el DNI del paciente a buscar: ")
            mostrar_paciente(dnis, nombres, edades, diagnosticos, estados, dni)

        elif subopcion == 3:
            mostrar_todos_los_pacientes(dnis, nombres, estados)

        elif subopcion == 4:
            dni = pedir_dni("Ingrese el DNI del paciente a actualizar: ")
            nuevo_diagnostico = pedir_diagnostico("Ingrese el nuevo diagnostico: ")

            if actualizar_diagnostico(dnis, diagnosticos, dni, nuevo_diagnostico):
                print("Diagnostico actualizado exitosamente.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 5:
            dni = pedir_dni("Ingrese el DNI del paciente a dar de alta: ")
            resultado = dar_alta(dnis, estados, dni)

            if resultado == 1:
                print("Paciente dado de alta exitosamente.")
            elif resultado == 0:
                print("El paciente ya tiene el alta medica.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 6:
            mostrar_pacientes_internados(dnis, nombres, estados)

        elif subopcion == 7:
            dni = pedir_dni("Ingrese el DNI del paciente a internar: ")
            resultado = internar_paciente(dnis, estados, dni)

            if resultado == 1:
                print("Paciente internado exitosamente.")
            elif resultado == 0:
                print("El paciente ya estaba internado.")
            else:
                print("No se encontro ningun paciente con ese DNI.")

        elif subopcion == 0:
            print("Volviendo al menu principal...")


def main():
    #Controla el menu principal del sistema
    opcion = -1

    while opcion != 0:
        print("\n--- MENU PRINCIPAL ---")
        print("[1] Ver turnos disponibles")
        print("[2] Reserva de turnos")
        print("[3] Cancelacion de turnos")
        print("[4] Gestion de pacientes")
        print("[0] Salir")

        opcion = pedir_opcion("Opcion: ", 0, 4)

        if opcion == 1:
            print("\n--- TURNOS DISPONIBLES ---")
            mostrar_turnos()

        elif opcion == 2:
            asignar_turnos()

        elif opcion == 3:
            cancelar_turno()

        elif opcion == 4:
            menu_pacientes()

        elif opcion == 0:
            print("Saliendo del sistema...")


if __name__ == "__main__":
    main()
