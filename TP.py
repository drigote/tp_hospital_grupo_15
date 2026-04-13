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

# ------------------ TURNOS ------------------
dnis = []
nombres = []
edades = []
diagnosticos = []
estados = []
turnos = ["Libre", "Libre", "Libre", "Libre", "Libre"]
horarios = ["08:00", "09:00", "10:00", "11:00", "12:00"]

# ------------------ MENU PRINCIPAL ----------
opcion = -1

while opcion != 0:
    print("\n--- MENU PRINCIPAL ---")
    print("[1] Ver turnos disponibles")
    print("[2] Reserva de turnos")
    print("[3] Cancelación de turnos")
    print("[4] Gestion de pacientes")
    print("[0] Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("\n--- TURNOS DISPONIBLES ---")
        mostrar_turnos()

    elif opcion == 2:
        asignar_turnos()

    elif opcion == 3:
        cancelar_turno()

    elif opcion == 4:
        subopcion = -1
        while subopcion != 0:
            print("1 - Registrar paciente")
            print("2 - Buscar Paciente")
            print("3 - Mostrar todos los pacientes")
            print("4 - Actualizar diagnostico")
            print("5 - Dar alta")
            print("0 - Volver al menu principal")
            
            subopcion = int(input("Opcion: "))

            if subopcion == 1:
                dni = input("Ingrese el DNI del paciente: ")
                nombre = input("Ingrese el nombre del paciente: ")
                edad = int(input("Ingrese la edad del paciente: "))
                diagnostico = input("Ingrese el diagnóstico del paciente: ")

                if registrar_paciente(dni, nombre, edad, diagnostico):
                    print("Paciente registrado exitosamente.")
                else:
                    print("Ya existe un paciente con ese DNI.")
            
            elif subopcion == 2:
                dni = input("Ingrese el DNI del paciente a buscar: ")
                mostrar_paciente(dni)
            
            elif subopcion == 3:
                mostrar_todos_los_pacientes()
            
            elif subopcion == 4:
                dni = input("Ingrese el DNI del paciente a actualizar: ")
                nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ")

                if actualizar_diagnostico(dni, nuevo_diagnostico):
                    print("Diagnóstico actualizado exitosamente.")
                else:
                    print("No se encontró ningún paciente con ese DNI.")
            
            elif subopcion == 5:
                dni = input("Ingrese el DNI del paciente a dar de alta: ")
                resultado = dar_alta(dni)

                if resultado == 1:
                    print("Paciente dado de alta exitosamente.")
                elif resultado == 0:
                    print("El paciente ya tiene el alta médica.")
                else:
                    print("No se encontró ningún paciente con ese DNI.")
            
            elif subopcion == 0:
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    elif opcion == 5:
        turno_a_eliminar = input("Ingrese el turno a eliminar: ")

        if turno_a_eliminar in turnos:
            i = 0
            while i < len(turnos):
                if turnos[i] == turno_a_eliminar:
                    turnos.pop(i)
                    break
                i = i + 1

            print(f"Turno '{turno_a_eliminar}' eliminado exitosamente.")
        else:
            print("El turno no existe.")

    elif opcion == 6:
            
        if len(turnos) > 0:
            print("\n--- TURNOS AGENDADOS ---")
            i = 0
            while i < len(turnos):
                print("[", i + 1, "]", turnos[i])
                i = i + 1
        else:
            print("No hay turnos agendados.")
