from utilidad_edad import calcular_edad,pedir_ano
import json
import shutil
from datetime import datetime



def cargar_personas():
    try:
        with open("personas.json", "r", encoding="utf-8") as archivo:
            personas = json.load(archivo)
            print("Archivo cargado")
            return personas
    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except json.JSONDecodeError:
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f'personas.{fecha}.bak'
        print("Archivo está dañado")
        shutil.copy('personas.json',nombre_archivo)
        print(f'Se realizó un backup de la base de datos anterior.{nombre_archivo}')
        return []

def agregar_persona(personas, nombre, ano):
    
    persona={"nombre":nombre.title(),"ano":ano}

    personas.append(persona)

def mostrar_personas(personas):
    if not personas:
        print("Agenda esta Vacía, no se encontraron personas")
        return

    for posicion,persona in enumerate(personas,1):
        print(f"{posicion}. Nombre: {persona['nombre']} - {calcular_edad(persona['ano']) } años")

    

def guardar_personas(personas):
    with open("personas.json", "w", encoding="utf-8") as archivo:
        json.dump(personas, archivo, ensure_ascii=False, indent=2)


def ingresar_persona(personas):
    nombre = input("Ingrese el nombre\n")
    ano = pedir_ano()
    agregar_persona(personas,nombre,ano)

personas = cargar_personas()
      
while True:
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Salir")
    opcion = input("Elige la opcion:") 

    if opcion in ("1", "a"):
        ingresar_persona(personas)
        guardar_personas(personas)
    elif opcion in ("2", "m"):
        mostrar_personas(personas)
    elif opcion in ("3", "s"):
        print("Ha salido del programa")
        break
    else:
        print("Opcion Invalida")

