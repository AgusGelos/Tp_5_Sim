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
        #Establecer estados de Trans a valores iniciales o mantenimiento
        if i == t1.mantenimiento:
            t1.estado = "Mantenimiento"
            t1.mantenimiento += 10
        elif i == t2.mantenimiento:
            t2.estado = "Mantenimiento"
            t2.mantenimiento += 10
        else:
            t1.estado = "Esperando"
            t1.localizacion = "Continente"
            t1.hora_partida = 9
            t2.estado = "Esperando"
            t2.localizacion = "Continente"
            t2.hora_partida = 10

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
            if reloj < 7.5:
                reloj = prox_llegada_mionca_cont
                rnd_llegada_mionca_cont = random.uniform(0,1)
                prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 0.28, 0.38)


                if t1.estado == "Esperando" :
                    t1.estado = "Cargando"
                    t1.capacidad -= 2
                    t1.cola_mionca+=1
                    rnd_carga = random.uniform(0,1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga,0.0654,0.676)

                ##Hay Posibilidad que este cargando un camión y llegue otro? de 7 - 7.30


             ## Perído de 7.30 a 11.30

            #Primera llegada de un auto
            if prox_llegada_mionca_cont >= 7.5 & prox_llegada_auto_cont == 0:
                reloj = 7.5
                rnd_llegada_auto_cont = random.uniform(0,1)
                prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,0.22,0.28)
                if t1.estado == "Libre":
                    t1.estado = "Cargando"
                    t1.capacidad -= 1
                    t1.cola_autos += 1
                    rnd_carga = random.uniform(0, 1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

            if trans_en_uso == "T1" & t1.capacidad == 0:
                t1.hora_partida = reloj
            if trans_en_uso == "T2" & t1.capacidad == 0:
                t2.hora_partida = reloj
            #Curso normal
            if min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, t1.hora_partida, t2.hora_partida,t1.hora_llegada,t2.hora_llegada) == t1.hora_llegada:
                #Llegada de ferry
                if t1.puerto_salida == "Isla":
                    #Como no puedo sunir y bajar autos, voy a bajar primero a todos y recien ahí empiezo a cargar.
                    pass

            elif min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont) == fin_cargan_vehic_cont:
                if t1.estado == "Cargando" & t1.localizacion == "Continente" & cola_autos == 0 & cola_mionca == 0:
                    t1.estado == "Libre"
                elif t2.estado == "Cargando" & t2.localizacion == "Continente" & cola_autos == 0 & cola_mionca == 0:
                    t2.estado == "Libre"
                else:
                    if trans_en_uso == "T1" & cola_autos != 0:
                        #Cargar un auto
                        t1.estado == "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)
                    elif trans_en_uso == "T1" & cola_mionca!= 0:
                        #Cargo un camión
                        t1.estado == "Cargando"
                        t1.capacidad -= 2
                        t1.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 1,2)
                    elif trans_en_uso == "T2" & cola_autos != 0:
                        # Cargar un auto
                        t2.estado == "Cargando"
                        t2.capacidad -= 1
                        t2.cola_autos += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                    elif trans_en_uso == "T2" & cola_mionca != 0:
                        # Cargo un camión
                        t2.estado == "Cargando"
                        t2.capacidad -= 2
                        t2.cola_mionca += 1
                        rnd_carga = random.uniform(0, 1)
                        fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 1,2)



            elif min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, t1.hora_partida, t2.hora_partida) == prox_llegada_auto_cont:
                ## Llega un auto
                reloj = prox_llegada_auto_cont
                if reloj <=12:
                    rnd_llegada_auto_cont = random.uniform(0,1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont,2.5,0.83)
                else:
                    rnd_llegada_auto_cont = random.uniform(0, 1)
                    prox_llegada_auto_cont = reloj + funcion_uniforme(rnd_llegada_auto_cont, 5, 0.83)
                if (t1.localizacion != "Continente" & t2.localizacion != "Continente") | (t1.localizacion == "Continente" & t1.estado == "Cargando" )\
                        |(t2.localizacion == "Continente" & t2.estado == "Cargando" ) \
                        | (trans_en_uso == "T1" & t1.capacidad < 1) \
                        | (trans_en_uso == "T2" & t2.capacidad < 1):
                    cola_autos += 1
                else:
                    if (trans_en_uso == "T1") :
                        t1.estado = "Cargando"
                        t1.capacidad -= 1
                        t1.cola_autos += 1
                    elif trans_en_uso == "T2" :
                        t2.estado = "Cargando"
                        t2.capacidad -=1
                        t2.cola_autos += 1

                    rnd_carga = random.uniform(0, 1)
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                acum_auto +=1

            elif min(prox_llegada_auto_cont,prox_llegada_mionca_cont,fin_cargan_vehic_cont, t1.hora_partida, t2.hora_partida) == prox_llegada_mionca_cont:
                ## Llega un camion
                reloj = prox_llegada_mionca_cont
                if reloj <= 12:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 2.5, 0.83)
                else:
                    rnd_llegada_mionca_cont = random.uniform(0, 1)
                    prox_llegada_mionca_cont = reloj + funcion_uniforme(rnd_llegada_mionca_cont, 5, 0.83)

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
                    fin_cargan_vehic_cont = reloj + funcion_uniforme(rnd_carga, 0.017, 0.049)

                acum_mionca += 1
            else:
                if trans_en_uso == "T1":
                    if t1.estado == "Cargando":
                        t1.hora_partida = fin_cargan_vehic_cont + 0.01
                    else:
                        if t2.localizacion == t1.localizacion:
                            trans_en_uso = "T2"
                            t1.estado = "Viajando"
                            t1.puerto_salida = t1.localizacion
                            t1.localizacion = "Mar"
                            t1.hora_llegada = reloj + random.uniform(0.95,1.05)
                        else:
                            trans_en_uso = "Esperando"
                            t1.estado = "Viajando"
                            t1.puerto_salida = t1.localizacion
                            t1.localizacion = "Mar"
                            t1.hora_llegada = reloj + random.uniform(0.95, 1.05)
                elif trans_en_uso == "T2":
                    if t2.estado == "Cargando":
                        t2.hora_partida = fin_cargan_vehic_cont + 0.01
                    else:
                        if t2.localizacion == t1.localizacion:
                            trans_en_uso = "T1"
                            t2.puerto_salida = t2.localizacion
                            t2.estado = "Viajando"
                            t2.localizacion = "Mar"
                            t2.hora_llegada = reloj + random.uniform(0.95, 1.05)
                        else:
                            trans_en_uso = "Esperando"
                            t2.estado = "Viajando"
                            t2.puerto_salida = t2.localizacion
                            t2.localizacion = "Mar"
                            t2.hora_llegada = reloj + random.uniform(0.95, 1.05)


