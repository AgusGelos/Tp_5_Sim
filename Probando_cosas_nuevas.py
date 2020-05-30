import math
import random

from Class.Entrada_class import Entrada
from Class.Trans_Class import Transbordador
from Class.Entrada_Cont_prueba import Entrada_prueba


def hora_de_irse(t1,t2,reloj):
    if t1.capacidad == 0:
        t1.hora_partida = reloj + 0.01
    if t2.capacidad == 0:
        t2.hora_partida = reloj + 0.01
    return t1,t2


def funcion_uniforme(rnd,lim_inf, lim_sup):
    return lim_inf + rnd*(lim_sup-lim_inf)

def cargar_auto(reloj, t1, cola_autos):
    fin_cargan_auto_cont = 999
    rnd_carga_auto_cont,t_fin_cargan_vehic_cont = 0,0
    if t1.capacidad >= 1 and cola_autos != 0:
        # Cargo un auto
        t1.estado = "Cargando"
        t1.capacidad -= 1
        t1.cola_autos += 1
        cola_autos -= 1
        rnd_carga_auto_cont = random.uniform(0, 1)
        t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_auto_cont, 0.017, 0.049)
        fin_cargan_auto_cont = reloj + t_fin_cargan_vehic_cont
    else:
        t1.estado = "Libre"


    return rnd_carga_auto_cont,t_fin_cargan_vehic_cont, fin_cargan_auto_cont, cola_autos,t1

def cargar_mionca(reloj, t1, cola_mionca):
    fin_cargan_mionca_cont = 999
    rnd_carga_mionca_cont,t_fin_cargan_vehic_cont = 0,0
    if t1.capacidad >= 2 and cola_mionca != 0:
        # Cargo un camion
        t1.estado = "Cargando"
        t1.capacidad -= 2
        t1.cola_mionca += 1
        cola_mionca -= 1
        rnd_carga_mionca_cont = random.uniform(0, 1)
        t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.017, 0.049)
        fin_cargan_mionca_cont = reloj + t_fin_cargan_vehic_cont
    else:
        t1.estado = "Libre"

    return rnd_carga_mionca_cont,t_fin_cargan_vehic_cont, fin_cargan_mionca_cont,  cola_mionca,t1

def generar_miles(cantidad_dias):

    tabla_dia = []
    tabla_completa = []

    t1 = Transbordador(0,0,10, 9, "Libre", "Continente", 5,99,"Continente")
    t2 = Transbordador(0,0,20, 10, "Libre", "Continente", 10,99,"Continente")

    cola_max_auto, cola_max_mionca, cola_max_mionca_isla, cola_max_auto_isla = 0,0,0,0
    for i in range(cantidad_dias):
        ############# Parámetros de entrada
        if i != 0:
            tabla_completa.append(tabla_dia)
        tabla_dia = []
        reloj = 7
        evento = "Inicio del Día"
        rnd_llegada_mionca_cont = random.uniform(0, 1)
        prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)
        rnd_llegada_auto_cont = random.uniform(0, 1)
        prox_llegada_auto_cont = 7.5 + funcion_uniforme(rnd_llegada_auto_cont, 0.16, 0.33)
        trans_en_uso = "T1"
        hora_descarga_t1, hora_descarga_t2 = 999,999
        dia = 1
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
            acum_auto = tabla_completa[-1][-1].acum_paso_auto
            acum_mionca = tabla_completa[-1][-1].acum_paso_mionca
            acum_auto_isla = tabla_completa[-1][-1].acum_paso_auto_isla
            acum_mionca_isla = tabla_completa[-1][-1].acum_paso_mionca_isla

        corta = False
        #########################################################   CICLO     ###################################################
        while reloj != 20:
            cola_esp_man_auto = 0
            cola_esp_man_mionca = 0
            cola_esp_man_mionca_acum= 0
            cola_esp_man_auto_acum = 0

            t_fin_cargan_auto_isla, t_fin_cargan_vehic_cont, t_fin_cargan_vehic_isla, t_fin_cargan_auto_cont = 0,0,0,0
            rnd_llegada_auto_cont = 0
            rnd_llegada_mionca_cont = 0
            rnd_carga_mionca_cont,rnd_carga_auto_cont,rnd_carga_auto_isla,rnd_carga_mionca_isla = 0,0,0,0
            ############################################## param ISLA ##################################+
            cola_esp_man_auto_isla = 0
            cola_esp_man_mionca_isla = 0
            cola_esp_man_mionca_acum_isla = 0
            cola_esp_man_auto_acum_isla = 0
            t_fin_cargan_vehic_isla = 0
            rnd_llegada_auto_isla = 0
            rnd_llegada_mionca_isla = 0

            ############################################## COLA DE AYER ##########################################

            if (len(tabla_completa) != 0) and reloj == 7:
                cola_autos = tabla_completa[-1][-1].cola_esp_man_auto
                cola_mionca = tabla_completa[-1][-1].cola_esp_man_mionca
                cola_autos_isla = tabla_completa[-1][-1].cola_esp_man_auto_isla
                cola_mionca_isla = tabla_completa[-1][-1].cola_esp_man_mionca_isla
                ##Prox Carga de vehículo:

                if cola_mionca > 0 and hora_fin_matenimiento_t1 == 999:
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca += 1
                    cola_mionca -= 1
                    rnd_carga_mionca_cont = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga_mionca_cont, 0.05, 0.082)

                    fin_cargan_vehic_cont = reloj + t_fin_cargan_vehic_cont

                elif cola_autos > 0 and hora_fin_matenimiento_t1 == 999:
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


            if primero  :
                ########################################## OPCIÓN DE MINIMO ########################################################

                opcion = min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, fin_cargan_auto_cont,
                             t1.hora_partida, t2.hora_partida,t1.hora_llegada,t2.hora_llegada,
                             hora_descarga_t1, hora_descarga_t2,
                             hora_fin_matenimiento_t1,hora_fin_matenimiento_t2,fin_del_dia,
                             ################ Isleños ################
                             prox_llegada_auto_isla,prox_llegada_mionca_isla,fin_cargan_auto_isla,fin_cargan_vehic_isla
                             )


                ########################################## Curso normal ##################################################

                #################################################### FIN MANTENIMIENTO T1 #########################################
                if opcion == hora_fin_matenimiento_t1:
                    evento = "Fin Mantenimiento T1"
                    t1.estado = "Libre"
                    reloj = hora_fin_matenimiento_t1
                    t1.hora_partida = reloj + 1
                    hora_fin_matenimiento_t1 = 999
                    if t2.localizacion != "Continente":
                        trans_en_uso = "T1"
                        if cola_mionca > 0:
                            rnd_carga_mionca_cont,t_fin_cargan_vehic_cont,fin_cargan_vehic_cont,cola_mionca,t1 = cargar_mionca(reloj, t1, cola_mionca)

                        elif cola_autos > 0:
                            rnd_carga_auto_cont, t_fin_cargan_vehic_cont, fin_cargan_auto_cont, cola_autos, t1 = cargar_auto(
                                reloj, t1, cola_autos)

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
                    if trans_en_uso == "T1":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca !=0:
                            rnd_carga_mionca_cont, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont, cola_mionca, t1 = cargar_mionca(
                                reloj, t1, cola_mionca)
                        elif t1.capacidad >= 1 and cola_autos != 0:
                            rnd_carga_auto_cont, t_fin_cargan_auto_cont, fin_cargan_auto_cont, cola_autos, t1 = cargar_auto(
                                reloj, t1, cola_autos)
                    elif trans_en_uso == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca != 0:
                            # Cargo un Camión
                            rnd_carga_mionca_cont, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont, cola_mionca, t2 = cargar_mionca(
                                reloj, t2, cola_mionca)
                        elif t2.capacidad >= 1 and cola_autos != 0:
                            # Cargo un auto
                            rnd_carga_auto_cont, t_fin_cargan_auto_cont, fin_cargan_auto_cont, cola_autos, t2 = cargar_auto(
                                reloj, t2, cola_mionca)
                    t1,t2 = hora_de_irse(t1,t2,reloj)

                #################################################### FIN DE CARGA AUTO CONT #################################
                elif opcion == fin_cargan_auto_cont:
                    reloj = fin_cargan_auto_cont
                    fin_cargan_auto_cont = 999

                    evento = "Fin Carga de Auto Cont"
                    if trans_en_uso == "T1":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca != 0:
                            rnd_carga_mionca_cont, t_fin_cargan_vehic_cont,fin_cargan_vehic_cont, cola_mionca,t1 = cargar_mionca(reloj, t1, cola_mionca)
                        elif t1.capacidad >= 1 and cola_autos != 0:
                            rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_vehic_cont,cola_autos,t1 = cargar_auto(reloj, t1, cola_autos)
                    elif trans_en_uso == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca != 0:
                            #Cargo un Camión
                            rnd_carga_mionca_cont,t_fin_cargan_vehic_cont,fin_cargan_vehic_cont,cola_mionca,t2 = cargar_mionca(reloj, t2, cola_mionca)
                        elif t2.capacidad >= 1 and cola_autos != 0:
                            #Cargo un auto
                            rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_auto_cont,cola_autos,t2 = cargar_auto(reloj, t2, cola_mionca)

                    t1, t2 = hora_de_irse(t1, t2, reloj)


            ########################## LLEGADA DE AUTO AL CONTINENTE ##############################
                elif opcion == prox_llegada_auto_cont:
                    ## Llega un auto
                    evento = "Llegada de Auto a Continente"

                    reloj = prox_llegada_auto_cont
                    cola_autos += 1

                    if reloj <=12 and siguen_llegando_autos:
                        rnd_llegada_auto_cont = random.uniform(0,1)
                        prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.167,0.33)
                    elif reloj <=19 and siguen_llegando_autos:
                        rnd_llegada_auto_cont = random.uniform(0, 1)
                        prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont, 0.417, 0.583)
                    else:
                        siguen_llegando_autos = False
                        prox_llegada_auto_cont = 999
                    ##

                    if (trans_en_uso == "T1") and t1.estado == "Libre":
                        rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_auto_cont,cola_autos,t1 = cargar_auto(reloj, t1, cola_autos)
                    elif trans_en_uso == "T2" and t2.estado == "Libre":
                        rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_auto_cont,cola_autos,t2 = cargar_auto(reloj, t2, cola_autos)





                ################################### LLEGADA DE CAMION ####################################

                elif opcion == prox_llegada_mionca_cont:
                    evento = "Llegada de Camión/Ómnibus a Continente"
                    reloj = prox_llegada_mionca_cont
                    cola_mionca += 1

                    if reloj <= 11 and siguen_llegando_mionca:
                        rnd_llegada_mionca_cont = random.uniform(0, 1)
                        prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.314, 0.346)
                    elif reloj <= 19.5 and siguen_llegando_mionca:
                        rnd_llegada_mionca_cont = random.uniform(0, 1)
                        prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 1.917, 2.083)
                    else:
                        siguen_llegando_mionca = False
                        prox_llegada_mionca_cont = 999


                    if (trans_en_uso == "T1") and t1.estado == "Libre":
                        rnd_carga_mionca_cont,t_fin_cargan_vehic_cont,fin_cargan_vehic_cont,cola_mionca,t1 = cargar_mionca(reloj, t1, cola_mionca)
                    elif (trans_en_uso == "T2") and t2.estado == "Libre":
                        rnd_carga_mionca_cont,t_fin_cargan_vehic_cont,fin_cargan_vehic_cont,cola_mionca,t2 = cargar_mionca(reloj, t2, cola_mionca)



                ############################### PARTE EL FERRY CHU CHUUU######################pame la pija#############
                elif opcion == t1.hora_partida:
                    #Revisar desde donde sale y liberar el T

                    if reloj >= 20 and t1.localizacion == "Continente":
                        t1.hora_partida = 999
                    else:

                        if t1.estado == "Cargando":
                            evento = "Esperando fin de carga"
                            if t1.localizacion == "Continente":
                                if fin_cargan_auto_cont == 999:
                                    t1.hora_partida = fin_cargan_vehic_cont + 0.01
                                else:
                                    t1.hora_partida = fin_cargan_auto_cont + 0.01
                            else: #isla
                                if fin_cargan_auto_isla == 999:
                                    t1.hora_partida = fin_cargan_vehic_isla + 0.01
                                else:
                                    t1.hora_partida = fin_cargan_auto_isla +0.01
                        else:
                            #Reviso que sea del continente o la isla
                            reloj = t1.hora_partida
                            t1.hora_partida = 999
                            if t1.localizacion == "Continente":
                                evento = "Salida T1 Cont-Isla"
                                if t2.localizacion == "Continente" and t2.estado != "Mantenimiento":
                                    trans_en_uso = "T2"
                                else:
                                    trans_en_uso = "T3"
                                t1.hora_llegada = reloj + random.uniform(0.917,1.084)
                                t1.puerto_salida = t1.localizacion
                                t1.localizacion = "Mar"
                                t1.hora_partida = t1.hora_llegada + 1

                            else:
                                evento = "Salida T1 Isla-Cont"
                                t1.hora_partida = 999

                                if t2.localizacion == "Isla":
                                    trans_en_uso_isla = "T2"
                                else:
                                    trans_en_uso_isla = "T3"

                                t1.hora_llegada = reloj + random.uniform(0.917, 1.084)
                                t1.puerto_salida = t1.localizacion
                                t1.localizacion = "Mar"

            ################################# SALE EL SEGUNDO FERRY #######################################
                elif opcion == t2.hora_partida:

                    if t2.hora_partida >= 20 and t2.localizacion == "Continente":
                        t2.hora_partida = 999
                    else:
                        if t2.estado == "Cargando":
                            evento = "Esperando Fin de Carga"
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
                                t2.hora_llegada = reloj + random.uniform(0.917, 1.084)
                                t2.puerto_salida = t2.localizacion
                                t2.localizacion = "Mar"
                                t2.hora_partida = t2.hora_llegada + 1

                            else:
                                evento = "Salida T2 Isla-Cont"

                                if t1.localizacion == "Isla":
                                    trans_en_uso_isla = "T1"
                                else:
                                    trans_en_uso_isla = "T3"

                                t2.hora_llegada = reloj + random.uniform(0.917, 1.084)
                                t2.puerto_salida = t2.localizacion
                                t2.localizacion = "Mar"
                                t2.hora_partida = t2.hora_llegada +1

               #################################Llegada de ferry 1 al continente###################################
                elif opcion == t1.hora_llegada:
                    acum_auto += t1.cola_autos
                    acum_mionca += t1.cola_mionca
                    reloj = t1.hora_llegada
                    hora_descarga_t1 = reloj

                    if t1.puerto_salida == "Isla":
                        evento = "Llegada T1 a Continente"
                        t1.estado = "Descargando"
                        t1.localizacion = "Continente"
                        for i in range(t1.cola_autos):
                            hora_descarga_t1 += random.uniform(0.0077,0.024)
                        for i in range(t1.cola_mionca):
                            hora_descarga_t1 += random.uniform(0.024,0.041)

                        if t2.localizacion != "Continente" or t2.estado == "Mantenimiento":
                            trans_en_uso = "T1"
                    else:
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
                elif opcion == hora_descarga_t1:
                    if t1.localizacion == "Continente":
                        evento = "Fin de descarga T1 Continente"
                    else:
                        evento = "Fin de descarga T1 Isla"

                    reloj = hora_descarga_t1
                    hora_descarga_t1 = 999
                    t1.cola_autos = 0
                    t1.cola_mionca = 0
                    t1.capacidad = 10
                    t1.hora_partida = reloj + 1
                    if t1.localizacion == "Continente" and trans_en_uso == "T1" and reloj <= 20:
                        if cola_mionca > 0:
                            rnd_carga_mionca_cont,t_fin_cargan_vehic_cont,fin_cargan_vehic_cont,cola_mionca,t1 = cargar_mionca(reloj,t1,cola_mionca)

                        elif cola_autos > 0:
                            rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_auto_cont,cola_autos,t1 = cargar_auto(reloj,t1,cola_autos)
                        else:
                            t1.estado = "Libre"
                            fin_cargan_vehic_cont = 999

                    elif t1.localizacion == "Isla" and trans_en_uso_isla == "T1":
                        if cola_mionca_isla > 0:
                            rnd_carga_mionca_isla,t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,cola_mionca_isla,t1 = cargar_mionca(reloj,t1,cola_mionca_isla)

                        elif cola_autos_isla > 0:
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_auto_isla, cola_autos_isla, t1 = cargar_auto(
                                reloj, t1, cola_autos_isla)
                        else:
                            t1.estado = "Libre"
                            fin_cargan_vehic_isla = 999


                ######################## FIN Descarga T2 ######################################
                elif opcion == hora_descarga_t2:
                    if t2.localizacion == "Continente":
                        evento = "Fin de descarga T2 Contiente"
                    else:
                        evento = "Fin de descarga T2 Isla"
                    reloj = hora_descarga_t2
                    hora_descarga_t2 = 999
                    t2.cola_autos = 0
                    t2.cola_mionca = 0
                    t2.capacidad = 20
                    t2.hora_partida = reloj + 1

                    if t2.localizacion == "Continente" and trans_en_uso == "T2" and reloj <= 20:
                        if cola_mionca > 0:
                            rnd_carga_mionca_cont, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont, cola_mionca, t2 = cargar_mionca(
                                reloj, t2, cola_mionca)

                        elif cola_autos > 0:
                            rnd_carga_auto_cont, t_fin_cargan_auto_cont, fin_cargan_auto_cont, cola_autos, t2 = cargar_auto(
                                reloj, t2, cola_autos)
                        else:
                            t2.estado = "Libre"
                            fin_cargan_vehic_cont = 999

                    elif t2.localizacion == "Isla" and trans_en_uso_isla == "T2":
                        if cola_mionca_isla > 0:
                            rnd_carga_mionca_isla, t_fin_cargan_vehic_isla, fin_cargan_vehic_isla, cola_mionca_isla, t1 = cargar_mionca(
                                reloj, t1, cola_mionca_isla)

                        elif cola_autos_isla > 0:
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_auto_isla, cola_autos_isla, t1 = cargar_auto(
                                reloj, t1, cola_autos_isla)
                        else:
                            t1.estado = "Libre"
                            fin_cargan_vehic_isla = 999

                #################################################### FIN DE CARGA MIONCA ISLA #################################
                elif opcion == fin_cargan_vehic_isla:
                    reloj = fin_cargan_vehic_isla
                    fin_cargan_vehic_isla = 999
                    evento = "Fin Carga de Camión Isla"
                    if trans_en_uso_isla == "T1" :
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca_isla != 0 :
                            rnd_carga_mionca_isla, t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,cola_mionca_isla,t1 = cargar_mionca(reloj,t1,cola_mionca_isla)

                        elif t1.capacidad >= 1 and cola_autos_isla != 0:
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_vehic_isla,cola_autos_isla,t1 = cargar_auto(reloj,t1,cola_autos_isla)


                    elif trans_en_uso_isla == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca_isla != 0:
                            rnd_carga_mionca_isla, t_fin_cargan_vehic_isla, fin_cargan_vehic_isla, cola_mionca_isla, t2 = cargar_mionca(
                                reloj, t2, cola_mionca_isla)

                        elif t2.capacidad >= 1 and cola_autos_isla != 0:
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_vehic_isla, cola_autos_isla, t2 = cargar_auto(
                                reloj, t2, cola_autos_isla)

                    t1, t2 = hora_de_irse(t1, t2, reloj)

                #################################################### FIN DE CARGA AUTO ISLA #################################
                elif opcion == fin_cargan_auto_isla:
                    reloj = fin_cargan_auto_isla
                    fin_cargan_auto_isla = 999
                    evento = "Fin Carga de Auto Isla"
                    if trans_en_uso_isla == "T1":
                        t1.estado = "Libre"
                        if t1.capacidad >= 2 and cola_mionca != 0:
                            #cargo un camión
                            rnd_carga_mionca_isla,t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,cola_mionca_isla,t1 = cargar_mionca(reloj,t1,cola_mionca_isla)
                        elif t1.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_auto_isla, cola_autos_isla, t1 = cargar_auto(
                                reloj, t1, cola_autos_isla)
                    elif trans_en_uso_isla == "T2":
                        t2.estado = "Libre"
                        if t2.capacidad >= 2 and cola_mionca_isla != 0:
                            # cargo un camión
                            rnd_carga_mionca_isla, t_fin_cargan_vehic_isla, fin_cargan_vehic_isla, cola_mionca_isla, t2 = cargar_mionca(
                                reloj, t2, cola_mionca_isla)
                        elif t1.capacidad >= 1 and cola_autos_isla != 0:
                            # Cargo un auto
                            rnd_carga_auto_isla, t_fin_cargan_auto_isla, fin_cargan_auto_isla, cola_autos_isla, t2 = cargar_auto(
                                reloj, t2, cola_autos_isla)

                        t1, t2 = hora_de_irse(t1, t2, reloj)
                ########################## LLEGADA DE AUTO AL ISLA ##############################
                elif opcion == prox_llegada_auto_isla:
                    ## Llega un auto
                    evento = "Llegada de Auto a Isla"

                    reloj = prox_llegada_auto_isla
                    cola_autos_isla += 1

                    if reloj <= 18 and siguen_llegando_autos_isla:
                        rnd_llegada_auto_isla = random.uniform(0, 1)
                        prox_llegada_auto_isla = reloj + funcion_uniforme(rnd_llegada_auto_isla, 0.1167, 0.2833)

                    else:
                        siguen_llegando_autos = False
                        prox_llegada_auto_isla = 999
                    ##

                    if (trans_en_uso_isla == "T1") and t1.estado == "Libre" :
                        rnd_carga_auto_isla,t_fin_cargan_auto_isla,fin_cargan_auto_cont,cola_autos_isla,t1 = cargar_auto(reloj,t1,cola_autos_isla)

                    elif trans_en_uso_isla == "T2" and t2.estado == "Libre":
                        rnd_carga_auto_isla,t_fin_cargan_auto_isla,fin_cargan_auto_cont,cola_autos_isla,t2 = cargar_auto(reloj,t2,cola_autos_isla)



                        ################################### LLEGADA DE CAMION Isla ####################################

                elif opcion == prox_llegada_mionca_isla:
                    evento = "Llegada de Camión/Ómnibus a Isla"
                    reloj = prox_llegada_mionca_isla
                    cola_mionca_isla += 1
                    pasa = False
                    if reloj <= 18 and siguen_llegando_mionca_isla:
                        rnd_llegada_mionca_isla = random.uniform(0, 1)
                        prox_llegada_mionca_isla = reloj + funcion_uniforme(rnd_llegada_mionca_isla, 0.5, 1.5)
                    else:
                        siguen_llegando_mionca_isla = False
                        prox_llegada_mionca_isla = 999

                    if (trans_en_uso_isla == "T1") and t1.estado == "Libre":
                        rnd_carga_mionca_isla,t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,cola_mionca_isla,t1 =cargar_mionca(reloj,t1,cola_mionca_isla)

                    elif (trans_en_uso_isla == "T2") and t2.estado == "Libre":
                        rnd_carga_mionca_isla,t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,cola_mionca_isla,t2 =cargar_mionca(reloj,t2,cola_mionca_isla)


                ##################################### FIN DEL DÍA ############################
                elif opcion == fin_del_dia:
                    evento = "Esperando Fin"
                    if t1.localizacion != "Continente":
                        fin_del_dia += 0.3
                    elif t2.localizacion != "Continente":
                        fin_del_dia += 0.3
                    elif fin_cargan_auto_cont != 999:
                        fin_del_dia += 0.2
                    elif fin_cargan_vehic_cont != 999:
                        fin_del_dia +=0.2

                    else:
                        evento = "Fin de Día"
                        dia += 1
                        reloj = fin_del_dia

                        cola_esp_man_auto = cola_autos + t1.cola_autos + t2.cola_autos
                        cola_esp_man_mionca = cola_max_mionca + t1.cola_mionca + t2.cola_mionca
                        corta = True
                        try:
                            cola_esp_man_auto_acum = tabla_dia[-1].cola_esp_man_auto_acum + cola_esp_man_auto
                            cola_esp_man_mionca_acum = tabla_dia[-1].cola_esp_man_mionca_acum + cola_esp_man_mionca
                        except:
                            cola_esp_man_auto_acum = cola_esp_man_auto
                            cola_esp_man_mionca_acum = cola_esp_man_mionca



            entrada = Entrada(evento, dia, reloj,
            # Llegada continente
            rnd_llegada_auto_cont, prox_llegada_auto_cont, rnd_llegada_mionca_cont, prox_llegada_mionca_cont,
            # Colas cont
            cola_autos, cola_mionca,
            # Colas Max
            cola_max_auto, cola_max_mionca,
            # Flags Espera a mañana cont

            cola_esp_man_auto, cola_esp_man_mionca, cola_esp_man_auto_acum,
            cola_esp_man_mionca_acum, cola_esp_man_auto_acum/dia, cola_esp_man_mionca_acum/dia,
            # Carga cont
            rnd_carga_mionca_cont, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont,rnd_carga_auto_cont,t_fin_cargan_auto_cont,fin_cargan_auto_cont, t1, t2, acum_auto, acum_mionca,
            acum_auto/dia, acum_mionca/dia,
            ############# PARAM ISLA #########################
            rnd_llegada_auto_isla,prox_llegada_auto_isla,rnd_llegada_mionca_isla,prox_llegada_mionca_isla,
            ###Colas
            cola_autos_isla,cola_mionca_isla,cola_max_auto_isla,cola_max_mionca_isla,cola_esp_man_auto_isla,cola_esp_man_mionca_isla,
            cola_esp_man_auto_acum_isla, cola_esp_man_mionca_acum_isla,cola_esp_man_auto_acum_isla/dia,cola_esp_man_mionca_acum_isla/dia,
                              ##Colas de carga
            rnd_carga_mionca_isla,t_fin_cargan_vehic_isla,fin_cargan_vehic_isla,rnd_carga_auto_isla,t_fin_cargan_auto_isla, fin_cargan_auto_isla,acum_auto_isla,acum_mionca_isla,acum_auto_isla/dia, acum_mionca_isla/dia
            )
            tabla_dia.append(entrada)
            primero = True
            print(entrada.toString(),trans_en_uso, t1.capacidad,t2.capacidad,"--Cola t1---" ,t1.cola_autos ,t1.cola_mionca,"-- Colas t2--",t2.cola_autos, t2.cola_mionca)
            print(entrada.toStringIsla())
            if corta:
                break


generar_miles(1)




