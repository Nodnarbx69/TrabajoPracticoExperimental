from src.agenda import  agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_contactos

def test_integracion_agregar_y_buscar_contacto():
    # Creando una lista de datos para las pruebas
    datos = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }

    # Agregar contactos a la agenda telefonica, con su nombre y número telefónico
    for nombre, telefono in datos.items():
        agregar_contacto(nombre, telefono)

    # Asignamos lista de datos 
    contactos = mostrar_contactos()

    # Imprimo la lista de contactos, donde se visualiza el nombre y el teléfono
    print("\nLista inicial de contactos en integración:")
    for nombre, telefono in contactos.items():
        print(f"{nombre} → {telefono}")

    # Verificar búsqueda por el nombre 
    for nombre, telefono in datos.items():
        assert buscar_contacto("Ana Lopez") == "0981111111"

     # Eliminar un contacto de la agenda telefónica
    resultado = eliminar_contacto("Ana Lopez")
    assert resultado is True

    # Verificar que ya no exista el contacto eliminado
    assert buscar_contacto("Ana Lopez") is None

    # Imprimo la lista de contactos
    print("\nLista actual de contactos en integración:")
    for nombre, telefono in contactos.items():
        print(f"{nombre} → {telefono}")
 