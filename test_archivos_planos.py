import archivos_planos as archivos


def test_limpiar_campo_archivo():
    assert archivos.limpiar_campo_archivo("  Juan Perez  ") == "Juan Perez"
    assert archivos.limpiar_campo_archivo("Alergia;Penicilina") == "Alergia,Penicilina"


def test_armar_registro_paciente():
    registro = archivos.armar_registro_paciente(
        "12345678",
        "Juan Perez",
        30,
        "Control general",
        "Internado",
        "Ninguna",
        "Sin observaciones",
        "Sin evolucion"
    )

    assert registro == "12345678;Juan Perez;30;Control general;Internado;Ninguna;Sin observaciones;Sin evolucion\n"


def test_guardar_y_cargar_pacientes_csv(tmp_path):
    archivo = tmp_path / "pacientes.csv"

    dnis = ["12345678"]
    nombres = ["Juan Perez"]
    edades = [30]
    diagnosticos = ["Control general"]
    estados = ["Internado"]
    alergias = ["Ninguna"]
    observaciones = ["Sin observaciones"]
    evoluciones = ["Sin evolucion"]

    resultado_guardado = archivos.guardar_pacientes_csv(
        archivo,
        dnis,
        nombres,
        edades,
        diagnosticos,
        estados,
        alergias,
        observaciones,
        evoluciones
    )

    datos_cargados = archivos.cargar_pacientes_csv(archivo)

    assert resultado_guardado == True
    assert datos_cargados[0] == dnis
    assert datos_cargados[1] == nombres
    assert datos_cargados[2] == edades
    assert datos_cargados[3] == diagnosticos
    assert datos_cargados[4] == estados
    assert datos_cargados[5] == alergias
    assert datos_cargados[6] == observaciones
    assert datos_cargados[7] == evoluciones


def test_cargar_pacientes_csv_inexistente():
    resultado = archivos.cargar_pacientes_csv("archivo_inexistente.csv")

    assert resultado == None


def test_generar_reporte_pacientes_txt(tmp_path):
    archivo = tmp_path / "reporte.txt"

    resultado = archivos.generar_reporte_pacientes_txt(
        archivo,
        ["12345678"],
        ["Juan Perez"],
        [30],
        ["Control general"],
        ["Internado"]
    )

    contenido = archivo.read_text()

    assert resultado == True
    assert "REPORTE DE PACIENTES" in contenido
    assert "Cantidad total de pacientes: 1" in contenido
    assert "Juan Perez" in contenido


def test_registrar_movimiento_txt(tmp_path):
    archivo = tmp_path / "historial.txt"

    resultado = archivos.registrar_movimiento_txt(archivo, "Paciente registrado")

    contenido = archivo.read_text()

    assert resultado == True
    assert "Paciente registrado" in contenido
