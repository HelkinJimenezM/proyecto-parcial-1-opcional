from proceso import Proceso
from mlfq import MLFQ

class Simulador:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.procesos = []
        self.mlfq = MLFQ()

    def cargar_entrada(self):
        with open(self.archivo_entrada, "r") as file:
            for linea in file.readlines():
                if linea.startswith("#") or not linea.strip():
                    continue
                datos = linea.strip().split(";")
                etiqueta, bt, at, q, pr = datos[0], int(datos[1]), int(datos[2]), int(datos[3]), int(datos[4])
                self.procesos.append(Proceso(etiqueta, bt, at, q, pr))

    def configurar_mlfq(self):
        # Configuración según el esquema requerido
        self.mlfq.agregar_cola("RR", 1)
        self.mlfq.agregar_cola("RR", 3)
        self.mlfq.agregar_cola("SJF")

    def ejecutar_simulacion(self):
        tiempo_maximo = 100  # Tiempo arbitrario para simulación
        self.mlfq.ejecutar(self.procesos, tiempo_maximo)

    def generar_salida(self):
        with open(self.archivo_salida, "w") as file:
            for proceso in self.procesos:
                file.write(f"{proceso.etiqueta};{proceso.bt};{proceso.at};{proceso.q};{proceso.pr};"
                           f"{proceso.wt};{proceso.ct};{proceso.rt};{proceso.tat}\n")
            # Calcular promedios
            wt_promedio = sum(p.wt for p in self.procesos) / len(self.procesos)
            tat_promedio = sum(p.tat for p in self.procesos) / len(self.procesos)
            rt_promedio = sum(p.rt for p in self.procesos) / len(self.procesos)
            ct_promedio = sum(p.ct for p in self.procesos) / len(self.procesos)
            file.write(f"WT={wt_promedio}; TAT={tat_promedio}; RT={rt_promedio}; CT={ct_promedio}\n")
