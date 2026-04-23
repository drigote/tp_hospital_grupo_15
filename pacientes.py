def mostrar_turnos():
    print("--- ESTADO DE LOS TURNOS ---")
    for i in range(len(horarios)):
        print(horarios[i], "->", turnos[i])

def asignar_turnos():
    hora = input("Ingrese la hora del turno: ")
    nombre = input("Ingrese el nombre del paciente: ")

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] == "Libre":
                turnos[i] = nombre
                print("Turno asignado")
            else:
                print("Turno Ocupado")
            return
    print("Horario inexistente")

def cancelar_turno():
    hora = input("Ingrese la hora del turno a cancelar: ")

    for i in range(len(horarios)):
        if horarios[i] == hora:
            if turnos[i] != "Libre":
                turnos[i] = "Libre"
                print("Turno cancelado")
            else:
                print("El turno ya está libre")
            return
    print("Horario inexistente")

def contar_lista(lista):
    contador = 0
    for elemento in lista:
        contador = contador + 1
    return contador

def buscar_paciente(dni_buscado):
    i = 0
    while i < len(dnis) and dnis[i] != dni_buscado:
        i = i + 1

    if i < len(dnis):
        return i
    else:
        return -1

def registrar_paciente(dni, nombre, edad, diagnostico):
    if buscar_paciente(dni) != -1:
        return False

    nombre_limpio = nombre.strip().title()
    diagnostico_limpio = diagnostico.strip()

    dnis.append(dni)
    nombres.append(nombre_limpio)
    edades.append(edad)
    diagnosticos.append(diagnostico_limpio)
    estados.append("Internado")

    return True

def mostrar_paciente(dni_buscado):
    indice = buscar_paciente(dni_buscado)

    if indice == -1:
        print("No se encontró ningún paciente con ese DNI.")
    else:
        print("----- DATOS DEL PACIENTE -----")
        print("DNI:", dnis[indice])
        print("Nombre:", nombres[indice])
        print("Edad:", edades[indice])
        print("Diagnóstico:", diagnosticos[indice])
        print("Estado:", estados[indice])
        print("------------------------------")

def mostrar_todos_los_pacientes():
    total = contar_lista(dnis)

    if total == 0:
        print("No hay pacientes cargados.")
    else:
        print("----- LISTA DE PACIENTES -----")
        i = 0
        while i < total:
            print("DNI:", dnis[i], "- Nombre:", nombres[i], "- Estado:", estados[i])
            i = i + 1
        print("------------------------------")

def actualizar_diagnostico(dni_buscado, nuevo_diagnostico):
    indice = buscar_paciente(dni_buscado)

    if indice == -1:
        return False
    else:
        diagnostico_limpio = nuevo_diagnostico.strip()
        diagnosticos[indice] = diagnostico_limpio
        return True

def dar_alta(dni_buscado):
    indice = buscar_paciente(dni_buscado)

    if indice == -1:
        return -1
    else:
        if estados[indice] == "Alta médica":
            return 0
        else:
            estados[indice] = "Alta médica"
            return 1


def esta_internado(dni_buscado):
    indice = buscar_paciente(dni_buscado)

    if indice == -1:
        return False
    else:
        if estados[indice] == "Internado":
            return True
        else:
            return False