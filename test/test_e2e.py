from src.agenda import agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_contactos

def test_e2e_agenda():
    #Agregar varios contactos
    assert agregar_contacto("Ana Lopez", "0981111111") is True
    assert agregar_contacto("Juan Perez", "0982222222") is True
    assert agregar_contacto("Maria Vega", "0983333333") is True

    #Verificar que los contactos se agregaron correctamente
    assert buscar_contacto("Ana Lopez") == "0981111111"
    assert buscar_contacto("Juan Perez") == "0982222222"
    assert buscar_contacto("Maria Vega") == "0983333333"

    #Lista los contactos agregados
    contactos_actuales = mostrar_contactos()
    print("\n Contactos agregados:")
    for nombre, telefono in contactos_actuales.items():
        print(f"{nombre} → {telefono}")

    #Eliminar un contacto
    assert eliminar_contacto("Juan Perez") is True
    assert buscar_contacto("Juan Perez") is None

    #Mostrar contactos restantes
    contactos_actuales = mostrar_contactos()
    print("\n Contactos después de eliminar Juan Perez:")
    for nombre, telefono in contactos_actuales.items():
        print(f"{nombre} → {telefono}")

    #Validar integridad de la agenda
    assert len(contactos_actuales) == 2
    assert "Ana Lopez" in contactos_actuales
    assert "Maria Vega" in contactos_actuales