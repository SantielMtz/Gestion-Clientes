import os
import json

# Esta es mi tabla hash para asociar nombres de clientes con sus archivos
clientes = {}

# Aquí va mi directorio donde se almacenarán los archivos de clientes
CLIENTES_DIR = "clientes"
os.makedirs(CLIENTES_DIR, exist_ok=True)

def cargar_clientes():
    """Carga los clientes desde los archivos almacenados."""
    global clientes
    clientes.clear()
    for archivo in os.listdir(CLIENTES_DIR):
        if archivo.endswith(".json"):
            nombre = archivo[:-5]  # Remover la extensión .json
            clientes[nombre] = os.path.join(CLIENTES_DIR, archivo)

def crear_cliente(nombre, servicio):
    """Crea un nuevo cliente con su archivo correspondiente."""
    if nombre in clientes:
        print(f"El cliente {nombre} ya existe.")
        return
    
    datos_cliente = {"nombre": nombre, "servicios": [servicio]}
    ruta_archivo = os.path.join(CLIENTES_DIR, f"{nombre}.json")
    with open(ruta_archivo, "w") as f:
        json.dump(datos_cliente, f, indent=4)
    
    clientes[nombre] = ruta_archivo
    print(f"Cliente {nombre} creado con éxito.")

def actualizar_cliente(nombre, servicio):
    """Agrega una nueva solicitud de servicio a un cliente existente."""
    if nombre not in clientes:
        print(f"El cliente {nombre} no existe.")
        return
    
    ruta_archivo = clientes[nombre]
    with open(ruta_archivo, "r+") as f:
        datos_cliente = json.load(f)
        datos_cliente["servicios"].append(servicio)
        f.seek(0)
        json.dump(datos_cliente, f, indent=4)
    
    print(f"Servicio agregado al cliente {nombre}.")

def consultar_cliente(nombre):
    """Muestra la información de un cliente."""
    if nombre not in clientes:
        print(f"El cliente {nombre} no existe.")
        return
    
    with open(clientes[nombre], "r") as f:
        datos_cliente = json.load(f)
        print(json.dumps(datos_cliente, indent=4))

def eliminar_cliente(nombre):
    """Elimina un cliente y su archivo."""
    if nombre not in clientes:
        print(f"El cliente {nombre} no existe.")
        return
    
    os.remove(clientes[nombre])
    del clientes[nombre]
    print(f"Cliente {nombre} eliminado con éxito.")

def listar_clientes():
    """Lista todos los clientes registrados."""
    if not clientes:
        print("No hay clientes registrados.")
    else:
        print("Clientes registrados:")
        for cliente in clientes:
            print(f"- {cliente}")

# Cargar clientes al iniciar el programa
cargar_clientes()

# Simulación de interacción
crear_cliente("Ana_Admin", "Servicio de consultoría")
crear_cliente("Carlos_Editor", "Optimización de procesos")
actualizar_cliente("Ana_Admin", "Soporte técnico")
consultar_cliente("Ana_Admin")
eliminar_cliente("Carlos_Editor")
listar_clientes()
