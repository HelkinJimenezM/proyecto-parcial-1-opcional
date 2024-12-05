from queue import Queue
from abc import ABC, abstractmethod

class Planificador(ABC):
    @abstractmethod
    def planificar(self, procesos, tiempo_actual):
        pass

class ColaRR(Planificador):
    def __init__(self, quantum):
        self.quantum = quantum
        self.procesos = Queue()

    def agregar_proceso(self, proceso):
        self.procesos.put(proceso)

    def planificar(self, tiempo_actual):
        if not self.procesos.empty():
            proceso = self.procesos.get()
            ejecutado = min(proceso.remaining_time, self.quantum)
            proceso.remaining_time -= ejecutado
            if proceso.remaining_time > 0:
                self.procesos.put(proceso)  # Si no terminó, regresa a la cola
            return proceso, ejecutado
        return None, 0

class ColaSJF(Planificador):
    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)
        self.procesos.sort(key=lambda p: p.remaining_time)  # Ordenar por tiempo restante

    def planificar(self, tiempo_actual):
        if self.procesos:
            proceso = self.procesos.pop(0)  # Tomar el más corto
            ejecutado = proceso.remaining_time
            proceso.remaining_time = 0
            return proceso, ejecutado
        return None, 0
