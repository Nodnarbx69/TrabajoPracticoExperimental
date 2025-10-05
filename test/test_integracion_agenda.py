from src.agenda import  agregar_contacto, buscar_contacto

def test_flujo_agregar_y_buscar_contacto():
    datos = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }

    # Agregar contactos
    for nombre, telefono in datos.items():
        agregar_contacto(nombre, telefono)

    # Verificar búsqueda
    for nombre, telefono in datos.items():
        assert buscar_contacto("Juan Perez") == "0982222222"

    """ # Eliminar un contacto
    resultado = datos.eliminar_contacto("Juan Perez")
    assert resultado is True

    # Verificar que ya no exista
    assert datos.buscar_contacto("Juan Perez") is None

    # Los demás contactos siguen existiendo
    assert datos.buscar_contacto("Ana Lopez") == "0981111111"
    assert datos.buscar_contacto("Maria Vega") == "0983333333" """