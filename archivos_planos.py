def limpiar_campo_archivo(texto):
    #Limpia un campo para guardarlo en un archivo separado por punto y coma
    texto = str(texto).strip()
    texto = texto.replace(";", ",")
    texto = texto.replace("\n", " ")
    return texto


def armar_registro_paciente(dni, nombre, edad, diagnostico, estado, alergias, observaciones, evolucion):
    #Arma una linea de texto con los datos de un paciente
    registro = limpiar_campo_archivo(dni) + ";"
    registro = registro + limpiar_campo_archivo(nombre) + ";"
    registro = registro + limpiar_campo_archivo(edad) + ";"
    registro = registro + limpiar_campo_archivo(diagnostico) + ";"
    registro = registro + limpiar_campo_archivo(estado) + ";"
    registro = registro + limpiar_campo_archivo(alergias) + ";"
    registro = registro + limpiar_campo_archivo(observaciones) + ";"
    registro = registro + limpiar_campo_archivo(evolucion) + "\n"

    return registro


def guardar_pacientes_csv(nombre_archivo, dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones):
    #Guarda los pacientes en un archivo csv usando ; como separador
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("dni;nombre;edad;diagnostico;estado;alergias;observaciones;evolucion\n")

            for i in range(len(dnis)):
                registro = armar_registro_paciente(
                    dnis[i],
                    nombres[i],
                    edades[i],
                    diagnosticos[i],
                    estados[i],
                    alergias[i],
                    observaciones[i],
                    evoluciones[i]
                )

                archivo.write(registro)

        return True
    except OSError:
        return False


def cargar_pacientes_csv(nombre_archivo):
    #Carga pacientes desde un archivo csv y devuelve las listas
    dnis = []
    nombres = []
    edades = []
    diagnosticos = []
    estados = []
    alergias = []
    observaciones = []
    evoluciones = []

    try:
        with open(nombre_archivo, "r") as archivo:
            archivo.readline()

            for linea in archivo:
                linea = linea.strip()

                if linea != "":
                    datos = linea.split(";")

                    if len(datos) == 8:
                        dnis.append(datos[0])
                        nombres.append(datos[1])

                        try:
                            edades.append(int(datos[2]))
                        except ValueError:
                            edades.append(0)

                        diagnosticos.append(datos[3])
                        estados.append(datos[4])
                        alergias.append(datos[5])
                        observaciones.append(datos[6])
                        evoluciones.append(datos[7])

        return dnis, nombres, edades, diagnosticos, estados, alergias, observaciones, evoluciones
    except OSError:
        return None


def generar_reporte_pacientes_txt(nombre_archivo, dnis, nombres, edades, diagnosticos, estados):
    #Genera un reporte de pacientes en formato txt
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("REPORTE DE PACIENTES\n")
            archivo.write("--------------------\n")
            archivo.write("Cantidad total de pacientes: " + str(len(dnis)) + "\n\n")

            for i in range(len(dnis)):
                archivo.write("DNI: " + limpiar_campo_archivo(dnis[i]) + "\n")
                archivo.write("Nombre: " + limpiar_campo_archivo(nombres[i]) + "\n")
                archivo.write("Edad: " + limpiar_campo_archivo(edades[i]) + "\n")
                archivo.write("Diagnostico: " + limpiar_campo_archivo(diagnosticos[i]) + "\n")
                archivo.write("Estado: " + limpiar_campo_archivo(estados[i]) + "\n")
                archivo.write("--------------------\n")

        return True
    except OSError:
        return False


def registrar_movimiento_txt(nombre_archivo, descripcion):
    #Agrega un movimiento al archivo de historial
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(limpiar_campo_archivo(descripcion) + "\n")

        return True
    except OSError:
        return False
