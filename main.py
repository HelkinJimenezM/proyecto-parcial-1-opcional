# main.py

from mlfq import MLFQ
from utils import leer_archivo, escribir_salida

def main():
    # Lista de archivos de entrada
    archivos = ['mlq021.txt', 'mlq025.txt', 'mlq026.txt']  

    for archivo_entrada in archivos:
        print(f"Procesando archivo {archivo_entrada}...")

        # Leer el archivo y obtener los procesos
        procesos = leer_archivo(archivo_entrada)

        # Crear la instancia del algoritmo MLFQ
        mlfq = MLFQ()

        # Agregar los procesos a las colas del MLFQ
        for proceso in procesos:
            mlfq.agregar_proceso(proceso)

        # Ejecutar el algoritmo MLFQ
        resultados = mlfq.ejecutar()

        # Escribir los resultados en el archivo de salida
        archivo_salida = f"salida_{archivo_entrada}"
        escribir_salida(archivo_salida, resultados)

        print(f"Archivo de salida generado: {archivo_salida}")

if __name__ == "__main__":
    main()
