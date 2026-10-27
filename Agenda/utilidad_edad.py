def calcular_edad(ano_nacimiento):
    ano_actual = 2026
    edad = ano_actual-ano_nacimiento
    return edad

def pedir_ano():
    
    while True:
        try:
            ano_nacimiento = int(input("Cual es tu año de nacimiento?\n"))
           
            
        except ValueError:
              print("Eso no es un número")
        else:
            if 1900 <= ano_nacimiento <= 2026:
                return ano_nacimiento

            print("Año inválido, debe estar entre 1900 y 2026")

    