from src.agenda import  agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_contactos

def test_flujo_agregar_y_buscar_contacto():
    datos = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }

    # Agregar contactos
    for nombre, telefono in datos.items():
        agregar_contacto(nombre, telefono)


    # Imprimo la lista de contactos
    print("\nLista actual de contactos en integración:")
    for nombre, telefono in datos.items():
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
    for nombre, telefono in datos.items():
        print(f"{nombre} → {telefono}")

    # Los demás contactos siguen existiendo
    """ assert buscar_contacto("Ana Lopez") == "0981111111"
    assert buscar_contacto("Maria Vega") == "0983333333"  """


def test_mostrar_contactos_integra_todo():
    agregar_contacto("Carlos Ruiz", "0999999999")
    contactos = mostrar_contactos()

    # Verificar que el contacto esté en la lista
    assert "Carlos Ruiz" in contactos
    assert contactos["Carlos Ruiz"] == "0999999999"

    # También podemos imprimir la lista para visualizarla en consola
    print("\nLista actual de contactos en integración:")
    for nombre, telefono in contactos.items():
        print(f"{nombre} → {telefono}")

