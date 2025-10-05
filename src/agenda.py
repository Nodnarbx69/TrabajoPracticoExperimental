import re

# Diccionario global de contactos
contactos = {}

def validar_nombre(nombre):
    return bool(re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', nombre))

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

# Funcion para agregar contacto , nombre y telefono
def agregar_contacto(nombre, telefono):
    if not validar_nombre(nombre):
        raise ValueError("El nombre solo debe contener letras y espacios.")
    if not validar_telefono(telefono):
        raise ValueError("El número debe contener exactamente 10 dígitos.")
    contactos[nombre] = telefono
    return True

# Funcion buscar contacto por nombre
def buscar_contacto(nombre):
    return contactos.get(nombre, None)

# Funcion eliminar contacto por nombre
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        return True
    else:
        return False

def mostrar_contactos():
        return contactos

