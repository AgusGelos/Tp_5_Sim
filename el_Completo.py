import math
import random

from Class.Entrada_class import Entrada
from Class.Trans_Class import Transbordador
from Class.Entrada_Cont_prueba import Entrada_prueba
import pandas as pd


def funcion_uniforme(rnd, lim_inf, lim_sup):
    return lim_inf + rnd * (lim_sup - lim_inf)


def generar_miles(cantidad_dias, lim_inf, lim_sup):
    tabla_dia = []
    tabla_completa = []
    entry_aux = 0
    cola_esp_man_auto_acum = 0
    cola_esp_man_mionca_acum = 0
    cola_esp_man_total = 0

    ############################### Purga #############################################

    hora_descarga_t1_lequeda = 0
    hora_fin_matenimiento_t1_lequeda = 0
    fin_cargan_vehic_cont_lequeda = 0
    fin_cargan_auto_cont_lequeda = 0
    fin_cargan_auto_islalequeda = 0
    fin_cargan_vehic_islalequeda = 0


    tiempo_purga = 999
    pausa_por_purga = (20/60)
    bandera_purga = False
    verdadera_hora = 999

    fin_de_purga = 999
    t1_anterior_Estado = ""
    rnd_purga = random.random()

    if (rnd_purga < 0.5):
        tiempo_purga = 7 + (21.1)
        bandera_purga = True
    else:
        if (rnd_purga < 0.8):
            tiempo_purga = 7 + (18.7)
            bandera_purga = True
        else:
            tiempo_purga = 7 + (16.3)
            bandera_purga = True


    cola_esp_man_auto_acum_isla = 0
    cola_esp_man_mionca_acum_isla = 0

    t1 = Transbordador(0, 0, 10, 9, "Libre", "Continente", 4, 99, "Continente")
    t2 = Transbordador(0, 0, 20, 10, "Libre", "Continente", 9, 99, "Continente")
    autos_totales_cont = 0
    camiones_totales_cont = 0
    vehic_totales_isla = 0
    dia = 0
    cola_max_auto, cola_max_mionca, cola_max_mionca_isla, cola_max_auto_isla = 0, 0, 0, 0
    acum_paso_a_ci, acum_paso_c_ci, acum_paso_a_ic, acum_paso_c_ic = 0, 0, 0, 0
    for i in range(cantidad_dias):
        ############# Parámetros de entrada

        tabla_dia = []
        reloj = 7
        evento = "Inicio del Día"
        rnd_llegada_mionca_cont = random.uniform(0, 1)
        t_mionca = funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)
        prox_llegada_mionca_cont = reloj + t_mionca
        rnd_llegada_auto_cont = random.uniform(0, 1)
        t_auto = funcion_uniforme(rnd_llegada_auto_cont, 0.16, 0.33)
        prox_llegada_auto_cont = 7.5 + t_auto
        trans_en_uso = "T1"
        hora_descarga_t1, hora_descarga_t2 = 9999, 9999
        dia += 1
        siguen_llegando_autos = True
        siguen_llegando_mionca = True
        fin_cargan_vehic_cont = 999
        primero = False
        fin_cargan_auto_cont = 999
        hora_fin_matenimiento_t1 = 999
        hora_fin_matenimiento_t2 = 999
        fin_del_dia = 20


        ################################### PARAMETROS DE ISLA ###########################
        siguen_llegando_autos_isla = True
        siguen_llegando_mionca_isla = True
        rnd_llegada_auto_isla = random.uniform(0, 1)
        prox_llegada_auto_isla = 10 + funcion_uniforme(rnd_llegada_auto_isla, 0.1167, 0.2833)
        rnd_llegada_mionca_isla = random.uniform(0, 1)
        prox_llegada_mionca_isla = 10 + funcion_uniforme(rnd_llegada_mionca_isla, 0.5, 1.5)
        fin_cargan_vehic_isla = 999
        fin_cargan_auto_isla = 999
        trans_en_uso_isla = "T3"



        ####################### CHEKAR estados de Trans a valores iniciales o mantenimiento ######################################
        if i == t1.mantenimiento:
            t1.estado = "Mantenimiento"
            trans_en_uso = "T2"
            t1.mantenimiento += 10
            t1.hora_partida = 999
            t1.hora_llegada = 999
            t2.hora_partida = 9
            hora_fin_matenimiento_t1 = 13
        elif i == t2.mantenimiento:
            t2.estado = "Mantenimiento"
            t2.mantenimiento += 10
            trans_en_uso = "T1"
            t1.hora_partida = 9
            hora_fin_matenimiento_t2 = 13
            t2.hora_partida = 999
            t2.hora_llegada = 999

        else:
            t1.estado = "Libre"
            t1.localizacion = "Continente"
            t1.hora_partida = 9
            t2.estado = "Libre"
            t2.localizacion = "Continente"
            t2.hora_partida = 10

        ############################## Establecer el valor de las colas ACUMULADAS ##############################################
        if i == 0:
            cola_autos = 0
            cola_mionca = 0
            acum_auto = 0
            acum_mionca = 0
            cola_autos_isla = 0
            cola_mionca_isla = 0
            acum_auto_isla = 0
            acum_mionca_isla = 0
        else:
            acum_auto = entry_aux.acum_paso_auto
            acum_mionca = entry_aux.acum_paso_mionca
            acum_auto_isla = entry_aux.acum_paso_auto_isla
            acum_mionca_isla = entry_aux.acum_paso_mionca_isla

        corta = False

        bandera_fin = True
        #########################################################   CICLO     ###################################################
        while bandera_fin:
            bandera_fin = True
            rnd_purga = 0
            cola_esp_man_auto = 0
            cola_esp_man_mionca = 0


            t_t1,t_t2, t_auto,t_mionca,t_auto_isla,t_mionca_isla = 0,0,0,0,0,0
            t_fin_cargan_auto_isla, t_fin_cargan_vehic_cont, t_fin_cargan_vehic_isla, t_fin_cargan_auto_cont = 0, 0, 0, 0
            rnd_llegada_auto_cont = 0
            rnd_llegada_mionca_cont = 0
            rnd_carga_mionca_cont, rnd_carga_auto_cont, rnd_carga_auto_isla, rnd_carga_mionca_isla = 0, 0, 0, 0
            ############################################## param ISLA ##################################+
            cola_esp_man_auto_isla = 0
            cola_esp_man_mionca_isla = 0
            t_fin_cargan_vehic_isla = 0
            rnd_llegada_auto_isla = 0
            rnd_llegada_mionca_isla = 0

            ############################################## COLA DE AYER ##########################################

            if (len(tabla_completa) != 0) and reloj == 7:
                cola_autos = aux[-1].cola_esp_man_auto - aux[-1].t1_cola_autos - aux[-1].t2_cola_autos
                cola_mionca = aux[-1].cola_esp_man_mionca - aux[-1].t1_cola_mionca - aux[-1].t2_cola_mionca
                cola_autos_isla = aux[-1].cola_esp_man_auto_isla
                cola_mionca_isla = aux[-1].cola_esp_man_mionca_isla
                cola_max_auto = aux[-1].cola_max_autos_cont
                cola_max_mionca = aux[-1].cola_max_mionca_cont
                cola_max_auto_isla= aux[-1].cola_max_autos_isla
                cola_max_mionca_isla = aux[-1].cola_max_mionca_isla
                ##Prox Carga de vehículo:

                if cola_mionca > 0 and hora_fin_matenimiento_t1 == 999:
                    evento = "Inicio día/Carga Camión"
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca += 1
                    cola_mionca -= 1
                    rnd_carga_mionca_cont = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)

                    fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                elif cola_autos > 0 and hora_fin_matenimiento_t1 == 999:
                    evento = "Inicio día/Carga Auto"
                    t1.estado = "Cargando"
                    t1.capacidad -= 1
                    t1.cola_autos += 1
                    cola_autos -= 1
                    rnd_carga_auto_cont = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                    fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                else:
                    if t1.estado == "Mantenimiento":
                        if cola_mionca > 0:
                            evento = "Inicio día/Carga Camión"
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif cola_autos > 0:
                            evento = "Inicio día/Carga Auto"
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont

            if primero:
                ########################################## OPCIÓN DE MINIMO ########################################################

                opcion = min(prox_llegada_auto_cont, prox_llegada_mionca_cont, fin_cargan_vehic_cont,
                             fin_cargan_auto_cont,
                             t1.hora_partida, t2.hora_partida, t1.hora_llegada, t2.hora_llegada,
                             hora_descarga_t1, hora_descarga_t2,
                             hora_fin_matenimiento_t1, hora_fin_matenimiento_t2, fin_del_dia,
                             ################ Isleños ################
                             prox_llegada_auto_isla, prox_llegada_mionca_isla, fin_cargan_auto_isla,
                             fin_cargan_vehic_isla,tiempo_purga, fin_de_purga
                             )

                ########################################## Curso normal ##################################################




                #################################################### FIN MANTENIMIENTO T1 #########################################
                if opcion == tiempo_purga and tiempo_purga < 23:
                    evento = "Purga de T1"
                    t1_anterior_Estado = t1.estado
                    t1.estado = "Purga"
                    reloj = tiempo_purga
                    fin_de_purga = reloj + round(20/60,4)
                    tiempo_purga = 999

                    t1.hora_llegada_lequeda = (t1.hora_llegada - reloj)
                    t1.hora_llegada = 999
                    t1.hora_partida_lequeda = (t1.hora_partida - reloj)
                    t1.hora_partida = 999
                    hora_descarga_t1_lequeda = hora_descarga_t1 - reloj
                    hora_descarga_t1 = 999
                    hora_fin_matenimiento_t1_lequeda = hora_fin_matenimiento_t1 - reloj
                    if(trans_en_uso == "T1"):
                        if(fin_cargan_vehic_cont != 999):
                            fin_cargan_vehic_cont_lequeda = fin_cargan_vehic_cont - reloj
                            fin_cargan_vehic_cont=999
                        else:
                            fin_cargan_auto_cont_lequeda = fin_cargan_auto_cont - reloj
                            fin_cargan_auto_cont = 999
                    if(trans_en_uso_isla == "T1"):
                        if(fin_cargan_auto_isla != 999):
                            fin_cargan_auto_islalequeda = fin_cargan_auto_isla - reloj
                            fin_cargan_auto_isla=999
                        else:
                            fin_cargan_vehic_islalequeda = fin_cargan_vehic_isla - reloj
                            fin_cargan_vehic_isla = 999
                elif opcion == tiempo_purga and reloj > 22:
                    tiempo_purga = 7.1

                elif opcion == fin_de_purga:
                    evento = "Fin de Purga"
                    if(t1_anterior_Estado != "Purga"):
                        t1.estado = t1_anterior_Estado
                    else:
                        t1.estado = "Libre"
                    reloj = fin_de_purga
                    rnd_purga = random.random()
                    fin_de_purga = 999
                    if (rnd_purga < 0.5):
                        tiempo_purga = reloj + (5.1)
                    else:
                        if (rnd_purga < 0.8):
                            tiempo_purga = reloj + (3.7)
                        else:
                            tiempo_purga = reloj + (1.3)

                    t1.hora_llegada = reloj + t1.hora_llegada_lequeda
                    t1.hora_partida = reloj + t1.hora_partida_lequeda
                    hora_descarga_t1 = reloj + hora_descarga_t1_lequeda
                    hora_fin_matenimiento_t1 = reloj + hora_fin_matenimiento_t1_lequeda

                    if (trans_en_uso == "T1"):
                        if (fin_cargan_vehic_cont != 999):
                            fin_cargan_vehic_cont = reloj + fin_cargan_vehic_cont_lequeda
                        else:
                            fin_cargan_auto_cont = reloj + fin_cargan_auto_cont_lequeda
                    if (trans_en_uso_isla == "T1"):
                        if (fin_cargan_auto_isla != 999):
                            fin_cargan_auto_isla = reloj + fin_cargan_auto_islalequeda
                        else:
                            fin_cargan_vehic_isla = reloj + fin_cargan_vehic_islalequeda


                    hora_descarga_t1_lequeda = 0
                    hora_fin_matenimiento_t1_lequeda = 0
                    fin_cargan_vehic_cont_lequeda = 0
                    fin_cargan_auto_cont_lequeda = 0
                    fin_cargan_auto_islalequeda = 0
                    fin_cargan_vehic_islalequeda = 0
                    t1.hora_partida_lequeda = 0


                elif opcion == hora_fin_matenimiento_t1 and t1.estado != "Purga":
                    evento = "Fin Mantenimiento T1"
                    t1.estado = "Libre"
                    reloj = hora_fin_matenimiento_t1
                    t1.hora_partida = reloj + 1
                    hora_fin_matenimiento_t1 = 999
                    if t2.localizacion != "Continente":
                        trans_en_uso = "T1"
                        if cola_mionca > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)

                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif cola_autos > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont


                #################################################### FIN MANTENIMIENTO T2 #########################################
                elif opcion == hora_fin_matenimiento_t2:
                    evento = "Fin Mantenimiento T2"
                    t2.estado = "Libre"
                    reloj = hora_fin_matenimiento_t2
                    t2.hora_partida = reloj + 1
                    hora_fin_matenimiento_t2 = 999
                    if t1.localizacion != "Continente":
                        trans_en_uso = "T2"
                        if cola_mionca > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif cola_autos > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont

                #################################################### FIN DE CARGA MIONCA CONT #################################
                elif opcion == fin_cargan_vehic_cont:
                    reloj = fin_cargan_vehic_cont
                    fin_cargan_vehic_cont = 999
                    evento = "Fin Carga de Camión Cont"
                    if trans_en_uso == "T1" and t1.estado != "Purga":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif t1.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t1.capacidad == 0:
                            t1.hora_partida = reloj + 0.01



                    elif trans_en_uso == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad == 0:
                            t2.hora_partida = reloj + 0.01

                elif opcion == fin_cargan_vehic_cont:
                    reloj = fin_cargan_vehic_cont
                    fin_cargan_vehic_cont = 999
                    evento = "Fin Carga de Camión Cont"
                    if trans_en_uso == "T1" and t1.estado != "Purga":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif t1.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t1.capacidad == 0:
                            t1.hora_partida = reloj + 0.01



                    elif trans_en_uso == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad == 0:
                            t2.hora_partida = reloj + 0.01


                #################################################### FIN DE CARGA AUTO CONT #################################
                elif opcion == fin_cargan_auto_cont:
                    reloj = fin_cargan_auto_cont
                    fin_cargan_auto_cont = 999

                    evento = "Fin Carga de Auto Cont"
                    if trans_en_uso == "T1" and t1.estado != "Purga":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif t1.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t1.capacidad == 0:
                            t1.hora_partida = reloj + 0.01

                    elif trans_en_uso == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un camión
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
                        elif t2.capacidad == 0:
                            t2.hora_partida = reloj + 0.01

                ########################## LLEGADA DE AUTO AL CONTINENTE ##############################
                elif opcion == prox_llegada_auto_cont:
                    ## Llega un auto
                    evento = "Llegada de Auto a Continente"
                    autos_totales_cont += 1
                    reloj = prox_llegada_auto_cont
                    cola_autos += 1
                    pasa = False
                    if reloj <= 12 and siguen_llegando_autos:
                        rnd_llegada_auto_cont = random.uniform(0, 1)
                        t_auto = funcion_uniforme(rnd_llegada_auto_cont, 0.167, 0.33)
                        prox_llegada_auto_cont = reloj + t_auto
                    elif reloj <= 19 and siguen_llegando_autos:
                        rnd_llegada_auto_cont = random.uniform(0, 1)
                        t_auto = funcion_uniforme(rnd_llegada_auto_cont, 0.417, 0.583)
                        prox_llegada_auto_cont = reloj + t_auto
                    else:
                        siguen_llegando_autos = False
                        prox_llegada_auto_cont = 999
                    ##

                    if (trans_en_uso == "T1") and t1.estado == "Libre" and t1.capacidad >= 1 and t1.estado != "Purga":
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                        cola_autos -= 1
                        pasa = True
                    elif trans_en_uso == "T2" and t2.estado == "Libre" and t2.capacidad >= 1:
                        t2.estado = "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        cola_autos -= 1
                        pasa = True

                    elif trans_en_uso == "T1" and t1.capacidad == 0 and t1.estado != "Purga":
                        t1.hora_partida = reloj + 0.01
                    elif trans_en_uso == "T2" and t2.capacidad == 0:
                        t2.hora_partida = reloj + 0.01

                    if pasa:
                        rnd_carga_auto_cont = random.uniform(0, 1)
                        t_fin_cargan_auto_cont = + funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                        fin_cargan_auto_cont = reloj + t_fin_cargan_auto_cont


                    if (cola_max_auto) <= cola_autos:
                        cola_max_auto = cola_autos




                ################################### LLEGADA DE CAMION ####################################

                elif opcion == prox_llegada_mionca_cont:
                    evento = "Llegada de Camión/Ómnibus a Continente"
                    reloj = prox_llegada_mionca_cont
                    camiones_totales_cont += 1
                    cola_mionca += 1
                    pasa = False
                    if reloj <= 11 and siguen_llegando_mionca:
                        rnd_llegada_mionca_cont = random.uniform(0, 1)
                        t_mionca = funcion_uniforme(rnd_llegada_mionca_cont, 0.314, 0.346)
                        prox_llegada_mionca_cont = reloj + t_mionca
                    elif reloj <= 19.5 and siguen_llegando_mionca:
                        rnd_llegada_mionca_cont = random.uniform(0, 1)
                        t_mionca = funcion_uniforme(rnd_llegada_mionca_cont, 1.917, 2.083)
                        prox_llegada_mionca_cont = reloj + t_mionca
                    else:
                        siguen_llegando_mionca = False
                        prox_llegada_mionca_cont = 999

                    if (trans_en_uso == "T1") and t1.capacidad >= 2 and t1.estado == "Libre" and t1.estado != "Purga":
                        t1.estado = "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        pasa = True
                        cola_mionca -= 1
                    elif (trans_en_uso == "T2") and t2.capacidad >= 2 and t2.estado == "Libre":
                        t2.estado = "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        pasa = True
                        cola_mionca -= 1

                    elif trans_en_uso == "T1" and t1.capacidad == 0 and t1.estado != "Purga":
                        t1.hora_partida = reloj + 0.01
                    elif trans_en_uso == "T2" and t2.capacidad == 0:
                        t2.hora_partida = reloj + 0.01

                    if pasa:
                        rnd_carga_mionca_cont = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)

                    if cola_max_mionca <= cola_mionca:
                        cola_max_mionca = cola_mionca

                ############################### PARTE EL FERRY CHU CHUUU######################pame la pija#############
                elif opcion == t1.hora_partida and t1.estado != "Purga":
                    # Revisar desde donde sale y liberar el T
                    if reloj >= 20 and t1.localizacion == "Continente":
                        t1.hora_partida = 999
                    else:

                        if t1.estado == "Cargando":
                            if t1.localizacion == "Continente":
                                evento = "Esperando Para partir"
                                if fin_cargan_auto_cont == 999:
                                    t1.hora_partida = fin_cargan_vehic_cont + 0.01
                                else:
                                    t1.hora_partida = fin_cargan_auto_cont + 0.01
                            else:  # isla
                                if fin_cargan_auto_isla == 999:
                                    t1.hora_partida = fin_cargan_vehic_isla + 0.01
                                else:
                                    t1.hora_partida = fin_cargan_auto_isla + 0.01
                        else:
                            # Reviso que sea del continente o la isla
                            reloj = t1.hora_partida
                            t1.hora_partida = 999
                            if t1.localizacion == "Continente":

                                evento = "Salida T1 Cont-Isla"
                                if t2.localizacion == "Continente" and t2.estado != "Mantenimiento":
                                    trans_en_uso = "T2"
                                else:
                                    trans_en_uso = "T3"

                                t_t1 = random.uniform(0.917, 1.084)
                                t1.hora_llegada = reloj + t_t1
                                t1.puerto_salida = t1.localizacion
                                t1.localizacion = "Mar"
                                t1.hora_partida = t1.hora_llegada + 1

                            else:
                                evento = "Salida T1 Isla-Cont"

                                if t2.localizacion == "Isla":
                                    trans_en_uso_isla = "T2"
                                else:
                                    trans_en_uso_isla = "T3"
                                t_t1 = random.uniform(0.917, 1.084)
                                t1.hora_llegada = reloj + t_t1
                                t1.puerto_salida = t1.localizacion
                                t1.localizacion = "Mar"

                ################################# SALE EL SEGUNDO FERRY #######################################
                elif opcion == t2.hora_partida:

                    if t2.hora_partida >= 20 and t2.localizacion == "Continente":
                        t2.hora_partida = 999
                    else:
                        if t2.estado == "Cargando":
                            evento = "Esperando para Partir"
                            if t2.localizacion == "Continente":
                                if fin_cargan_auto_cont == 999:
                                    t2.hora_partida = fin_cargan_vehic_cont + 0.01
                                else:
                                    t2.hora_partida = fin_cargan_auto_cont + 0.01
                            else:  # isla
                                if fin_cargan_auto_isla == 999:
                                    t2.hora_partida = fin_cargan_vehic_isla + 0.01
                                else:
                                    t2.hora_partida = fin_cargan_auto_isla + 0.01
                        else:
                            reloj = t2.hora_partida
                            t2.hora_partida = 999
                            if t2.localizacion == "Continente":
                                evento = "Salida T2 Cont-Isla"

                                if t1.localizacion == "Continente" and t1.estado != "Mantenimiento":
                                    trans_en_uso = "T1"
                                else:
                                    trans_en_uso = "T3"
                                t_t2 = random.uniform(0.917, 1.084)
                                t2.hora_llegada = reloj + t_t2
                                t2.puerto_salida = t2.localizacion
                                t2.localizacion = "Mar"
                                t2.hora_partida = t2.hora_llegada + 1

                            else:
                                evento = "Salida T2 Isla-Cont"

                                if t1.localizacion == "Isla":
                                    trans_en_uso_isla = "T1"
                                else:
                                    trans_en_uso_isla = "T3"

                                t_t2 = random.uniform(0.917, 1.084)
                                t2.hora_llegada = reloj + t_t2
                                t2.puerto_salida = t2.localizacion
                                t2.localizacion = "Mar"
                                t2.hora_partida = t2.hora_llegada + 1

                #################################Llegada de ferry 1 al continente###################################
                elif opcion == t1.hora_llegada and t1.estado != "Purga":
                    acum_auto += t1.cola_autos
                    acum_mionca += t1.cola_mionca
                    reloj = t1.hora_llegada
                    hora_descarga_t1 = reloj

                    if t1.puerto_salida == "Isla":
                        acum_paso_a_ci += t1.cola_autos
                        acum_paso_c_ci += t1.cola_mionca
                        evento = "Llegada T1 a Continente"
                        t1.estado = "Descargando"
                        t1.localizacion = "Continente"
                        for i in range(t1.cola_autos):
                            hora_descarga_t1 += random.uniform(0.0077, 0.024)
                        for i in range(t1.cola_mionca):
                            hora_descarga_t1 += random.uniform(0.024, 0.041)

                        if t2.localizacion != "Continente" or t2.estado == "Mantenimiento":
                            trans_en_uso = "T1"
                    else:
                        acum_paso_a_ic += t1.cola_autos
                        acum_paso_c_ic += t1.cola_mionca
                        evento = "Llegada T1 a Isla"
                        t1.estado = "Descargando"
                        t1.localizacion = "Isla"
                        for i in range(t1.cola_autos):
                            hora_descarga_t1 += random.uniform(0.0077, 0.024)
                        for i in range(t1.cola_mionca):
                            hora_descarga_t1 += random.uniform(0.024, 0.041)
                        if t2.localizacion != "Isla":
                            trans_en_uso_isla = "T1"
                    t1.hora_llegada = 999

                #############Llegada de ferry 2 al continente###########
                elif opcion == t2.hora_llegada:
                    acum_auto += t2.cola_autos
                    acum_mionca += t2.cola_mionca
                    reloj = t2.hora_llegada
                    hora_descarga_t2 = reloj
                    if t2.puerto_salida == "Isla":
                        acum_paso_a_ci += t2.cola_autos
                        acum_paso_c_ci += t2.cola_mionca
                        evento = "Llegada de T2 al continente"
                        t2.estado = "Descargando"
                        t2.localizacion = "Continente"
                        for i in range(t2.cola_autos):
                            hora_descarga_t2 += random.uniform(0.0077, 0.024)
                        for i in range(t2.cola_mionca):
                            hora_descarga_t2 += random.uniform(0.024, 0.041)

                        if t1.localizacion != "Continente" or t1.estado == "Mantenimiento":
                            trans_en_uso = "T2"
                    ##################################### Llegada del Ferry 2 a la ISLA #################################
                    else:
                        acum_paso_a_ic += t2.cola_autos
                        acum_paso_c_ic += t2.cola_mionca
                        evento = "Llegada T2 a Isla"
                        t2.estado = "Descargando"
                        t2.localizacion = "Isla"
                        for i in range(t2.cola_autos):
                            hora_descarga_t2 += random.uniform(0.0077, 0.024)
                        for i in range(t2.cola_mionca):
                            hora_descarga_t2 += random.uniform(0.024, 0.041)
                        if t1.localizacion != "Isla":
                            trans_en_uso_isla = "T2"
                    t2.hora_llegada = 999

                #################Fin Descarga T1 ###########################
                elif opcion == hora_descarga_t1 and t1.estado != "Purga":
                    if t1.localizacion == "Continente":
                        evento = "Fin de descarga T1 Continente"
                    else:
                        evento = "Fin de descarga T1 Isla"
                    t1.estado = "Libre"
                    reloj = hora_descarga_t1
                    hora_descarga_t1 = 999
                    t1.cola_autos = 0
                    t1.cola_mionca = 0
                    t1.capacidad = 10
                    t1.hora_partida = reloj + 1
                    if t1.localizacion == "Continente" and trans_en_uso == "T1" and reloj <= 20:
                        if cola_mionca > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif cola_autos > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont
                        else:
                            t1.estado = "Libre"
                            fin_cargan_vehic_cont = 999

                    elif t1.localizacion == "Isla" and trans_en_uso_isla == "T1":
                        if cola_mionca_isla > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla

                        elif cola_autos_isla > 0:
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla
                        else:
                            t1.estado = "Libre"
                            fin_cargan_vehic_isla = 999

                ######################## FIN Descarga T2 ######################################
                elif opcion == hora_descarga_t2:
                    if t2.localizacion == "Continente":
                        evento = "Fin de descarga T2 Contiente"
                    else:
                        evento = "Fin de descarga T2 Isla"
                    t2.estado = "Libre"
                    reloj = hora_descarga_t2
                    hora_descarga_t2 = 999
                    t2.cola_autos = 0
                    t2.cola_mionca = 0
                    t2.capacidad = 20
                    t2.hora_partida = reloj + 1

                    if t2.localizacion == "Continente" and trans_en_uso == "T2" and reloj <= 20:
                        if cola_mionca > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca -= 1
                            rnd_carga_mionca_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.017, 0.049)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                        elif cola_autos > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos -= 1
                            rnd_carga_auto_cont = random.uniform(0, 1)
                            t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
                            fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont
                        else:
                            t2.estado = "Libre"
                            fin_cargan_vehic_cont = 999
                    elif t2.localizacion == "Isla" and trans_en_uso_isla == "T2":
                        if cola_mionca_isla > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla

                        elif cola_autos_isla > 0:
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla
                        else:
                            t2.estado = "Libre"
                            fin_cargan_vehic_isla = 999

                #################################################### FIN DE CARGA MIONCA ISLA #################################
                elif opcion == fin_cargan_vehic_isla:
                    reloj = fin_cargan_vehic_isla
                    fin_cargan_vehic_isla = 999
                    evento = "Fin Carga de Camión Isla"
                    if trans_en_uso_isla == "T1" and t1.estado != "Purga":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca_isla != 0:
                            # Cargo un camión
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla

                        elif t1.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_auto_isla = reloj + t_fin_cargan_vehic_isla
                        elif t1.capacidad == 0:
                            t1.hora_partida = reloj + 0.01

                    elif trans_en_uso_isla == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca_isla != 0:
                            # Cargo un camión
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla
                        elif t2.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_auto_isla = reloj + t_fin_cargan_vehic_isla
                        elif t2.capacidad == 0:
                            t2.hora_partida = reloj + 0.01

                #################################################### FIN DE CARGA AUTO ISLA #################################
                elif opcion == fin_cargan_auto_isla:
                    reloj = fin_cargan_auto_isla
                    fin_cargan_auto_isla = 999
                    evento = "Fin Carga de Auto Isla"
                    if trans_en_uso_isla == "T1" and t1.estado != "Purga":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca_isla != 0:
                            # Cargo un camión
                            t1.estado = "Cargando"
                            t1.capacidad -= 2
                            t1.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla

                        elif t1.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            t1.estado = "Cargando"
                            t1.capacidad -= 1
                            t1.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_auto_isla = reloj + t_fin_cargan_vehic_isla
                        elif t1.capacidad == 0:
                            t1.hora_partida = reloj + 0.01



                    elif trans_en_uso_isla == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca_isla != 0:
                            # Cargo un camión
                            t2.estado = "Cargando"
                            t2.capacidad -= 2
                            t2.cola_mionca += 1
                            cola_mionca_isla -= 1
                            rnd_carga_mionca_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)
                            fin_cargan_vehic_isla = reloj + t_fin_cargan_vehic_isla
                        elif t2.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            t2.estado = "Cargando"
                            t2.capacidad -= 1
                            t2.cola_autos += 1
                            cola_autos_isla -= 1
                            rnd_carga_auto_isla = random.uniform(0, 1)
                            t_fin_cargan_vehic_isla = funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                            fin_cargan_auto_isla = reloj + t_fin_cargan_vehic_isla
                        elif t2.capacidad == 0:
                            t2.hora_partida = reloj + 0.01

                ########################## LLEGADA DE AUTO AL ISLA ##############################
                elif opcion == prox_llegada_auto_isla:
                    ## Llega un auto
                    evento = "Llegada de Auto a Isla"
                    vehic_totales_isla += 1

                    reloj = prox_llegada_auto_isla
                    cola_autos_isla += 1
                    pasa = False
                    if reloj <= 18 and siguen_llegando_autos_isla:
                        rnd_llegada_auto_isla = random.uniform(0, 1)
                        t_auto_isla = funcion_uniforme(rnd_llegada_auto_isla, 0.1167, 0.2833)
                        prox_llegada_auto_isla = reloj + t_auto_isla

                    else:
                        siguen_llegando_autos = False
                        prox_llegada_auto_isla = 999
                    ##

                    if (trans_en_uso_isla == "T1") and t1.estado == "Libre" and t1.capacidad >= 1 and t1.estado != "Purga":
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                        cola_autos_isla -= 1
                        pasa = True
                    elif trans_en_uso_isla == "T2" and t2.estado == "Libre" and t2.capacidad >= 1:
                        t2.estado = "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        cola_autos_isla -= 1
                        pasa = True

                    elif trans_en_uso_isla == "T1" and t1.capacidad == 0 and t1.estado != "Purga":
                        t1.hora_partida = reloj + 0.01
                    elif trans_en_uso == "T2" and t2.capacidad == 0:
                        t2.hora_partida = reloj + 0.01

                    if pasa:
                        rnd_carga_auto_isla = random.uniform(0, 1)
                        t_fin_cargan_auto_isla = + funcion_uniforme(rnd_carga_auto_isla, 0.017, 0.049)
                        fin_cargan_auto_isla = reloj + t_fin_cargan_auto_isla

                    if cola_max_auto_isla <= cola_autos_isla:
                        cola_max_auto_isla = cola_autos_isla

                    ################################### LLEGADA DE CAMION Isla ####################################

                elif opcion == prox_llegada_mionca_isla:
                    evento = "Llegada de Camión/Ómnibus a Isla"
                    reloj = prox_llegada_mionca_isla
                    cola_mionca_isla += 1
                    vehic_totales_isla += 1
                    pasa = False
                    if reloj <= 18 and siguen_llegando_mionca_isla:
                        rnd_llegada_mionca_isla = random.uniform(0, 1)
                        t_mionca_isla = funcion_uniforme(rnd_llegada_mionca_isla, 0.5, 1.5)
                        prox_llegada_mionca_isla = reloj + t_mionca_isla
                    else:
                        siguen_llegando_mionca_isla = False
                        prox_llegada_mionca_isla = 999

                    if (trans_en_uso_isla == "T1") and t1.capacidad >= 2 and t1.estado == "Libre" and t1.estado != "Purga":
                        t1.estado = "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        pasa = True
                        cola_mionca_isla -= 1
                    elif (trans_en_uso_isla == "T2") and t2.capacidad >= 2 and t2.estado == "Libre":
                        t2.estado = "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        pasa = True
                        cola_mionca_isla -= 1

                    elif trans_en_uso_isla == "T1" and t1.capacidad == 0 and t1.estado != "Purga":
                        t1.hora_partida = reloj + 0.01
                    elif trans_en_uso_isla == "T2" and t2.capacidad == 0:
                        t2.hora_partida = reloj + 0.01

                    if pasa:
                        rnd_carga_mionca_isla = random.uniform(0, 1)
                        fin_cargan_vehic_isla = reloj + funcion_uniforme(rnd_carga_mionca_isla, 0.05, 0.082)

                    if cola_max_mionca_isla <= cola_mionca_isla:
                        cola_max_mionca_isla = cola_mionca_isla

                ##################################### FIN DEL DÍA ############################

                elif opcion == fin_del_dia:
                    evento = "Esperando Fin"
                    if t1.estado == "Purga":

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif t1.hora_llegada < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.5
                    elif t2.hora_llegada < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.5
                    elif t1.localizacion != "Continente":

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif t2.localizacion != "Continente":

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif t2.estado == "Descargando":

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif t1.estado == "Descargando":

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif hora_descarga_t1 < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif hora_descarga_t2 < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.3
                    elif fin_cargan_auto_cont < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.2
                    elif fin_cargan_vehic_cont < 40:

                        reloj = fin_del_dia
                        fin_del_dia += 0.2


                    else:
                        evento = "Fin de Día"

                        reloj = fin_del_dia
                        tiempo_purga = 7 +  round(tiempo_purga - reloj, 4)
                        bandera_fin = False

                        cola_esp_man_auto = cola_autos + t1.cola_autos + t2.cola_autos
                        cola_esp_man_mionca = cola_mionca + t1.cola_mionca + t2.cola_mionca
                        cola_esp_man_auto_isla = cola_autos_isla
                        cola_esp_man_mionca_isla = cola_mionca_isla
                        corta = True
                        if dia == 1:
                            cola_esp_man_auto_acum = cola_esp_man_auto_acum + cola_esp_man_auto
                            cola_esp_man_mionca_acum = cola_esp_man_mionca_acum + cola_esp_man_mionca
                        else:
                            cola_esp_man_auto_acum = entry_aux.cola_esp_man_auto_acum + cola_esp_man_auto
                            cola_esp_man_mionca_acum = entry_aux.cola_esp_man_mionca_acum + cola_esp_man_mionca



            entrada = Entrada(evento, dia, reloj,
                              # Llegada continente
                              rnd_llegada_auto_cont, prox_llegada_auto_cont, rnd_llegada_mionca_cont,
                              prox_llegada_mionca_cont,
                              # Colas cont
                              cola_autos, cola_mionca,
                              # Colas Max
                              cola_max_auto, cola_max_mionca,
                              # Flags Espera a mañana cont

                              cola_esp_man_auto, cola_esp_man_mionca, cola_esp_man_auto_acum,
                              cola_esp_man_mionca_acum, cola_esp_man_auto_acum / dia, cola_esp_man_mionca_acum / dia,
                              ( (cola_esp_man_auto_acum+cola_esp_man_mionca_acum)/dia),
                              # Carga cont
                              rnd_carga_mionca_cont, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont,
                              rnd_carga_auto_cont, t_fin_cargan_auto_cont, fin_cargan_auto_cont,
                              ##Trans
                              t1.cola_autos, t1.cola_mionca, t1.hora_partida, t1.estado, t1.localizacion,
                              t2.cola_autos, t2.cola_mionca, t2.hora_partida, t2.estado, t2.localizacion,


                              acum_paso_a_ci,
                              acum_paso_c_ci,
                              acum_paso_a_ci / dia, acum_paso_c_ci / dia,
                              acum_paso_a_ic,acum_paso_c_ic,
                              acum_paso_a_ic/dia, acum_paso_c_ic/dia,
                              ############# PARAM ISLA #########################
                              rnd_llegada_auto_isla, prox_llegada_auto_isla, rnd_llegada_mionca_isla,
                              prox_llegada_mionca_isla,
                              ###Colas
                              cola_autos_isla, cola_mionca_isla, cola_max_auto_isla, cola_max_mionca_isla,
                              cola_esp_man_auto_isla, cola_esp_man_mionca_isla,
                              cola_esp_man_auto_acum_isla, cola_esp_man_mionca_acum_isla,
                              cola_esp_man_auto_acum_isla / dia, cola_esp_man_mionca_acum_isla / dia,
                              ##Colas de carga
                              rnd_carga_mionca_isla, t_fin_cargan_vehic_isla, fin_cargan_vehic_isla,
                              rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_auto_isla, acum_auto_isla,
                              acum_mionca_isla, acum_auto_isla / dia, acum_mionca_isla / dia,
                              autos_totales_cont, autos_totales_cont / dia, camiones_totales_cont,
                              camiones_totales_cont / dia, vehic_totales_isla, vehic_totales_isla / dia,
                              t_t1,t_t2,t_auto,t_mionca,t_auto_isla, t_mionca_isla,
                              rnd_purga, tiempo_purga,fin_de_purga,hora_descarga_t1_lequeda, hora_fin_matenimiento_t1_lequeda, fin_cargan_vehic_cont_lequeda,fin_cargan_auto_cont_lequeda,
                             fin_cargan_auto_islalequeda, fin_cargan_vehic_islalequeda,t1.hora_llegada_lequeda,t1.hora_partida_lequeda
                              )
            primero = True

            if entrada.evento != "Esperando Fin":
                if len(tabla_dia) != 0:
                    if entrada.reloj != tabla_dia[-1].reloj:
                        tabla_dia.append(entrada)

                        # print(entrada.toString(),trans_en_uso, t1.capacidad,t2.capacidad,"--Cola t1---" ,t1.cola_autos ,t1.cola_mionca,"-- Colas t2--",t2.cola_autos, t2.cola_mionca)
                        # print(entrada.toStringIsla())
                else:
                    tabla_dia.append(entrada)


            if corta:
                break

        entry_aux = entrada
        dia_final = []
        aux = tabla_dia
        if dia >= lim_inf and dia <= lim_sup:
            tabla_completa.append(tabla_dia)
        elif dia == cantidad_dias:
            dia_final.append(tabla_dia[-1])
            tabla_completa.append(dia_final)


    entradas = [[entrada for entrada in tabladia] for tabladia in tabla_completa]

    df = pd.DataFrame({'Evento': [entrada.evento for sublist in entradas for entrada in sublist],
                       'Dia': [entrada.dia for sublist in entradas for entrada in sublist],
                       'Reloj': [round(entrada.reloj,2) for sublist in entradas for entrada in sublist],
                       'Random Purga': [round(entrada.rnd_purga,2) for sublist in entradas for entrada in sublist],
                       'Tiempo purga': [round(entrada.tiempo_purga,2) if entrada.tiempo_purga < 100 else 0 for sublist in entradas for entrada in sublist],
                       'Fin de purga': [round(entrada.fin_purga,2) if entrada.fin_purga < 100 else 0 for sublist in entradas for entrada in sublist],
                       'RND llegada A cont' :  [round(entrada.rnd_llegada_auto_cont,2) if entrada.rnd_llegada_auto_cont != 999 else 0 for sublist in entradas for entrada in sublist],
                       'T llegada A cont': [round(entrada.t_auto, 2) for sublist in entradas for entrada in sublist],
                       'Prox llegada A cont': [round(entrada.prox_llegada_auto_cont,2)  if entrada.prox_llegada_auto_cont != 999 else 0for sublist in entradas for entrada in sublist],
                       'RND llegada C cont': [round(entrada.rnd_llegada_mionca_cont,2) for sublist in entradas for entrada in sublist],
                       'T llegada C cont': [round(entrada.t_mionca, 2) for sublist in entradas for entrada in sublist],
                       'Prox llegada C cont': [round(entrada.prox_llegada_mionca_cont,2) if entrada.prox_llegada_mionca_cont != 999 else 0 for sublist in entradas for entrada in sublist],
                       'C. Auto': [entrada.cola_autos_cont for sublist in entradas for entrada in sublist],
                       'C. Camion': [entrada.cola_mionca_cont for sublist in entradas for entrada in sublist],
                       'Max Auto': [entrada.cola_max_autos_cont for sublist in entradas for entrada in sublist],
                       'Max Camion': [entrada.cola_max_mionca_cont for sublist in entradas for entrada in sublist],
                       'E. Auto': [entrada.cola_esp_man_auto for sublist in entradas for entrada in sublist],
                       'EA. Auto': [entrada.cola_esp_man_auto_acum for sublist in entradas for entrada in sublist],
                       'EAP. Auto': [entrada.cola_esp_man_auto_prom for sublist in entradas for entrada in sublist],
                       'E. Camion': [entrada.cola_esp_man_mionca for sublist in entradas for entrada in sublist],
                       'EA. Camion': [entrada.cola_esp_man_mionca_acum for sublist in entradas for entrada in sublist],
                       'EAP. Camion': [entrada.cola_esp_man_mionca_prom for sublist in entradas for entrada in sublist],
                       'Total cont': [entrada.cola_esp_man_total for sublist in entradas for entrada in sublist],
                       'RND Carga camion': [round(entrada.rnd_carga_vehiculo,2) for sublist in entradas for entrada in sublist],
                       'Le queda a la descarga': [round(entrada.hora_descarga_t1_lequeda,2) if entrada.hora_descarga_t1_lequeda <= 100 else 0 for sublist in entradas for entrada in sublist],
                       'Le queda al mantenimiento': [round(entrada.hora_fin_matenimiento_t1_lequeda,2) if entrada.hora_fin_matenimiento_t1_lequeda <= 100 else 0 for sublist in entradas for entrada in sublist],
                       'Le queda a la carga de vehículo:': [round(entrada.getMax(),2) if entrada.getMax() <= 100 else 0 for sublist in entradas for entrada in sublist],
                       'T. Carga camion': [round(entrada.tiempo_carga_vehic,2) for sublist in entradas for entrada in sublist],
                       'T. Final camion': [round(entrada.tiempo_final_vehic,2)  if entrada.tiempo_final_vehic != 999 else 0 for sublist in entradas for entrada in sublist],
                       'RND Carga auto': [round(entrada.rnd_carga_auto,2) for sublist in entradas for entrada in sublist],
                       'T. Carga auto': [round(entrada.tiempo_carga_auto,2) for sublist in entradas for entrada in sublist],
                       'T. Final auto': [round(entrada.tiempo_final_auto,2)  if entrada.tiempo_final_auto != 999 else 0 for sublist in entradas for entrada in sublist],
                       'Cola auto T1': [entrada.t1_cola_autos for sublist in entradas for entrada in sublist],
                       'Cola camion T1': [entrada.t1_cola_mionca for sublist in entradas for entrada in sublist],
                       'T Partida T1': [round(entrada.t_t1, 2) for sublist in entradas for entrada in sublist],
                       'T Partida T1 le queda': [round(entrada.hora_partida_lequeda,2) if entrada.hora_partida_lequeda <= 100 else 0 for sublist in entradas for entrada in sublist],
                       'T Llegada T1 le queda': [round(entrada.hora_llegada_lequeda,2) if entrada.hora_llegada_lequeda <= 100 else 0 for sublist in entradas for entrada in
                                                 sublist],
                       'Hora partida T1': [round(entrada.t1_hora_partida,2)  if entrada.t1_hora_partida != 999 else 0 for sublist in entradas for entrada in sublist],
                       'Estado T1': [entrada.t1_estado for sublist in entradas for entrada in sublist],
                       'Localizacion T1': [entrada.t1_localizacion for sublist in entradas for entrada in sublist],
                       'Cola auto T2': [entrada.t2_cola_autos for sublist in entradas for entrada in sublist],
                       'Cola camion T2': [entrada.t2_cola_mionca for sublist in entradas for entrada in sublist],
                       'T Partida T2': [round(entrada.t_t2, 2) for sublist in entradas for entrada in sublist],
                       'Hora partida T2': [round(entrada.t2_hora_partida,2) if entrada.t2_hora_partida != 999 else 0 for sublist in entradas for entrada in sublist],
                       'Estado T2': [entrada.t2_estado for sublist in entradas for entrada in sublist],
                       'Localizacion T2': [entrada.t2_localizacion for sublist in entradas for entrada in sublist],
                       'A. Auto': [entrada.acum_paso_auto for sublist in entradas for entrada in sublist],
                       'Prom Auto': [round(entrada.prom_paso_auto,2) for sublist in entradas for entrada in sublist],
                       'A. Camion': [entrada.acum_paso_mionca for sublist in entradas for entrada in sublist],
                       'Prom. Camion': [round(entrada.prom_paso_mionca,2) for sublist in entradas for entrada in sublist],
                       'RND llegada C isla':[round(entrada.rnd_llegada_mionca_isla,2) for sublist in entradas for entrada in sublist],
                       'T llegada C Isla': [round(entrada.t_mionca_isla, 2) for sublist in entradas for entrada in sublist],
                       'Prox llegada C isla': [round(entrada.prox_llegada_mionca_isla)  if entrada.prox_llegada_mionca_isla != 999 else 0 for sublist in entradas for entrada in sublist],
                       'RND llegada A isla': [round(entrada.rnd_llegada_auto_isla,2) for sublist in entradas for entrada in
                                              sublist],
                       'T llegada A Isla': [round(entrada.t_auto_isla, 2) for sublist in entradas for entrada in sublist],
                       'Prox llegada A isla': [round(entrada.prox_llegada_auto_isla,2)  if entrada.prox_llegada_auto_isla != 999 else 0 for sublist in entradas for entrada in sublist],
                       'Cola auto Isla': [entrada.cola_autos_isla for sublist in entradas for entrada in sublist],
                       'Cola camion Isla': [entrada.cola_mionca_isla for sublist in entradas for entrada in sublist],
                       'Max auto Isla': [entrada.cola_max_autos_isla for sublist in entradas for entrada in sublist],
                       'Max camion Isla': [entrada.cola_max_mionca_isla for sublist in entradas for entrada in sublist],
                       'EM auto': [entrada.cola_esp_man_auto_isla for sublist in entradas for entrada in sublist],
                       'EMA auto': [entrada.cola_esp_man_auto_acum_isla for sublist in entradas for entrada in sublist],
                       'EMP auto': [entrada.cola_esp_man_auto_prom_isla for sublist in entradas for entrada in sublist],
                       'EM camion': [entrada.cola_esp_man_mionca_isla for sublist in entradas for entrada in sublist],
                       'EMA camion': [entrada.cola_esp_man_mionca_acum_isla for sublist in entradas for entrada in
                                      sublist],
                       'EMP camion': [entrada.cola_esp_man_mionca_prom_isla for sublist in entradas for entrada in
                                      sublist],
                       'Total isla': [entrada.cola_esp_man_total_isla for sublist in entradas for entrada in sublist],
                       'RND T. Carga C isla': [round(entrada.rnd_carga_vehiculo_isla,2) for sublist in entradas for entrada in sublist],
                       'T. Carga C': [round(entrada.tiempo_carga_isla,2)  if entrada.tiempo_carga_isla != 999 else 0 for sublist in entradas for entrada in sublist],
                       'T. Final C': [round(entrada.tiempo_final_vehic_isla,2)  if entrada.tiempo_final_vehic_isla != 999 else 0 for sublist in entradas for entrada in sublist],
                       'RND Carga A isla': [round(entrada.rnd_carga_auto_isla,2) for sublist in entradas for entrada in
                                               sublist],
                       'T. Carga A': [round(entrada.tiempo_carga_auto_isla,2) for sublist in entradas for entrada in sublist],
                       'T. Final A': [round(entrada.tiempo_final_auto_isla,2)  if entrada.tiempo_final_auto_isla != 999 else 0 for sublist in entradas for entrada in sublist],
                       'Acum Autos': [entrada.acum_paso_auto_isla for sublist in entradas for entrada in sublist],
                       'Prom Autos': [round(entrada.prom_paso_auto_isla,2) for sublist in entradas for entrada in sublist],
                       'Acum Camiones': [entrada.acum_paso_mionca_isla for sublist in entradas for entrada in sublist],
                       'Prom Camiones': [round(entrada.prom_paso_mionca_isla,2) for sublist in entradas for entrada in sublist],
                       'Acum Auto Cont': [entrada.acum_auto_cont for sublist in entradas for entrada in sublist],
                       'Prom Autos Cont': [round(entrada.prom_auto_cont,2) for sublist in entradas for entrada in sublist],
                       'Acum Camion Cont': [entrada.acum_camion_cont for sublist in entradas for entrada in sublist],
                       'Prom Camión Cont': [round(entrada.prom_camion_cont,2) for sublist in entradas for entrada in sublist],
                       'Acumulado Vehic isla': [entrada.acum_vehic_isla for sublist in entradas for entrada in sublist],
                       'Prom Vehic Isla': [round(entrada.prom_vehic_isla,2) for sublist in entradas for entrada in sublist],
                       'Acum Paso A CI': [entrada.acum_paso_auto for sublist in entradas for entrada in sublist],
                       'Prom Paso A CI': [round(entrada.prom_paso_auto,2) for sublist in entradas for entrada in sublist],
                       'Acum Paso C CI': [entrada.acum_paso_mionca for sublist in entradas for entrada in sublist],
                       'Acum Paso A IC': [entrada.acum_paso_auto_ic for sublist in entradas for entrada in sublist],
                       'Prom Paso A IC': [round(entrada.prom_paso_auto_ic,2) for sublist in entradas for entrada in sublist],
                       'Acum Paso C IC': [entrada.acum_paso_mionca_ic for sublist in entradas for entrada in sublist],
                       'Prom Paso C IC': [round(entrada.prom_paso_mionca_ic,2) for sublist in entradas for entrada in sublist],



                       })

    return df
    #print(len(tabla_completa))
    #for i in range(len(tabla_completa)):
    #    for j in range(len(tabla_completa[i])):
    #        print(tabla_completa[i][j].toString())
#
    #print(df)
#generar_miles(20,5,19)




