# ------------------ TURNOS ------------------

turnos = []
turnos_disponibles = ["Lunes 08:00", "Lunes 09:00", "Lunes 10:00", "Martes 08:00", "Martes 09:00", "Martes 10:00", "Miercoles 08:00", "Miercoles 09:00", "Miercoles 10:00", "Jueves 08:00", "Jueves 09:00", "Jueves 10:00", "Viernes 08:00", "Viernes 09:00", "Viernes 10:00"]

# ------------------ MENU PRINCIPAL ----------
opcion = -1

while opcion != 0:
    print("\n--- MENU PRINCIPAL ---")
    print("[1] Ver turnos disponibles")
    print("[2] Reserva de turnos")
    print("[3] Gestion de pacientes")
    print("[4] Gestion de camas")
    print("[5] Registro Clinico")
    print("[0] Salir")

    op = int(input("Opcion: "))
    # ----------TURNOS-------------
    if op == 1:
        print("\n--- TURNOS DISPONIBLES ---")

        hay_disponibles = False
        i = 0
        while i < len(turnos_disponibles):
            if turnos_disponibles[i] not in turnos:
                print("-", turnos_disponibles[i])
                hay_disponibles = True
            i = i + 1

        if not hay_disponibles:
            print("No hay turnos disponibles.")
        elif op == 2:
            turno = input("Ingrese el turno a agendar: ")

            if turno in turnos_disponibles and turno not in turnos:
                turnos.append(turno)
                print(f"Turno '{turno}' agendado exitosamente.")
            else:
                print("Turno inválido o ya ocupado.")

        elif op == 3:
            turno_actual = input("Ingrese el turno a modificar: ")

            if turno_actual in turnos:
                nuevo_turno = input("Ingrese el nuevo turno: ")

                if nuevo_turno in turnos_disponibles and nuevo_turno not in turnos:
                    i = 0
                    while i < len(turnos):
                        if turnos[i] == turno_actual:
                            turnos[i] = nuevo_turno
                        i = i + 1

                    print(f"Turno '{turno_actual}' modificado a '{nuevo_turno}'.")
                else:
                    print("El nuevo turno no es válido o ya está ocupado.")
            else:
                print("El turno no existe.")
            
        elif op == 4:
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

        elif op == 5:
            
            if len(turnos) > 0:
                print("\n--- TURNOS AGENDADOS ---")
                i = 0
                while i < len(turnos):
                    print("[", i + 1, "]", turnos[i])
                    i = i + 1
            else:
                print("No hay turnos agendados.")