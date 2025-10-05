from src.agenda import  agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_contactos

def test_integracion_agregar_y_buscar_contacto():
    datos = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }

    # Agregar contactos
    for nombre, telefono in datos.items():
        agregar_contacto(nombre, telefono)

    # Asignamos lista de datos 
    contactos = mostrar_contactos()

    # Imprimo la lista de contactos
    print("\nLista inicial de contactos en integración:")
    for nombre, telefono in contactos.items():
        print(f"{nombre} → {telefono}")

    # Verificar búsqueda
    for nombre, telefono in datos.items():
        assert buscar_contacto("Juan Perez") == "0982222222"

     # Eliminar un contacto
    resultado = eliminar_contacto("Juan Perez")
    assert resultado is True

    # Verificar que ya no exista
    assert buscar_contacto("Juan Perez") is None

    # Imprimo la lista de contactos
    print("\nLista actual de contactos en integración:")
    for nombre, telefono in contactos.items():
        print(f"{nombre} → {telefono}")
 