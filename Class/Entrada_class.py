class Entrada:
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
                 prom_paso_auto,prom_paso_mionca,
                 ###############Isla####################
                 #Llegada
                 rnd_llegada_auto_isla, prox_llegada_auto_isla,rnd_llegada_mionca_isla, prox_llegada_mionca_isla, tipo_vehiculo_isla,flag_espera_auto_isla, flag_espera_mionca_isla,

                 # Colas isla
                 cola_autos_isla, cola_mionca_isla,
                 # Colas Max
                 cola_max_auto_isla, cola_max_mionca_isla,
                 # Flags Espera a mañana isla
                 flag_espera_man_auto_isla, flag_espera_man_mionca_isla,
                 cola_esp_man_auto_isla, cola_esp_man_mionca_isla, cola_esp_man_auto_acum_isla,
                 cola_esp_man_mionca_acum_isla, cola_esp_man_auto_prom_isla, cola_esp_man_mionca_prom_isla,
                 # Carga isla
                 flag_esta_cargando_isla,
                 rnd_carga_vehiculo_isla, tiempo_carga_isla, tiempo_final_isla, acum_paso_auto_isla, acum_paso_mionca_isla,
                 prom_paso_auto_isla, prom_paso_mionca_isla,
                 ):
        self.evento = evento
        self.dia = dia
        self.reloj = reloj
        #Llegada de vehículo Continente
        self.rnd_llegada_auto_cont = rnd_llegada_auto_cont
        self.prox_llegada_auto_cont = prox_llegada_auto_cont
        self.rnd_llegada_mionca_cont = rnd_llegada_mionca_cont
        self.prox_llegada_mionca_cont = prox_llegada_mionca_cont
        #self.tipo_vehiculo_cont= tipo_vehiculo_cont
        #self.flag_espera_auto_cont = flag_espera_auto_cont
        #self.flag_espera_mionca_cont = flag_espera_mionca_cont
        #Colas diarias cont
        self.cola_autos_cont = cola_autos_cont
        self.cola_mionca_cont = cola_mionca_cont
        #Max de colas cont
        self.cola_max_autos_cont = cola_max_auto_cont
        self.cola_max_mionca_cont = cola_max_mionca_cont
        #Colas de espera a mañana cont
        self.cola_esp_man_auto = cola_esp_man_auto
        self.cola_esp_man_mionca = cola_esp_man_mionca
        self.flag_espera_man_auto_cont = flag_espera_man_auto_cont
        self.flag_espera_man_mionca_cont = flag_espera_man_mionca_cont
        self.cola_esp_man_auto_acum = cola_esp_man_auto_acum
        self.cola_esp_man_mionca_acum = cola_esp_man_mionca_acum
        self.cola_esp_man_auto_prom = cola_esp_man_auto_prom
        self.cola_esp_man_mionca_prom = cola_esp_man_mionca_prom
        self.cola_esp_man_total = (cola_esp_man_auto_prom + cola_esp_man_mionca_prom)/2
        #Carga de vehículos cont
        self.flag_esta_cargando = flag_esta_cargando
        self.rnd_carga_vehiculo = rnd_carga_vehiculo
        self.tiempo_carga = tiempo_carga
        self.tiempo_final = tiempo_final
        #Transbordadores
        self.t1 = t1
        self.t2 = t2
        #Contadores de Continente a Isla
        self.acum_paso_auto = acum_paso_auto
        self.acum_paso_mionca = acum_paso_mionca
        self.prom_paso_auto =prom_paso_auto
        self.prom_paso_mionca = prom_paso_mionca
        #######################ISLA##########################
        #Llegada vehículos a la isla
        self.rnd_llegada_auto_isla = rnd_llegada_auto_isla
        self.prox_llegada_auto_isla = prox_llegada_auto_isla
        self.rnd_llegada_mionca_cont = rnd_llegada_mionca_isla
        self.prox_llegada_mionca_isla = prox_llegada_mionca_isla
        self.tipo_vehiculo_isla = tipo_vehiculo_isla
        self.flag_espera_auto_isla = flag_espera_auto_isla
        self.flag_espera_mionca_isla = flag_espera_mionca_isla
        # Colas diarias isla
        self.cola_autos_isla = cola_autos_isla
        self.cola_mionca_isla = cola_mionca_isla
        # Max de colas isla
        self.cola_max_autos_isla = cola_max_auto_isla
        self.cola_max_mionca_isla = cola_max_mionca_isla
        # Colas de espera a mañana isla
        self.cola_esp_man_auto_isla = cola_esp_man_auto_isla
        self.cola_esp_man_mionca_isla = cola_esp_man_mionca_isla
        self.flag_espera_man_auto_isla = flag_espera_man_auto_isla
        self.flag_espera_man_mionca_isla = flag_espera_man_mionca_isla
        self.cola_esp_man_auto_acum_isla = cola_esp_man_auto_acum_isla
        self.cola_esp_man_mionca_acum_isla = cola_esp_man_mionca_acum_isla
        self.cola_esp_man_auto_prom_isla = cola_esp_man_auto_prom_isla
        self.cola_esp_man_mionca_prom_isla = cola_esp_man_mionca_prom_isla
        self.cola_esp_man_total_isla = (cola_esp_man_auto_prom_isla + cola_esp_man_mionca_prom_isla) / 2
        # Carga de vehículos isla
        self.flag_esta_cargando_isla = flag_esta_cargando_isla
        self.rnd_carga_vehiculo_isla = rnd_carga_vehiculo_isla
        self.tiempo_carga_isla = tiempo_carga_isla
        self.tiempo_final_isla = tiempo_final_isla
        # Contadores de Isla a Continente
        self.acum_paso_auto_isla = acum_paso_auto_isla
        self.acum_paso_mionca_isla = acum_paso_mionca_isla
        self.prom_paso_auto_isla = prom_paso_auto_isla
        self.prom_paso_mionca_isla = prom_paso_mionca_isla



