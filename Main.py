import math
import random

from Class.Entrada_class import Entrada
from Class.Trans_Class import Transbordador
from Class.Entrada_Cont_prueba import Entrada_prueba



def funcion_uniforme(rnd,lim_inf, lim_sup):
    return lim_inf + rnd*(lim_sup-lim_inf)

def generar_miles(cantidad_dias):

    tabla_dia = []
    tabla_completa = []

    t1 = Transbordador(0,0,10, 9, "Libre", "Continente", 5,99,"Continente")
    t2 = Transbordador(0,0,20, 10, "Libre", "Continente", 10,99,"Continente")

    cola_max_auto, cola_max_mionca = 0,0
    for i in range(cantidad_dias):
        ############# Parámetros de entrada
        if i != 0:
            tabla_completa.append(tabla_dia)
        reloj = 7
        evento = "Inicio del Día"
        prox_llegada_auto_cont = 999
        rnd_llegada_mionca_cont = random.uniform(0, 1)
        prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)
        trans_en_uso = "T1"
        hora_descarga_t1, hora_descarga_t2 = 9999,9999
        dia = 1
        siguen_llegando_autos = True
        siguen_llegando_mionca = True
        fin_cargan_vehic_cont = 999
        primer = True
        #Establecer estados de Trans a valores iniciales o mantenimiento
        if i == t1.mantenimiento:
            t1.estado = "Mantenimiento"
            t1.mantenimiento += 10
            hora_fin_matenimiento = 13
        elif i == t2.mantenimiento:
            t2.estado = "Mantenimiento"
            t2.mantenimiento += 10
            hora_fin_matenimiento = 13
        else:
            t1.estado = "Libre"
            t1.localizacion = "Continente"
            t1.hora_partida = 9
            t2.estado = "Libre"
            t2.localizacion = "Continente"
            t2.hora_partida = 10
            hora_fin_matenimiento = 9999999

        ##Establecer el valor de las colas
        if i == 0:
            cola_autos = 0
            cola_mionca = 0
            acum_auto = 0
            acum_mionca = 0
        else:
            acum_auto = tabla_completa[-1][-1].acum_paso_auto
            acum_mionca = tabla_completa[-1][-1].acum_paso_mionca


#################################################################   Antes de las 8       ###################################################
        while reloj != 20:
            cola_esp_man_auto = 0
            cola_esp_man_mionca = 0
            t_fin_cargan_vehic_cont = 0
            rnd_carga = 0
            rnd_llegada_auto_cont = 0
            rnd_llegada_mionca_cont = 0


            if (len(tabla_dia) != 0) and reloj == 7:
                cola_autos = tabla_dia[dia-2].cola_esp_man_auto
                cola_mionca = tabla_dia[dia-2].cola_esp_man_mionca
                ##Prox Carga de vehículo:
                if cola_mionca > 0:
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca += 1
                    rnd_carga = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga, 0.05, 0.082)

                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)

                elif cola_autos > 0:
                    t1.estado = "Cargando"
                    t1.capacidad -= 1
                    t1.cola_autos += 1
                    rnd_carga = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga, 0.017, 0.049)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                else:
                    t1.estado = "Libre"
                    fin_cargan_vehic_cont = 999

            ############################################ Primer Omnibus ########################################

            if (reloj < 7.5) and min(fin_cargan_vehic_cont,prox_llegada_mionca_cont) == prox_llegada_mionca_cont:
                evento = "Llegada Camión/Omnibus al Continente"
                reloj = prox_llegada_mionca_cont
                rnd_llegada_mionca_cont = random.uniform(0,1)
                prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)

                if t1.estado == "Libre" :
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca+=1
                    rnd_carga = random.uniform(0,1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga,0.05,0.082)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga,0.05,0.082)
                else:
                    cola_mionca += 1




            #Primera llegada de un auto
            if (prox_llegada_mionca_cont >= 7.5) and (prox_llegada_auto_cont == 999) and len(tabla_dia)>2 :
                reloj = 7.5
                evento = "Llegada Auto Continente"
                rnd_llegada_auto_cont = random.uniform(0,1)
                prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.16,0.33)
                if t1.estado == "Libre":
                    t1.estado = "Cargando"
                    t1.capacidad -= 1
                    t1.cola_autos += 1
                    rnd_carga = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga, 0.017, 0.049)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                else:
                    cola_autos += 1

            if trans_en_uso == "T1" and t1.capacidad == 0:
                t1.hora_partida = reloj
            if trans_en_uso == "T2" and t1.capacidad == 0:
                t2.hora_partida = reloj

            opcion = min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, t1.hora_partida,
                         t2.hora_partida,t1.hora_llegada,t2.hora_llegada, hora_descarga_t1, hora_descarga_t2,20)

            ###########################################Curso normal##################################################
            if opcion == t1.hora_llegada:
                evento = "Llegada T1 a Continente"
                acum_auto += t1.cola_autos
                acum_mionca += t1.cola_mionca
                #Llegada de ferry al continente
                if t1.puerto_salida == "Isla":
                    reloj = t1.hora_llegada
                    hora_descarga_t1 = reloj
                    t1.estado = "Descargando"
                    t1.localizacion = "Continente"
                    for i in range(len(t1.cola_autos)):
                        hora_descarga_t1 += random.uniform(0.0077,0.024)
                    for i in range(len(t1.cola_mionca)):
                        hora_descarga_t1 += random.uniform(0.024,0.041)

                    if t2.localizacion != "Continente":
                        trans_en_uso = "T1"

                t1.hora_llegada = 999

            elif opcion == t2.hora_llegada:             #Llega t2 al contintente
                evento = "Llegada de T2 al continente"

                acum_auto += t2.cola_autos
                acum_mionca += t2.cola_mionca
                if t2.puerto_salida == "Isla":
                    reloj = t2.hora_llegada
                    hora_descarga_t2 = reloj
                    t2.estado = "Descargando"
                    t2.localizacion = "Continente"
                    for i in range(len(t2.cola_autos)):
                        hora_descarga_t2 += random.uniform(0.0077, 0.024)
                    for i in range(len(t2.cola_mionca)):
                        hora_descarga_t2 += random.uniform(0.024, 0.041)

                    if t1.localizacion != "Continente":
                        trans_en_uso = "T2"
                t2.hora_llegada = 999

            elif opcion == hora_descarga_t1:            #Descarga T1
                evento = "Fin de descarga T1 en Contintente"
                t1.cola_autos = 0
                t1.cola_mionca = 0
                t1.capacidad = 10
                if t1.localizacion == "Continente" and trans_en_uso == "T1":
                    if cola_mionca > 0:
                        t1.estado = "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont= funcion_uniforme(rnd_carga, 0.05, 0.082)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)

                    elif cola_autos > 0:
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos +=1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga, 0.017, 0.049)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    else:
                        t1.estado = "Libre"
                        fin_cargan_vehic_cont = 999

            elif opcion == hora_descarga_t2: #Descarga T2
                evento = "Fin de descarga T2 en Continente"
                t2.cola_autos = 0
                t2.cola_mionca = 0
                t2.capacidad = 20

                if t2.localizacion == "Continente" and trans_en_uso == "T2":
                    if cola_mionca > 0:
                        t2.estado = "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont = funcion_uniforme(rnd_carga, 0.017, 0.049)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                    elif cola_autos > 0:
                        t2.estado = "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont =  funcion_uniforme(rnd_carga, 0.017, 0.049)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    else:
                        t2.estado = "Libre"
                        fin_cargan_vehic_cont = 999

            elif opcion == fin_cargan_vehic_cont:
                #Fin Carga de Vehículo

                reloj = fin_cargan_vehic_cont
                if trans_en_uso == "T1" and t1.capacidad == 0:
                    t1.estado = "Libre"
                    t1.hora_partida = fin_cargan_vehic_cont +0.01
                if trans_en_uso == "T2" and t2.capacidad == 0:
                    t2.estado = "Libre"
                    t2.hora_partida = fin_cargan_vehic_cont + 0.01
                if t1.estado == "Cargando" and t1.localizacion == "Continente" and cola_autos == 0 and cola_mionca == 0:
                    t1.estado == "Libre"
                    fin_cargan_vehic_cont = 999
                elif t2.estado == "Cargando" and t2.localizacion == "Continente" and cola_autos == 0 and cola_mionca == 0:
                    t2.estado == "Libre"
                    fin_cargan_vehic_cont = 999

                else:
                    if trans_en_uso == "T1" and cola_mionca != 0 and t1.capacidad > 2:
                        # Cargo un camión
                        evento = "Fin de Carga Camión Continente"
                        t1.estado == "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont =  funcion_uniforme(rnd_carga, 0.05, 0.082)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)

                    elif trans_en_uso == "T1" and cola_autos != 0 and t1.capacidad > 1:
                        #Cargar un auto
                        evento = "Fin de Carga Auto Continente"
                        t1.estado == "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont =  funcion_uniforme(rnd_carga, 0.017, 0.049)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                    elif trans_en_uso == "T2" and cola_mionca != 0 and t2.capacidad > 2:
                        # Cargo un camión
                        evento = "Fin de Carga Camión Continente"
                        t2.estado == "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont =  funcion_uniforme(rnd_carga, 0.05,0.082)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05,0.082)

                    elif trans_en_uso == "T2" and cola_autos != 0 and t2.capacidad > 1:
                        # Cargar un auto
                        evento = "Fin de Carga Auto Continente"
                        t2.estado == "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        t_fin_cargan_vehic_cont =  funcion_uniforme(rnd_carga, 0.017, 0.049)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    else:
                        fin_cargan_vehic_cont = 999


            elif opcion == prox_llegada_auto_cont:
                ## Llega un auto
                evento = "Llegada de Auto a Continente"
                reloj = prox_llegada_auto_cont
                if reloj <=12 and siguen_llegando_autos:
                    rnd_llegada_auto_cont = random.uniform(0,1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.167,0.33)
                elif reloj <=19 and siguen_llegando_autos:
                    rnd_llegada_auto_cont = random.uniform(0, 1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont, 0.417, 0.583)
                else:
                    siguen_llegando_autos = False
                    prox_llegada_auto_cont = 9999
                ##

                if (t1.localizacion != "Continente" and t2.localizacion != "Continente") or (t1.localizacion == "Continente" and t1.estado == "Cargando" )\
                        or(t2.localizacion == "Continente" and t2.estado == "Cargando" ) \
                        or (trans_en_uso == "T1" and t1.capacidad < 1) \
                        or (trans_en_uso == "T2" and t2.capacidad < 1):
                    cola_autos += 1
                else:
                    if (trans_en_uso == "T1") and t1.estado == "Libre" :
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                    elif trans_en_uso == "T2" and t2.estado == "Libre":
                        t2.estado = "Cargando"
                        t2.capacidad -=1
                        t2.cola_autos += 1

                    rnd_carga = random.uniform(0, 1)
                    t_fin_cargan_vehic_cont = + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                    try:
                        if (tabla_dia[dia-2].cola_max_auto_cont)<cola_autos:
                            cola_max_auto = cola_mionca
                        else:
                            cola_max_auto = tabla_dia[dia-2].cola_max_auto_cont
                    except:
                        cola_max_auto = cola_autos

            elif opcion == prox_llegada_mionca_cont:
                ## Llega un camion
                evento = "Llegada de Camión/Ómnibus a Continente"
                reloj = prox_llegada_mionca_cont
                if reloj <= 12 and siguen_llegando_mionca:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.314, 0.346)
                elif reloj <= 19.5 and siguen_llegando_mionca:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 1.917, 2.083)
                else:
                    siguen_llegando_mionca = False
                    prox_llegada_mionca_cont = 9999

                if (t1.localizacion != "Continente" and t2.localizacion != "Continente") or (
                        t1.localizacion == "Continente" and t1.estado == "Cargando") \
                        or (t2.localizacion == "Continente" and t2.estado == "Cargando") \
                        or(trans_en_uso == "T1" and t1.capacidad<2)\
                        or(trans_en_uso == "T2" and t2.capacidad<2):
                    cola_mionca += 1

                else:
                    if (trans_en_uso == "T1"):
                        t1.estado = "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                    else:
                        t2.estado = "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca+=1
                    rnd_carga = random.uniform(0, 1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)
                    try:
                        if (tabla_dia[dia-2].cola_max_mionca_cont)<cola_mionca:
                            cola_max_mionca = cola_mionca
                        else:
                            cola_max_mionca = tabla_dia[dia-2].cola_max_mionca_cont
                    except:
                        cola_max_mionca = cola_mionca

            elif opcion == t1.hora_partida:
                #Revisar desde donde sale y liberar el T

                if t1.estado == "Cargando":
                    t1.hora_partida = fin_cargan_vehic_cont + 0.001
                if t1.localizacion == "Continente":
                    evento = "Salida T1 Cont-Isla"
                    if t2.localizacion == "Continente":
                        trans_en_uso = "T2"
                    else:
                        trans_en_uso = "T3"
                    t1.hora_llegada = random.uniform(0.917,1.084)
                    t1.puerto_salida = t1.localizacion
                    t1.localizacion = "Mar"
                t1.hora_partida = 999

            elif opcion == t2.hora_partida:
                if t2.estado == "Cargando":
                    t2.hora_partida = fin_cargan_vehic_cont + 0.001
                if t2.localizacion == "Continente":
                    evento = "Salida T2 Cont-Isla"
                    if t1.localizacion == "Continente":
                        trans_en_uso = "T1"
                    else:
                        trans_en_uso = "T3"
                    t2.hora_llegada = random.uniform(0.917, 1.084)
                    t2.puerto_salida = t2.localizacion
                    t2.localizacion = "Mar"
                t2.hora_partida = 999

            elif opcion == 20:
                evento = "Fin de Día"
                dia += 1
                reloj = 20

                cola_esp_man_auto = cola_autos
                cola_esp_man_mionca = cola_max_mionca


            try:
                cola_esp_man_auto_acum = tabla_dia[-1].cola_esp_man_auto_acum + cola_esp_man_auto
                cola_esp_man_mionca_acum = tabla_dia[-1].cola_esp_man_mionca_acum + cola_esp_man_mionca
            except:
                cola_esp_man_auto_acum = cola_esp_man_auto
                cola_esp_man_mionca_acum = cola_esp_man_mionca



            entrada = Entrada_prueba(evento, dia, reloj,
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
            rnd_carga, t_fin_cargan_vehic_cont, fin_cargan_vehic_cont, t1, t2, acum_auto, acum_mionca,
            acum_auto/dia, acum_mionca/dia)
            tabla_dia.append(entrada)
            print(entrada.toString())


generar_miles(2)
