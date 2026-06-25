import validacion_arch as validacion


def test_validar_texto_no_vacio():
    assert validacion.validar_texto_no_vacio("Paciente estable") == True
    assert validacion.validar_texto_no_vacio("   ") == False
    assert validacion.validar_texto_no_vacio("") == False


def test_validar_texto_largo():
    assert validacion.validar_texto_largo("Control general", 3, 30) == True
    assert validacion.validar_texto_largo("Hi", 3, 30) == False
    assert validacion.validar_texto_largo("Texto demasiado largo para el rango indicado", 3, 10) == False


def test_solo_numeros():
    assert validacion.solo_numeros("123456") == True
    assert validacion.solo_numeros("123a56") == False
    assert validacion.solo_numeros("") == False
    assert validacion.solo_numeros("   ") == False


def test_validar_dni():
    assert validacion.validar_dni("12345678") == True
    assert validacion.validar_dni("1234567") == True
    assert validacion.validar_dni("123456") == False
    assert validacion.validar_dni("123456789") == False
    assert validacion.validar_dni("1234abcd") == False


def test_validar_nombre():
    assert validacion.validar_nombre("Juan Perez") == True
    assert validacion.validar_nombre("Maria Gomez") == True
    assert validacion.validar_nombre("A") == False
    assert validacion.validar_nombre("Juan123") == False
    assert validacion.validar_nombre("") == False


def test_validar_edad():
    assert validacion.validar_edad("0") == True
    assert validacion.validar_edad("30") == True
    assert validacion.validar_edad("120") == True
    assert validacion.validar_edad("121") == False
    assert validacion.validar_edad("-1") == False
    assert validacion.validar_edad("treinta") == False


def test_validar_diagnostico():
    assert validacion.validar_diagnostico("Control general") == True
    assert validacion.validar_diagnostico("Fiebre") == True
    assert validacion.validar_diagnostico("") == False
    assert validacion.validar_diagnostico("ab") == False


def test_validar_alergias():
    assert validacion.validar_alergias("Ninguna") == True
    assert validacion.validar_alergias("Penicilina") == True
    assert validacion.validar_alergias("") == False
    assert validacion.validar_alergias("a") == False


def test_validar_observacion():
    assert validacion.validar_observacion("Paciente estable") == True
    assert validacion.validar_observacion("ab") == False
    assert validacion.validar_observacion("") == False


def test_validar_evolucion():
    assert validacion.validar_evolucion("Evoluciona favorablemente") == True
    assert validacion.validar_evolucion("ab") == False
    assert validacion.validar_evolucion("") == False


def test_validar_opcion():
    assert validacion.validar_opcion("1", 0, 5) == True
    assert validacion.validar_opcion("0", 0, 5) == True
    assert validacion.validar_opcion("5", 0, 5) == True
    assert validacion.validar_opcion("6", 0, 5) == False
    assert validacion.validar_opcion("abc", 0, 5) == False


def test_validar_estado_paciente():
    assert validacion.validar_estado_paciente("Ambulatorio") == True
    assert validacion.validar_estado_paciente("Internado") == True
    assert validacion.validar_estado_paciente("Alta medica") == True
    assert validacion.validar_estado_paciente("Derivado") == False


def test_validar_numero_cama():
    assert validacion.validar_numero_cama("1") == True
    assert validacion.validar_numero_cama("10") == True
    assert validacion.validar_numero_cama("0") == False
    assert validacion.validar_numero_cama("-1") == False
    assert validacion.validar_numero_cama("cama") == False


def test_validar_estado_cama():
    assert validacion.validar_estado_cama("Libre") == True
    assert validacion.validar_estado_cama("Ocupada") == True
    assert validacion.validar_estado_cama("Mantenimiento") == True
    assert validacion.validar_estado_cama("Reservada") == False


def test_validar_sector():
    assert validacion.validar_sector("Guardia") == True
    assert validacion.validar_sector("Clinica medica") == True
    assert validacion.validar_sector("UTI") == True
    assert validacion.validar_sector("Pediatria") == True
    assert validacion.validar_sector("Traumatologia") == False
