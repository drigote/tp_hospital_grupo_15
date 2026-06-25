import archivos_json as archivos


def test_convertir_pacientes_a_diccionarios():
    pacientes = archivos.convertir_pacientes_a_diccionarios(
        ["12345678"],
        ["Juan Perez"],
        [30],
        ["Control general"],
        ["Internado"],
        ["Ninguna"],
        ["Sin observaciones"],
        ["Sin evolucion"]
    )

    assert len(pacientes) == 1
    assert pacientes[0]["dni"] == "12345678"
    assert pacientes[0]["nombre"] == "Juan Perez"
    assert pacientes[0]["edad"] == 30
    assert pacientes[0]["estado"] == "Internado"


def test_convertir_diccionarios_a_listas():
    pacientes = [
        {
            "dni": "12345678",
            "nombre": "Juan Perez",
            "edad": 30,
            "diagnostico": "Control general",
            "estado": "Internado",
            "alergias": "Ninguna",
            "observaciones": "Sin observaciones",
            "evolucion": "Sin evolucion"
        }
    ]

    datos = archivos.convertir_diccionarios_a_listas(pacientes)

    assert datos[0] == ["12345678"]
    assert datos[1] == ["Juan Perez"]
    assert datos[2] == [30]
    assert datos[3] == ["Control general"]
    assert datos[4] == ["Internado"]
    assert datos[5] == ["Ninguna"]
    assert datos[6] == ["Sin observaciones"]
    assert datos[7] == ["Sin evolucion"]


def test_guardar_y_cargar_pacientes_json(tmp_path):
    archivo = tmp_path / "pacientes.json"

    dnis = ["12345678"]
    nombres = ["Juan Perez"]
    edades = [30]
    diagnosticos = ["Control general"]
    estados = ["Internado"]
    alergias = ["Ninguna"]
    observaciones = ["Sin observaciones"]
    evoluciones = ["Sin evolucion"]

    resultado_guardado = archivos.guardar_pacientes_json(
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

    datos_cargados = archivos.cargar_pacientes_json(archivo)

    assert resultado_guardado == True
    assert datos_cargados[0] == dnis
    assert datos_cargados[1] == nombres
    assert datos_cargados[2] == edades
    assert datos_cargados[3] == diagnosticos
    assert datos_cargados[4] == estados
    assert datos_cargados[5] == alergias
    assert datos_cargados[6] == observaciones
    assert datos_cargados[7] == evoluciones


def test_cargar_pacientes_json_inexistente():
    resultado = archivos.cargar_pacientes_json("pacientes_inexistente.json")

    assert resultado == None


def test_convertir_sistema_a_diccionario():
    sistema = archivos.convertir_sistema_a_diccionario(
        ["12345678"],
        ["Juan Perez"],
        [30],
        ["Control general"],
        ["Internado"],
        ["Ninguna"],
        ["Sin observaciones"],
        ["Sin evolucion"],
        ["Libre"],
        ["08:00"],
        ["Libre"],
        [1]
    )

    assert "pacientes" in sistema
    assert "turnos" in sistema
    assert "horarios" in sistema
    assert "camas" in sistema
    assert "numeros_camas" in sistema
    assert sistema["pacientes"][0]["dni"] == "12345678"
    assert sistema["horarios"] == ["08:00"]


def test_guardar_y_cargar_sistema_json(tmp_path):
    archivo = tmp_path / "sistema.json"

    resultado_guardado = archivos.guardar_sistema_json(
        archivo,
        ["12345678"],
        ["Juan Perez"],
        [30],
        ["Control general"],
        ["Internado"],
        ["Ninguna"],
        ["Sin observaciones"],
        ["Sin evolucion"],
        ["Libre"],
        ["08:00"],
        ["Libre"],
        [1]
    )

    resultado_cargado = archivos.cargar_sistema_json(archivo)

    datos_pacientes = resultado_cargado[0]
    turnos = resultado_cargado[1]
    horarios = resultado_cargado[2]
    camas = resultado_cargado[3]
    numeros_camas = resultado_cargado[4]

    assert resultado_guardado == True
    assert datos_pacientes[0] == ["12345678"]
    assert datos_pacientes[1] == ["Juan Perez"]
    assert turnos == ["Libre"]
    assert horarios == ["08:00"]
    assert camas == ["Libre"]
    assert numeros_camas == [1]


def test_cargar_sistema_json_inexistente():
    resultado = archivos.cargar_sistema_json("sistema_inexistente.json")

    assert resultado == None
