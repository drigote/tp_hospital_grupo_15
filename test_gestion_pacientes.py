import gestion_pacientes as gp


def test_contar_lista():
    assert gp.contar_lista([]) == 0
    assert gp.contar_lista(["a", "b", "c"]) == 3


def test_buscar_paciente():
    dnis = ["12345678", "87654321", "11222333"]

    assert gp.buscar_paciente(dnis, "12345678") == 0
    assert gp.buscar_paciente(dnis, " 87654321 ") == 1
    assert gp.buscar_paciente(dnis, "99999999") == -1


def test_registrar_paciente():
    dnis = []
    nombres = []
    edades = []
    diagnosticos = []
    estados = []

    resultado = gp.registrar_paciente(
        dnis, nombres, edades, diagnosticos, estados,
        "12345678", "juan perez", 30, "control general", "Internado"
    )

    assert resultado == True
    assert dnis == ["12345678"]
    assert nombres == ["Juan Perez"]
    assert edades == [30]
    assert diagnosticos == ["control general"]
    assert estados == ["Internado"]


def test_registrar_paciente_repetido():
    dnis = ["12345678"]
    nombres = ["Juan Perez"]
    edades = [30]
    diagnosticos = ["control general"]
    estados = ["Internado"]

    resultado = gp.registrar_paciente(
        dnis, nombres, edades, diagnosticos, estados,
        "12345678", "otro nombre", 40, "otro diagnostico", "Ambulatorio"
    )

    assert resultado == False
    assert len(dnis) == 1
    assert nombres[0] == "Juan Perez"


def test_obtener_resumenes_pacientes():
    dnis = ["12345678", "87654321"]
    nombres = ["Juan Perez", "Ana Gomez"]
    estados = ["Internado", "Ambulatorio"]

    resumenes = gp.obtener_resumenes_pacientes(dnis, nombres, estados)

    assert resumenes[0] == "DNI: 12345678 - Nombre: Juan Perez - Estado: Internado"
    assert resumenes[1] == "DNI: 87654321 - Nombre: Ana Gomez - Estado: Ambulatorio"


def test_actualizar_diagnostico():
    dnis = ["12345678"]
    diagnosticos = ["control general"]

    resultado = gp.actualizar_diagnostico(dnis, diagnosticos, "12345678", "gripe")

    assert resultado == True
    assert diagnosticos[0] == "gripe"


def test_actualizar_diagnostico_paciente_inexistente():
    dnis = ["12345678"]
    diagnosticos = ["control general"]

    resultado = gp.actualizar_diagnostico(dnis, diagnosticos, "99999999", "gripe")

    assert resultado == False
    assert diagnosticos[0] == "control general"


def test_internar_paciente():
    dnis = ["12345678", "87654321"]
    estados = ["Ambulatorio", "Internado"]

    resultado = gp.internar_paciente(dnis, estados, "12345678")
    resultado_repetido = gp.internar_paciente(dnis, estados, "87654321")
    resultado_inexistente = gp.internar_paciente(dnis, estados, "99999999")

    assert resultado == 1
    assert estados[0] == "Internado"
    assert resultado_repetido == 0
    assert resultado_inexistente == -1


def test_dar_alta():
    dnis = ["12345678", "87654321"]
    estados = ["Internado", "Alta medica"]

    resultado = gp.dar_alta(dnis, estados, "12345678")
    resultado_repetido = gp.dar_alta(dnis, estados, "87654321")
    resultado_inexistente = gp.dar_alta(dnis, estados, "99999999")

    assert resultado == 1
    assert estados[0] == "Alta medica"
    assert resultado_repetido == 0
    assert resultado_inexistente == -1


def test_esta_internado():
    dnis = ["12345678", "87654321"]
    estados = ["Internado", "Ambulatorio"]

    assert gp.esta_internado(dnis, estados, "12345678") == True
    assert gp.esta_internado(dnis, estados, "87654321") == False
    assert gp.esta_internado(dnis, estados, "99999999") == False


def test_obtener_indices_internados():
    estados = ["Internado", "Ambulatorio", "Internado", "Alta medica"]

    assert gp.obtener_indices_internados(estados) == [0, 2]


def test_actualizar_alergias():
    dnis = ["12345678"]
    alergias = ["Ninguna"]

    resultado = gp.actualizar_alergias(dnis, alergias, "12345678", "Penicilina")

    assert resultado == True
    assert alergias[0] == "Penicilina"


def test_actualizar_alergias_paciente_inexistente():
    dnis = ["12345678"]
    alergias = ["Ninguna"]

    resultado = gp.actualizar_alergias(dnis, alergias, "99999999", "Penicilina")

    assert resultado == False
    assert alergias[0] == "Ninguna"


def test_agregar_observacion():
    dnis = ["12345678"]
    observaciones = ["Sin observaciones"]

    resultado = gp.agregar_observacion(dnis, observaciones, "12345678", "Paciente estable")

    assert resultado == True
    assert observaciones[0] == "Paciente estable"


def test_agregar_observacion_acumulada():
    dnis = ["12345678"]
    observaciones = ["Paciente estable"]

    resultado = gp.agregar_observacion(dnis, observaciones, "12345678", "Control pendiente")

    assert resultado == True
    assert observaciones[0] == "Paciente estable | Control pendiente"


def test_agregar_evolucion():
    dnis = ["12345678"]
    evoluciones = ["Sin evolucion"]

    resultado = gp.agregar_evolucion(dnis, evoluciones, "12345678", "Mejora clinica")

    assert resultado == True
    assert evoluciones[0] == "Mejora clinica"


def test_agregar_evolucion_acumulada():
    dnis = ["12345678"]
    evoluciones = ["Mejora clinica"]

    resultado = gp.agregar_evolucion(dnis, evoluciones, "12345678", "Continua estable")

    assert resultado == True
    assert evoluciones[0] == "Mejora clinica | Continua estable"

def test_contar_pacientes_por_estado_recursivo():
    estados = ["Internado", "Alta medica", "Internado", "Ambulatorio"]

    assert gp.contar_pacientes_por_estado_recursivo(estados, "Internado") == 2
    assert gp.contar_pacientes_por_estado_recursivo(estados, "Alta medica") == 1
    assert gp.contar_pacientes_por_estado_recursivo(estados, "Ambulatorio") == 1
    assert gp.contar_pacientes_por_estado_recursivo(estados, "Derivado") == 0