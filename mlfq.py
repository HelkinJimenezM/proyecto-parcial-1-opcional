from cola import ColaRR, ColaSJF

class MLFQ:
    def __init__(self):
        self.colas = []

    def agregar_cola(self, politica, quantum=None):
        if politica == "RR":
            self.colas.append(ColaRR(quantum))
        elif politica == "SJF":
            self.colas.append(ColaSJF())
        else:
            raise ValueError("Política no soportada")

    def ejecutar(self, procesos, tiempo_maximo):
        tiempo_actual = 0
        cola_actual = 0

        while tiempo_actual < tiempo_maximo:
            for cola in self.colas:
                while not cola.procesos.empty():
                    proceso, ejecutado = cola.planificar(tiempo_actual)
                    if proceso:
                        if not proceso.started:
                            proceso.started = True
                            proceso.rt = tiempo_actual - proceso.at
                        tiempo_actual += ejecutado
                        if proceso.remaining_time == 0:
                            proceso.ct = tiempo_actual
                            proceso.calcular_metricas(tiempo_actual)
