# ==============================================================================
# ------------------ DATOS DEL SISTEMA: TURNOS -----------------------
# ==============================================================================

turnos_disponibles = [
    "Lunes 08:00", "Lunes 09:00", "Lunes 10:00", 
    "Martes 08:00", "Martes 09:00", "Martes 10:00", 
    "Miercoles 08:00", "Miercoles 09:00", "Miercoles 10:00", 
    "Jueves 08:00", "Jueves 09:00", "Jueves 10:00", 
    "Viernes 08:00", "Viernes 09:00", "Viernes 10:00"
]
# Lista paralela: almacena "Libre" o el nombre del paciente asignado
turnos = ["Libre"] * len(turnos_disponibles)


# ==============================================================================
# ------------------ FUNCIONES DE CONVERSIÓN Y VALIDACIÓN ----------------------
# ==============================================================================

def convertir_turnos_diccionario(horas_disponibles, estados_turnos):
    """
    Convierte las listas paralelas en un diccionario estructurado (tipo _camas_diccionarios).
    Mapea cada turno (Día y Hora) con su estado actual (Libre o Paciente).
    """
    turnos_dict = {}
    i = 0
    while i < len(horas_disponibles):
        turnos_dict[horas_disponibles[i]] = estados_turnos[i]
        i = i + 1
    return turnos_dict


def pedir_turno_disponible(mensaje):
    """Valida que el turno ingresado exista textualmente en el cronograma semanal."""
    turno = input(mensaje).strip()
    
    i = 0
    while i < len(turnos_disponibles):
        if turnos_disponibles[i].lower() == turno.lower():
            return turnos_disponibles[i]  # Devuelve el formato idéntico de la lista
        i = i + 1
    
    print("Error. El turno no existe en el cronograma. Ejemplo válido: 'Lunes 08:00'")
    return pedir_turno_disponible(mensaje)


# ==============================================================================
# ------------------ GESTIÓN DE TURNOS ------------
# ==============================================================================

def mostrar_turnos():
    """Muestra el estado de todos los turnos semanales usando el diccionario."""
    dict_actual = convertir_turnos_diccionario(turnos_disponibles, turnos)
    
    print("\n--- ESTADO DE LOS TURNOS SEMANALES ---")
    hay_disponibles = False
    
    for turno, estado in dict_actual.items():
        if estado == "Libre":
            print(f"- {turno}: Libre")
            hay_disponibles = True
        else:
            print(f"- {turno}: Ocupado por {estado}")

    if not hay_disponibles:
        print("No hay turnos disponibles.")


def asignar_turno():
    """Reserva un turno validando la disponibilidad mediante el diccionario."""
    print("\n--- RESERVA DE TURNOS ---")
    turno_elegido = pedir_turno_disponible("Ingrese el día y hora a agendar: ")
    
    # Verificamos la disponibilidad en el mapa del diccionario
    dict_actual = convertir_turnos_diccionario(turnos_disponibles, turnos)
    
    if dict_actual[turno_elegido] == "Libre":
        nombre_paciente = pedir_nombre("Ingrese el nombre del paciente: ")
        
        # Buscamos el índice correspondiente para impactar de forma persistente en la lista
        i = 0
        while i < len(turnos_disponibles):
            if turnos_disponibles[i] == turno_elegido:
                turnos[i] = nombre_paciente
                print(f"Turno '{turno_elegido}' agendado para {nombre_paciente} exitosamente.")
                break
            i = i + 1
    else:
        print("El turno ya está ocupado por otro paciente.")


def modificar_turno():
    """Modifica un turno activo por otro libre usando la estructura mapeada."""
    print("\n--- MODIFICAR TURNO ---")
    turno_actual = pedir_turno_disponible("Ingrese el turno a modificar: ")
    dict_actual = convertir_turnos_diccionario(turnos_disponibles, turnos)
    
    if dict_actual[turno_actual] == "Libre":
        print("Ese turno está libre, no hay ninguna reserva para modificar.")
        return
        
    nombre_paciente = dict_actual[turno_actual]
    turno_nuevo = pedir_turno_disponible("Ingrese el nuevo turno deseado: ")
    
    # Validamos el estado del nuevo turno usando el diccionario
    if dict_actual[turno_nuevo] == "Libre":
        i = 0
        while i < len(turnos_disponibles):
            if turnos_disponibles[i] == turno_actual:
                turnos[i] = "Libre"
            if turnos_disponibles[i] == turno_nuevo:
                turnos[i] = nombre_paciente
            i = i + 1
        print(f"Turno modificado correctamente de '{turno_actual}' a '{turno_nuevo}'.")
    else:
        print("El nuevo turno ya está ocupado.")


def cancelar_turno():
    """Cancela una reserva activa chequeando el diccionario."""
    print("\n--- CANCELACIÓN DE TURNO ---")
    turno_a_eliminar = pedir_turno_disponible("Ingrese el turno a cancelar: ")
    dict_actual = convertir_turnos_diccionario(turnos_disponibles, turnos)
    
    if dict_actual[turno_a_eliminar] != "Libre":
        i = 0
        while i < len(turnos_disponibles):
            if turnos_disponibles[i] == turno_a_eliminar:
                turnos[i] = "Libre"
                print(f"Turno '{turno_a_eliminar}' liberado exitosamente.")
                break
            i = i + 1
    else:
        print("El turno ya estaba libre.")
