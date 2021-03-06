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
                 cola_esp_man_mionca_acum,cola_esp_man_auto_prom,cola_esp_man_mionca_prom,cola_esp_man_total,
                 #Carga cont

                 rnd_carga_vehiculo, tiempo_carga,tiempo_final,rnd_carga_auto, tiempo_carga_auto,tiempo_final_auto ,
                 ##Datos Trans

                t1_cola_autos, t1_cola_mionca,t1_hora_partida, t1_estado, t1_localizacion,
                t2_cola_autos, t2_cola_mionca, t2_hora_partida, t2_estado, t2_localizacion,

                 acum_paso_auto_ci, acum_paso_mionca_ci,
                 prom_paso_auto_ci,prom_paso_mionca_ci,
                 acum_paso_auto_ic, acum_paso_mionca_ic,
                 prom_paso_auto_ic, prom_paso_mionca_ic,
                 ###############Isla####################
                 #Llegada
                 rnd_llegada_auto_isla, prox_llegada_auto_isla,rnd_llegada_mionca_isla, prox_llegada_mionca_isla,

                 # Colas isla
                 cola_autos_isla, cola_mionca_isla,
                 # Colas Max
                 cola_max_auto_isla, cola_max_mionca_isla,
                 # Flags Espera a mañana isla

                 cola_esp_man_auto_isla, cola_esp_man_mionca_isla, cola_esp_man_auto_acum_isla,
                 cola_esp_man_mionca_acum_isla, cola_esp_man_auto_prom_isla, cola_esp_man_mionca_prom_isla,
                 # Carga isla
                 rnd_carga_vehiculo_isla, tiempo_carga_isla, tiempo_final_isla, rnd_carga_auto_isla, tiempo_carga_auto_isla, tiempo_final_auto_isla ,
                 acum_paso_auto_isla, acum_paso_mionca_isla,
                 prom_paso_auto_isla, prom_paso_mionca_isla,
                 #Estadisticas propias
                 acum_auto_cont, prom_auto_cont,
                 acum_camion_cont, prom_camion_cont,
                 acum_vehic_isla, prom_vehic_isla,
                 #Tiempos agregados al final
                 t_t1,t_t2,t_auto,t_mionca, t_auto_isla, t_mionca_isla,
                 rnd_purga, tiempo_purga, fin_purga,
                 hora_descarga_t1_lequeda, hora_fin_matenimiento_t1_lequeda, fin_cargan_vehic_cont_lequeda,fin_cargan_auto_cont_lequeda,
                fin_cargan_auto_islalequeda, fin_cargan_vehic_islalequeda,
                 hora_llegada_lequeda, hora_partida_lequeda
                ):


        self.hora_llegada_lequeda = hora_llegada_lequeda
        self.hora_partida_lequeda = hora_partida_lequeda
        self.fin_cargan_auto_cont_lequeda = fin_cargan_auto_cont_lequeda
        self.fin_cargan_vehic_cont_lequeda = fin_cargan_vehic_cont_lequeda
        self.hora_fin_matenimiento_t1_lequeda = hora_fin_matenimiento_t1_lequeda
        self.hora_descarga_t1_lequeda = hora_descarga_t1_lequeda
        self.fin_cargan_auto_islalequeda = fin_cargan_auto_islalequeda
        self.fin_cargan_vehic_islalequeda = fin_cargan_vehic_islalequeda
        self.rnd_purga = rnd_purga
        self.tiempo_purga = tiempo_purga
        self.fin_purga = fin_purga
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
        #self.flag_espera_man_auto_cont = flag_espera_man_auto_cont
        #self.flag_espera_man_mionca_cont = flag_espera_man_mionca_cont
        self.cola_esp_man_auto_acum = cola_esp_man_auto_acum
        self.cola_esp_man_mionca_acum = cola_esp_man_mionca_acum
        self.cola_esp_man_auto_prom = cola_esp_man_auto_prom
        self.cola_esp_man_mionca_prom = cola_esp_man_mionca_prom
        self.cola_esp_man_total = cola_esp_man_total
        #Carga de vehículos cont
        #self.flag_esta_cargando = flag_esta_cargando
        self.rnd_carga_vehiculo = rnd_carga_vehiculo
        self.tiempo_carga_vehic = tiempo_carga
        self.tiempo_final_vehic= tiempo_final
        self.rnd_carga_auto = rnd_carga_auto
        self.tiempo_carga_auto = tiempo_carga_auto
        self.tiempo_final_auto = tiempo_final_auto
        #Transbordadores
        self.t1_cola_autos = t1_cola_autos
        self.t1_cola_mionca = t1_cola_mionca
        self.t1_hora_partida = t1_hora_partida
        self.t1_estado = t1_estado
        self.t1_localizacion = t1_localizacion

        self.t2_cola_autos = t2_cola_autos
        self.t2_cola_mionca = t2_cola_mionca
        self.t2_hora_partida = t2_hora_partida
        self.t2_estado = t2_estado
        self.t2_localizacion = t2_localizacion
        #Contadores de Continente a Isla
        self.acum_paso_auto = acum_paso_auto_ci
        self.acum_paso_mionca = acum_paso_mionca_ci
        self.prom_paso_auto =prom_paso_auto_ci
        self.prom_paso_mionca = prom_paso_mionca_ci
        self.acum_paso_auto_ic = acum_paso_auto_ic
        self.acum_paso_mionca_ic = acum_paso_mionca_ic
        self.prom_paso_auto_ic = prom_paso_auto_ic
        self.prom_paso_mionca_ic = prom_paso_mionca_ic
        #######################ISLA##########################
        #Llegada vehículos a la isla
        self.rnd_llegada_auto_isla = rnd_llegada_auto_isla
        self.prox_llegada_auto_isla = prox_llegada_auto_isla
        self.rnd_llegada_mionca_isla = rnd_llegada_mionca_isla
        self.prox_llegada_mionca_isla = prox_llegada_mionca_isla
        #self.tipo_vehiculo_isla = tipo_vehiculo_isla
        #self.flag_espera_auto_isla = flag_espera_auto_isla
        #self.flag_espera_mionca_isla = flag_espera_mionca_isla
        # Colas diarias isla
        self.cola_autos_isla = cola_autos_isla
        self.cola_mionca_isla = cola_mionca_isla
        # Max de colas isla
        self.cola_max_autos_isla = cola_max_auto_isla
        self.cola_max_mionca_isla = cola_max_mionca_isla
        # Colas de espera a mañana isla
        self.cola_esp_man_auto_isla = cola_esp_man_auto_isla
        self.cola_esp_man_mionca_isla = cola_esp_man_mionca_isla
        #self.flag_espera_man_auto_isla = flag_espera_man_auto_isla
        #self.flag_espera_man_mionca_isla = flag_espera_man_mionca_isla
        self.cola_esp_man_auto_acum_isla = cola_esp_man_auto_acum_isla
        self.cola_esp_man_mionca_acum_isla = cola_esp_man_mionca_acum_isla
        self.cola_esp_man_auto_prom_isla = cola_esp_man_auto_prom_isla
        self.cola_esp_man_mionca_prom_isla = cola_esp_man_mionca_prom_isla
        self.cola_esp_man_total_isla = (cola_esp_man_auto_prom_isla + cola_esp_man_mionca_prom_isla) / 2
        # Carga de vehículos isla
        #self.flag_esta_cargando_isla = flag_esta_cargando_isla
        self.rnd_carga_vehiculo_isla = rnd_carga_vehiculo_isla
        self.tiempo_carga_isla = tiempo_carga_isla
        self.tiempo_final_isla = tiempo_final_isla
        self.tiempo_final_vehic_isla = tiempo_final_isla
        self.rnd_carga_auto_isla = rnd_carga_auto_isla
        self.tiempo_carga_auto_isla = tiempo_carga_auto_isla
        self.tiempo_final_auto_isla = tiempo_final_auto_isla
        # Contadores de Isla a Continente
        self.acum_paso_auto_isla = acum_paso_auto_isla
        self.acum_paso_mionca_isla = acum_paso_mionca_isla
        self.prom_paso_auto_isla = prom_paso_auto_isla
        self.prom_paso_mionca_isla = prom_paso_mionca_isla

        ###########Estadisticas propias
        self.acum_auto_cont = acum_auto_cont
        self.prom_auto_cont = prom_auto_cont
        self.acum_camion_cont = acum_camion_cont
        self.prom_camion_cont = prom_camion_cont
        self.acum_vehic_isla = acum_vehic_isla
        self.prom_vehic_isla =prom_vehic_isla

        ############# Tiempos del final
        self.t_t1 = t_t1
        self.t_t2 = t_t2
        self.t_auto = t_auto
        self.t_mionca = t_mionca
        self.t_auto_isla = t_auto_isla
        self.t_mionca_isla = t_mionca_isla


    def toString(self):
        return (self.dia, self.reloj,self.evento,self.t1.estado, self.t2.estado)

    def toStringIsla(self):
        return (self.cola_autos_isla,self.cola_mionca_isla)

    def getMax(self):
        arreglo = [self.fin_cargan_vehic_cont_lequeda,self.fin_cargan_auto_cont_lequeda, self.fin_cargan_auto_islalequeda,self.fin_cargan_vehic_islalequeda]
        i = 0
        while(i < len(arreglo)):
            if arreglo[i] != 0:
                return arreglo[i]
            i += 1
        return 0
