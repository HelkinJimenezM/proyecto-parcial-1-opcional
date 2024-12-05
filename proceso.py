class Proceso:
    def __init__(self, etiqueta, bt, at, q, pr):
        self.etiqueta = etiqueta
        self.bt = bt  # Burst Time
        self.at = at  # Arrival Time
        self.q = q    # Queue
        self.pr = pr  # Prioridad
        self.remaining_time = bt
        self.ct = 0   # Completion Time
        self.wt = 0   # Waiting Time
        self.rt = 0   # Response Time
        self.tat = 0  # Turn Around Time
        self.started = False

    def calcular_metricas(self, tiempo_actual):
        """Calcula las métricas una vez que el proceso ha terminado."""
        self.tat = self.ct - self.at
        self.wt = self.tat - self.bt
        if not self.started:
            self.rt = tiempo_actual - self.at
