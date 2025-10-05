import pytest
from src.agenda import validar_nombre, validar_telefono, agregar_contacto, buscar_contacto, contactos,eliminar_contacto

def test_validar_nombre_valido():
    assert validar_nombre("Juan Perez") is True

def test_validar_telefono_valido():
    assert validar_telefono("0987654321") is True

def test_agregar_contacto_valido():
    contactos.clear()
    assert agregar_contacto("Ana", "0987654321") is True
    assert contactos["Ana"] == "0987654321"

def test_agregar_contacto_nombre_invalido():
    with pytest.raises(ValueError, match="El nombre solo debe contener letras y espacios."):
        agregar_contacto("Ana123", "0987654321")

def test_agregar_contacto_telefono_invalido():
    with pytest.raises(ValueError, match="El número debe contener exactamente 10 dígitos."):
        agregar_contacto("Pedro", "12345")

def test_buscar_contacto_existente():
    contactos.clear()
    agregar_contacto("Luis", "0987654321")
    agregar_contacto("Julio", "0968133795")
    assert buscar_contacto("Luis") == "0987654321"

# test eliminacion
def test_eliminar_contacto():
    agregar_contacto("Ana Lopez","0987654321")
    agregar_contacto("Ana Calderon","0987654322")
    agregar_contacto("Ana Maldonado","0987654323")
   ##  print("\nLISTADO COMPLETO")
    #for nombre, telefono in contactos.items():
     #   print(f" {nombre}: {telefono}") 
    resultado=eliminar_contacto("Ana Lopez")

    """ print("\nLISTADO ELIMINADO")
    for nombre, telefono in contactos.items():
        print(f" {nombre}: {telefono}") """
    assert resultado is True
    assert buscar_contacto("Ana Lucia") is None