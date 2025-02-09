"""
    Escritura de archivos
"""

# Definir una función para guardar información en un archivo de texto
def guardar_informacion(cadena_final):
    """
    Función que guarda la información recibida en un archivo de texto.
    
    Parámetros:
    cadena_final (str): Cadena de texto que contiene la información 
                        que se almacenará en el archivo.
    """
    # El archivo se abrirá y cerrará automáticamente al salir del bloque with
    # Se usa el modo "w" para escritura, lo que sobrescribe el contenido del archivo si ya existe.
    with open("data/informacion-escritura-03.txt", "w") as archivo:
        # Se escribe la información en el archivo usando write()
        archivo.write(f"{cadena_final}")  # Se guarda la cadena en el archivo
    
    # Al salir del bloque 'with', el archivo se cierra automáticamente

# Definir una función para ingresar datos desde el usuario
def ingresar_informacion():
    """
    Función que permite ingresar información sobre parroquias,
    almacenando datos como el nombre, número de mujeres, número de hombres
    y total de población.
    
    Retorna:
    str: Una cadena con la información ingresada, separada por "|".
    """
    bandera = True  # Controla el bucle while para permitir múltiples ingresos de datos
    cadena_parroquias = ""  # Almacena la información ingresada en formato de cadena
    
    while bandera:
        # Solicitar el nombre de la parroquia
        nombre = input("Ingrese el nombre de la parroquia: ")

        # Capturar y convertir a entero la cantidad de mujeres
        poblacion_mujeres = input("Ingrese número de mujeres de la parroquia: ")
        poblacion_mujeres = int(poblacion_mujeres)

        # Capturar y convertir a entero la cantidad de hombres
        poblacion_hombres = input("Ingrese número de hombres de la parroquia: ")
        poblacion_hombres = int(poblacion_hombres)

        # Calcular el total de la población
        total_poblacion = poblacion_mujeres + poblacion_hombres
        
        # Formatear los datos ingresados y agregarlos a la cadena final
        # Cada línea contiene los datos separados por "|"
        cadena_parroquias = f"{cadena_parroquias}{nombre}|{poblacion_mujeres}|{poblacion_hombres}|{total_poblacion}\n"
        
        # Solicitar al usuario si desea continuar o finalizar el ingreso de datos
        valor = input("Ingrese el cero (0) para salir del ciclo: ")
        
        try:
            valor = int(valor)  # Convertir el valor ingresado a entero
            if valor == 0:  # Si el usuario ingresa 0, finaliza el bucle
                bandera = False
        except Exception as e:
            pass  # Se ignoran errores si el usuario ingresa un valor no numérico
    
    return cadena_parroquias  # Se retorna la cadena con la información ingresada


# Punto de entrada principal del script
if __name__ == "__main__":
    # Se solicita información al usuario
    mis_parroquias = ingresar_informacion()
    
    # Se guarda la información ingresada en un archivo de texto
    guardar_informacion(mis_parroquias)
    
    # Mensaje de finalización
    print("Fin")
