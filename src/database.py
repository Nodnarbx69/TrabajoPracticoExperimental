contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono

def buscar_contacto(nombre):
    return contactos.get(nombre)