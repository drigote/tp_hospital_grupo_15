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


def contar_pacientes_por_estado_recursivo(estados, estado_buscado, indice=0):
    #Cuenta pacientes por estado usando recursividad
    if indice == len(estados):
        return 0
    else:
        if estados[indice] == estado_buscado:
            return 1 + contar_pacientes_por_estado_recursivo(estados, estado_buscado, indice + 1)
        else:
            return contar_pacientes_por_estado_recursivo(estados, estado_buscado, indice + 1)


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
