from proceso import Proceso

def leer_archivo(archivo):
    """
    Lee el archivo de entrada y devuelve una lista de objetos Proceso.
    """
    procesos = []
    with open(archivo, 'r') as f:
        for linea in f:
            if not linea.startswith('#'):  # Ignorar líneas de comentario
                datos = linea.strip().split(';')
                if len(datos) == 5:
                    proceso = Proceso(*datos)  # Crear un objeto Proceso
                    procesos.append(proceso)
    return procesos

def escribir_salida(archivo, resultados):
    """
    Escribe los resultados de la simulación en el archivo de salida.
    """
    with open(archivo, 'w') as f:
        for resultado in resultados:
            f.write(resultado + '\n')
