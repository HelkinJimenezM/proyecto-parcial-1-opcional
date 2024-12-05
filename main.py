from simulador import Simulador

if __name__ == "__main__":
    # Archivos de entrada y salida
    archivo_entrada = "mlq021.txt"
    archivo_salida = "output_mlq021.txt"

    # Crear simulador y ejecutar
    simulador = Simulador(archivo_entrada, archivo_salida)
    simulador.cargar_entrada()
    simulador.configurar_mlfq()
    simulador.ejecutar_simulacion()
    simulador.generar_salida()
    print(f"Simulación completada. Salida generada en {archivo_salida}.")
