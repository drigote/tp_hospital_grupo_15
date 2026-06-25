import json


def convertir_pacientes_a_diccionarios(dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones):
    #Convierte las listas paralelas de pacientes en una lista de diccionarios
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
    #Convierte una lista de diccionarios en listas paralelas
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
    #Guarda los pacientes en un archivo json
    try:
        pacientes = convertir_pacientes_a_diccionarios(
            dnis,
            nombres,
            edades,
            diagnosticos,
            estados,
            alergias,
            observaciones,
            evoluciones
        )

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(pacientes, archivo, indent=4, ensure_ascii=False)

        return True
    except OSError:
        return False


def cargar_pacientes_json(nombre_archivo):
    #Carga los pacientes desde un archivo json
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            pacientes = json.load(archivo)

        return convertir_diccionarios_a_listas(pacientes)
    except OSError:
        return None
    except json.JSONDecodeError:
        return None
    except KeyError:
        return None


def convertir_sistema_a_diccionario(dnis, nombres, edades, diagnosticos, estados,
                                    alergias, observaciones, evoluciones,
                                    turnos, horarios, camas, numeros_camas):
    #Convierte los datos principales del sistema en un diccionario
    sistema = {
        "pacientes": convertir_pacientes_a_diccionarios(
            dnis,
            nombres,
            edades,
            diagnosticos,
            estados,
            alergias,
            observaciones,
            evoluciones
        ),
        "turnos": turnos,
        "horarios": horarios,
        "camas": camas,
        "numeros_camas": numeros_camas
    }

    return sistema


def guardar_sistema_json(nombre_archivo, dnis, nombres, edades, diagnosticos, estados,
                         alergias, observaciones, evoluciones,
                         turnos, horarios, camas, numeros_camas):
    #Guarda los datos principales del sistema en un archivo json
    try:
        sistema = convertir_sistema_a_diccionario(
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
        )

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(sistema, archivo, indent=4, ensure_ascii=False)

        return True
    except OSError:
        return False


def cargar_sistema_json(nombre_archivo):
    #Carga los datos principales del sistema desde un archivo json
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            sistema = json.load(archivo)

        datos_pacientes = convertir_diccionarios_a_listas(sistema["pacientes"])

        turnos = sistema["turnos"]
        horarios = sistema["horarios"]
        camas = sistema["camas"]
        numeros_camas = sistema["numeros_camas"]

        return datos_pacientes, turnos, horarios, camas, numeros_camas
    except OSError:
        return None
    except json.JSONDecodeError:
        return None
    except KeyError:
        return None
