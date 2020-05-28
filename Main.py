import math
import random

from Class.Entrada_class import Entrada
from Class.Trans_Class import Transbordador




def funcion_uniforme(rnd,lim_inf, lim_sup):
    return lim_inf + rnd*(lim_sup-lim_inf)

def generar_miles(cantidad_dias):
    entrada = Entrada()
    entrada.cola_esp_man_auto = 0
    entrada.cola_esp_man_mionca = 0
    tabla_dia = []
    tabla_completa = [[]]

    t1 = Transbordador(0,0,10, 9, "Esperando", "Continente", 5)
    t2 = Transbordador(0,0,20, 10, "Esperando", "Continente", 10)
    for i in range(cantidad_dias):
        ############# Parámetros de entrada
        reloj = 7
        prox_llegada_auto_cont = 0
        rnd_llegada_mionca_cont = random.uniform(0, 1)
        prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)
        trans_en_uso = "T1"
        hora_descarga_t1, hora_descarga_t2 = 0,0
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
            t1.estado = "Esperando"
            t1.localizacion = "Continente"
            t1.hora_partida = 9
            t2.estado = "Esperando"
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


        while reloj < 20:

            ##Verificar la cola del dia anterior

            if reloj < 7.5:
                reloj = prox_llegada_mionca_cont
                rnd_llegada_mionca_cont = random.uniform(0,1)
                prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)


                if t1.estado == "Esperando" :
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca+=1
                    rnd_carga = random.uniform(0,1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga,0.05,0.082)
                else:
                    cola_mionca += 1

                ##Hay Posibilidad que este cargando un camión y llegue otro? de 7 - 7.30


            #Primera llegada de un auto
            if prox_llegada_mionca_cont >= 7.5 & prox_llegada_auto_cont == 0:
                reloj = 7.5
                rnd_llegada_auto_cont = random.uniform(0,1)
                prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.16,0.33)
                if t1.estado == "Libre":
                    t1.estado = "Cargando"
                    t1.capacidad -= 1
                    t1.cola_autos += 1
                    rnd_carga = random.uniform(0, 1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                else:
                    cola_autos += 1

            if trans_en_uso == "T1" & t1.capacidad == 0:
                t1.hora_partida = reloj
            if trans_en_uso == "T2" & t1.capacidad == 0:
                t2.hora_partida = reloj

            opcion = min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, t1.hora_partida,
                         t2.hora_partida,t1.hora_llegada,t2.hora_llegada, hora_descarga_t1, hora_descarga_t2)

            #Curso normal
            if opcion == t1.hora_llegada:
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

            elif opcion == t2.hora_llegada:             #Llega t2 al contintente

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

            elif opcion == hora_descarga_t1:            #Descarga T1
                t1.cola_autos = 0
                t1.cola_mionca = 0
                t1.capacidad = 10
                if t1.localizacion == "Continente" & trans_en_uso == "T1":
                    acum_auto += t1.cola_autos
                    acum_mionca += t2.cola_mionca
                    if cola_autos > 0:
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos +=1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    elif cola_mionca > 0:
                        t1.estado = "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)
                    else:
                        t1.estado = "Libre"

            elif opcion == hora_descarga_t2:                            #Descarga T2
                if t2.localizacion == "Continente" & trans_en_uso == "T2":
                    acum_auto += t1.cola_autos
                    acum_mionca += t2.cola_mionca
                    if cola_autos > 0:
                        t2.estado = "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    elif cola_mionca > 0:
                        t2.estado = "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    else:
                        t2.estado = "Libre"

            elif opcion == fin_cargan_vehic_cont:
                #Fin Carga de Vehículo

                reloj = fin_cargan_vehic_cont
                if trans_en_uso == "T1" & t1.capacidad == 0:
                    t1.estado = "Libre"
                    t1.hora_partida = fin_cargan_vehic_cont +0.01
                if trans_en_uso == "T2" & t2.capacidad == 0:
                    t2.estado = "Libre"
                    t2.hora_partida = fin_cargan_vehic_cont + 0.01
                if t1.estado == "Cargando" & t1.localizacion == "Continente" & cola_autos == 0 & cola_mionca == 0:
                    t1.estado == "Libre"
                elif t2.estado == "Cargando" & t2.localizacion == "Continente" & cola_autos == 0 & cola_mionca == 0:
                    t2.estado == "Libre"

                else:
                    if trans_en_uso == "T1" & cola_mionca != 0 & t1.capacidad > 2:
                        # Cargo un camión
                        t1.estado == "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05, 0.082)

                    elif trans_en_uso == "T1" & cola_autos != 0 & t1.capacidad > 1:
                        #Cargar un auto
                        t1.estado == "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                    elif trans_en_uso == "T2" & cola_mionca != 0 & t2.capacidad > 2:
                        # Cargo un camión
                        t2.estado == "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.05,0.082)

                    elif trans_en_uso == "T2" & cola_autos != 0 & t2.capacidad > 1:
                        # Cargar un auto
                        t2.estado == "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

            elif opcion == prox_llegada_auto_cont:
                ## Llega un auto
                reloj = prox_llegada_auto_cont
                if reloj <=12:
                    rnd_llegada_auto_cont = random.uniform(0,1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.167,0.33)
                else:
                    rnd_llegada_auto_cont = random.uniform(0, 1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont, 0.417, 0.583)

                ##

                if (t1.localizacion != "Continente" & t2.localizacion != "Continente") | (t1.localizacion == "Continente" & t1.estado == "Cargando" )\
                        |(t2.localizacion == "Continente" & t2.estado == "Cargando" ) \
                        | (trans_en_uso == "T1" & t1.capacidad < 1) \
                        | (trans_en_uso == "T2" & t2.capacidad < 1):
                    cola_autos += 1
                else:
                    if (trans_en_uso == "T1") & t1.estado == "Libre" :
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                    elif trans_en_uso == "T2" & t2.estado == "Libre":
                        t2.estado = "Cargando"
                        t2.capacidad -=1
                        t2.cola_autos += 1

                    rnd_carga = random.uniform(0, 1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)



            elif opcion == prox_llegada_mionca_cont:
                ## Llega un camion
                reloj = prox_llegada_mionca_cont
                if reloj <= 12:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.314, 0.346)
                else:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 1.917, 2.083)

                if (t1.localizacion != "Continente" & t2.localizacion != "Continente") | (
                        t1.localizacion == "Continente" & t1.estado == "Cargando") \
                        | (t2.localizacion == "Continente" & t2.estado == "Cargando") \
                        |(trans_en_uso == "T1" & t1.capacidad<2)\
                        |(trans_en_uso == "T2" & t2.capacidad<2):
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



            elif opcion == t1.hora_partida:
                #Revisar desde donde sale y liberar el T
                if t1.estado == "Cargando":
                    t1.hora_partida = fin_cargan_vehic_cont + 0.001
                if t1.localizacion == "Continente":
                    if t2.localizacion == "Continente":
                        trans_en_uso = "T2"
                    else:
                        trans_en_uso = "T3"
                    t1.hora_llegada = random.uniform(0.917,1.084)
                    t1.puerto_salida = t1.localizacion
                    t1.localizacion = "Mar"

            elif opcion == t2.hora_partida:
                if t2.estado == "Cargando":
                    t2.hora_partida = fin_cargan_vehic_cont + 0.001
                if t2.localizacion == "Continente":
                    if t1.localizacion == "Continente":
                        trans_en_uso = "T1"
                    else:
                        trans_en_uso = "T3"
                    t2.hora_llegada = random.uniform(0.917, 1.084)
                    t2.puerto_salida = t2.localizacion
                    t2.localizacion = "Mar"

