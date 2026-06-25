# ==============================================================================
# ------------------ DATOS DEL SISTEMA -----------------
# ==============================================================================

# --- MÓDULO TURNOS ---
turnos_disponibles = [
    "Lunes 08:00", "Lunes 09:00", "Lunes 10:00", 
    "Martes 08:00", "Martes 09:00", "Martes 10:00", 
    "Miercoles 08:00", "Miercoles 09:00", "Miercoles 10:00", 
    "Jueves 08:00", "Jueves 09:00", "Jueves 10:00", 
    "Viernes 08:00", "Viernes 09:00", "Viernes 10:00"
]
turnos = ["Libre"] * len(turnos_disponibles)

# --- MÓDULO CAMAS ---
numeros_camas = [1, 2, 3, 4, 5]
camas = ["Libre", "Libre", "Libre", "Libre", "Libre"]


# ==============================================================================
# ------------------ FUNCIONES DE CONVERSIÓN A DICCIONARIOS -------------------
# ==============================================================================

def convertir_turnos_diccionario(horas_disponibles, estados_turnos):
    """Convierte las listas paralelas de turnos en un diccionario (Día/Hora -> Estado)."""
    turnos_dict = {}
    i = 0
    while i < len(horas_disponibles):
        turnos_dict[horas_disponibles[i]] = estados_turnos[i]
        i = i + 1
    return turnos_dict


def convertir_camas_diccionario(numeros, estados_camas):
    """Convierte las listas paralelas de camas en un diccionario (Número -> Estado/DNI)."""
    camas_dict = {}
    i = 0
    while i < len(numeros):
        camas_dict[numeros[i]] = estados_camas[i]
        i = i + 1
    return camas_dict


# ==============================================================================
# ------------------ NUEVAS FUNCIONES DE GESTIÓN DE CAMAS ---------------------
# ==============================================================================

def mostrar_camas():
    """Muestra el estado de las camas formateado desde su diccionario."""
    dict_camas = convertir_camas_diccionario(numeros_camas, camas)
    
    print("\n--- ESTADO DE LAS CAMAS ---")
    for num_cama, estado in dict_camas.items():
        if estado == "Libre":
            print(f"Cama {num_cama} -> Libre")
        else:
            print(f"Cama {num_cama} -> Ocupada por DNI: {estado}")


def asignar_cama():
    """Asigna una cama libre chequeando disponibilidad en el diccionario."""
    dni = pedir_dni("Ingrese el DNI del paciente a asignar cama: ")
    indice_paciente = buscar_paciente(dnis, dni)

    if indice_paciente == -1:
        print("No se encontro ningun paciente con ese DNI.")
        return

    if estados[indice_paciente] != "Internado":
        print("El paciente no esta internado, no se le puede asignar una cama.")
        return

    dict_camas = convertir_camas_diccionario(numeros_camas, camas)
    
    # Validar si ya tiene cama asignada
    for num_cama, estado in dict_camas.items():
        if estado == dni:
            print(
