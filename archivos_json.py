import json

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

def convertir_pacientes_a_diccionarios(dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones):
    pacientes = []
    for i in range(len(dnis)):
        paciente = {
            "dni": dnis[i],
            "nombre": nombres[i],
            "edad": edades[i],
            "diagnostico": diagnosticos[i],
            "estado": estados[i],
            "alergias": alergias[i],
            "observaciones": observaciones[i],
            "evolucion": evoluciones[i]
        }
        pacientes.append(paciente)
    return pacientes


def convertir_diccionarios_a_listas(pacientes):
    dnis = []
    nombres = []
    edades = []
    diagnosticos = []
    estados = []
    alergias = []
    observaciones = []
    evoluciones = []

    for paciente in pacientes:
        dnis.append(paciente["dni"])
        nombres.append(paciente["nombre"])
        edades.append(paciente["edad"])
        diagnosticos.append(paciente["diagnostico"])
        estados.append(paciente["estado"])
        alergias.append(paciente["alergias"])
        observaciones.append(paciente["observaciones"])
        evoluciones.append(paciente["evolucion"])

    return dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones


def guardar_pacientes_json(nombre_archivo, dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones):
    try:
        pacientes = convertir_pacientes_a_diccionarios(
            dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones
        )
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(pacientes, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        return False


def cargar_pacientes_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            pacientes = json.load(archivo)
        return convertir_diccionarios_a_listas(pacientes)
    except (OSError, json.JSONDecodeError, KeyError):
        return None


def convertir_sistema_a_diccionario(dnis, nombres, edades, diagnosticos, estados,
                                    alergias, observaciones, evoluciones,
                                    turnos_disponibles, turnos, camas, numeros_camas):
    sistema = {
        "pacientes": convertir_pacientes_a_diccionarios(
            dnis, nombres, edades, diagnosticos, estados,
            alergias, observaciones, evoluciones
        ),
        "turnos_semanales": convertir_turnos_diccionario(turnos_disponibles, turnos),
        "camas_hospital": convertir_camas_diccionario(numeros_camas, camas)
    }
    return sistema


def guardar_sistema_json(nombre_archivo, dnis, nombres, edades, diagnosticos, estados,
                         alergias, observaciones, evoluciones,
                         turnos_disponibles, turnos, camas, numeros_camas):
    try:
        sistema = convertir_sistema_a_diccionario(
            dnis, nombres, edades, diagnosticos, estados,
            alergias, observaciones, evoluciones,
            turnos_disponibles, turnos, camas, numeros_camas
        )
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(sistema, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        return False


def cargar_sistema_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            sistema = json.load(archivo)

        datos_pacientes = convertir_diccionarios_a_listas(sistema["pacientes"])

    
        dict_turnos = sistema["turnos_semanales"]
        turnos_disponibles = list(dict_turnos.keys())
        turnos = list(dict_turnos.values())

      
        dict_camas = sistema["camas_hospital"]
        numeros_camas = list(map(int, dict_camas.keys()))
    except Exception as e:
        print(f"Error al cargar el sistema desde el archivo JSON: {e}")
        return None
