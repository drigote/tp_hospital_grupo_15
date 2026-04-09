opcion = -1:

while opcion != 0:
    print("\n--- MENU PRINCIPAL ---")
    print("[1] Gestion de turnos")
    print("[2] Gestion de pacientes")
    print("[3] Gestion de camas")
    print("[4] Registro Clinico")
    print("[0] Salir")

    opcion = int(input("Opcion: "))
    # ----------TURNOS-------------
    if opcion == 1:
        op = -1
        while op != 0:
            print("\n--- GESTION DE TURNOS ---")
            print("[1] Agendar turno")
            print("[2] Modificar turno")
            print("[3] Eliminar turno")
            print("[4] Listar turnos")
            print("[0] Volver al menu principal")

            op = int(input("Opcion: "))

            if op == 1:
                turno = input("Ingrese el turno a agendar: ")
                turnos.append(turno)
                print(f"Turno '{turno}' agendado exitosamente.")

            elif op == 2:
                turno_actual = input("Ingrese el turno a modificar: ")
                if turno_actual in turnos:
                    nuevo_turno = input("Ingrese el nuevo turno:")
                    
                    i = 0
                    while i < len(turnos):
                        if turnos[i] == turno_actual:
                            turnos[i] = nuevo_turno
                            print(f"Turno '{turno_actual}' modifica a '{nuevo_turno}' exitosamente.")
                        else:
                            print("El turno no existe.")

            elif op == 3:
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
            elif op == 4:
                if len(turnos) > 0:
                    print("\n--- TURNOS AGENDADOS ---")
                    
                    i = 0
                    while i < len(turnos):
                        print("[", i + 1, "]", turnos[i])
                        i = i + 1
                else:
                    print("No hay turnos agendados.")