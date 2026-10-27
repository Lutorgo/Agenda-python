from datetime import datetime
print("keylor".title())
print("keylor navas".title())
print(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

def eliminar_persona(personas, posicion):
    if 1 <= posicion <= len(personas):
        return personas.pop(posicion - 1)
    return None

personas = [{"nombre":"Ana","ano":2000},{"nombre":"Luis","ano":1995},{"nombre":"Carlos","ano":2010}]

print(eliminar_persona(personas, 1))
print(eliminar_persona(personas, 3))
print(eliminar_persona(personas, 0))
print(eliminar_persona(personas, -1))
print(eliminar_persona(personas, 10))
print(personas)