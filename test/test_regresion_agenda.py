from src.agenda_v2 import agregar_contacto as agregar_contacto_v1, buscar_contacto as buscar_contacto_v1
from src.agenda import buscar_contacto, agregar_contacto,mostrar_contactos,eliminar_contacto

def test_regression_agenda():
    datos = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }  
                                                                                                                                    
    # Cargamos los contactos en la versión nueva
    for nombre, telefono in datos.items():
        agregar_contacto(nombre, telefono)
        agregar_contacto_v1(nombre,telefono)      
        
    # --- Regresión de búsqueda de contactos ---
    for nombre in datos:
        resultado_antiguo = buscar_contacto_v1(nombre)
        resultado_nuevo = buscar_contacto(nombre)
        assert resultado_antiguo == resultado_nuevo, (
            f"Regresión detectada: búsqueda de {nombre} cambió de "
            f"{resultado_antiguo} a {resultado_nuevo}"
        )
   
    # --- Regresión de mostrar los contactos ---
    contactos_antiguos = {"Ana Lopez": "0981111111", "Juan Perez": "0982222222", "Maria Vega": "0983333333"}

    # --- Listas de contactos antiguos ---
    print("\nLista de contactos antiguos:")
    for nombre, telefono in contactos_antiguos.items():
        print(f"{nombre} → {telefono}")
    
    contactos_nuevos = mostrar_contactos()

    # --- Lista de contactos nuevos ---
    print("\nLista de contactos nuevos:")
    for nombre, telefono in contactos_nuevos.items():
     print(f"{nombre} → {telefono}")

    assert contactos_antiguos == contactos_nuevos, (
        f"Regresión detectada: mostrar_contactos cambió de {contactos_antiguos} a {contactos_nuevos}"
    )


   # --- Regresión de eliminación de contactos ---
    eliminar_contacto("Maria Vega")
    assert buscar_contacto("Maria Vega") is None, "Regresión: eliminación no funciona igual que antes"
    print("\nLista de contactos actualizados:")
    for nombre, telefono in contactos_nuevos.items():
        print(f"{nombre} → {telefono}")






