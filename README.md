# Simulador de Planificación MLFQ

Este proyecto implementa un simulador de planificación de procesos en sistemas operativos utilizando el algoritmo **MLFQ** (Multi-Level Feedback Queue). El simulador maneja procesos organizados en varias colas con diferentes niveles de prioridad y aplica políticas de planificación como **Round Robin (RR)** y **Shortest Job First (SJF)**.

## Archivos

- **proceso.py**: Define la clase `Proceso` que representa un proceso con su identificador, tiempo de ejecución (BT), tiempo de llegada (AT), cola, y prioridad.
- **mlfq.py**: Implementa el algoritmo MLFQ y gestiona las colas de procesos.
- **utils.py**: Contiene funciones para leer archivos de entrada y escribir archivos de salida.
- **main.py**: El archivo principal que coordina la ejecución del simulador.
- **simulador.py**: Contiene la lógica para ejecutar los algoritmos de planificación y generar los resultados.

## Archivos de Entrada

El simulador espera archivos de entrada con el siguiente formato:
