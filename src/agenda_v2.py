contactos = {}
#Agregar contactos a la agenda telefónica
def agregar_contacto(nombre, telefono):
    if not nombre or not telefono.isdigit() or len(telefono) != 10:
        return False
    contactos[nombre] = telefono
    return True
#Buscar contactos en la agenda telefónica
def buscar_contacto(nombre):
    return contactos.get(nombre)

#Mostrar contactos de la agenda telefónica
"""
def mostrar_contactos():
    return contactos
"""
#Eliminar contactos de la agenda telefónica
"""
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        return True
    return False
"""