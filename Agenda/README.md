# Agenda en Python

Programa de consola para guardar personas (nombre y año de nacimiento) y consultar su edad. Es mi primer proyecto, hecho mientras aprendo Python desde cero.

## Funciones

- Menú interactivo: agregar persona, mostrar personas y salir.
- Los datos se guardan en un archivo `personas.json`, así que siguen ahí al cerrar y volver a abrir el programa.
- Los nombres se normalizan con `.title()` (por ejemplo, "keylor navas" se guarda como "Keylor Navas").
- Si `personas.json` está dañado, el programa avisa, hace una copia de seguridad con la fecha y la hora en el nombre y empieza con una lista vacía, para no perder los datos anteriores.
- Si no hay personas, muestra un mensaje en vez de una pantalla en blanco.
- Eliminar persona por posición, mostrando la lista antes para elegir.

## Cómo ejecutarlo

Necesitas Python 3 instalado. Desde la carpeta del proyecto:

```
cd Agenda
python Agenda.py
```

## Qué practiqué

Funciones y parámetros, listas y diccionarios, lectura y escritura de archivos JSON, manejo de errores con `try/except`, módulos propios (`utilidad_edad.py`) y control de versiones con Git.