contactos = {}

def agregar_contacto(nombre, telefono):
    if not nombre or not telefono.isdigit() or len(telefono) != 10:
        return False
    contactos[nombre] = telefono
    return True

def buscar_contacto(nombre):
    return contactos.get(nombre)

def mostrar_contactos():
    return contactos

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        return True
    return False