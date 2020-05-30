class Entrada_prueba:
    def __init__(self, evento, dia, reloj,
                 #Llegada continente
                 rnd_llegada_auto_cont, prox_llegada_auto_cont,rnd_llegada_mionca_cont, prox_llegada_mionca_cont,
                 #Colas cont
                 cola_autos_cont, cola_mionca_cont,
                 #Colas Max
                 cola_max_auto_cont, cola_max_mionca_cont,
                 #Flags Espera a mañana cont
                 cola_esp_man_auto, cola_esp_man_mionca,cola_esp_man_auto_acum,
                 cola_esp_man_mionca_acum,cola_esp_man_auto_prom,cola_esp_man_mionca_prom,
                 #Carga cont

                 rnd_carga_vehiculo, tiempo_carga,tiempo_final, t1,t2, acum_paso_auto, acum_paso_mionca,
                 prom_paso_auto,prom_paso_mionca):
        self.evento = evento
        self.dia = dia
        self.reloj = reloj
        # Llegada de vehículo Continente
        self.rnd_llegada_auto_cont = rnd_llegada_auto_cont
        self.prox_llegada_auto_cont = prox_llegada_auto_cont
        self.rnd_llegada_mionca_cont = rnd_llegada_mionca_cont
        self.prox_llegada_mionca_cont = prox_llegada_mionca_cont
        # self.tipo_vehiculo_cont= tipo_vehiculo_cont
        # self.flag_espera_auto_cont = flag_espera_auto_cont
        # self.flag_espera_mionca_cont = flag_espera_mionca_cont
        # Colas diarias cont
        self.cola_autos_cont = cola_autos_cont
        self.cola_mionca_cont = cola_mionca_cont
        # Max de colas cont
        self.cola_max_autos_cont = cola_max_auto_cont
        self.cola_max_mionca_cont = cola_max_mionca_cont
        # Colas de espera a mañana cont
        self.cola_esp_man_auto = cola_esp_man_auto
        self.cola_esp_man_mionca = cola_esp_man_mionca

        self.cola_esp_man_auto_acum = cola_esp_man_auto_acum
        self.cola_esp_man_mionca_acum = cola_esp_man_mionca_acum
        self.cola_esp_man_auto_prom = cola_esp_man_auto_prom
        self.cola_esp_man_mionca_prom = cola_esp_man_mionca_prom
        self.cola_esp_man_total = (cola_esp_man_auto_prom + cola_esp_man_mionca_prom) / 2
        # Carga de vehículos cont

        self.rnd_carga_vehiculo = rnd_carga_vehiculo
        self.tiempo_carga = tiempo_carga
        self.tiempo_final = tiempo_final
        # Transbordadores
        self.t1 = t1
        self.t2 = t2
        # Contadores de Continente a Isla
        self.acum_paso_auto = acum_paso_auto
        self.acum_paso_mionca = acum_paso_mionca
        self.prom_paso_auto = prom_paso_auto
        self.prom_paso_mionca = prom_paso_mionca

    def toString(self):
        print(self.reloj,self.evento,self.cola_autos_cont, self.cola_mionca_cont)