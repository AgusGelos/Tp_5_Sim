class Transbordador:
    def __init__(self, cola_autos, cola_mionca , capacidad,hora_partida,estado,localizacion,mantenimiento, hora_llegada, salio_de):
        self.cola_autos = cola_autos
        self.cola_mionca = cola_mionca
        self.capacidad = capacidad
        self.hora_partida = hora_partida
        self.estado = estado
        self.localizacion = localizacion
        self.mantenimiento = mantenimiento
        self.hora_llegada = hora_llegada
        self.puerto_salida = salio_de
        self.hora_partida_lequeda = 0
        self.hora_llegada_lequeda = 0

    def set_estado(self, estado):
        self.estado = estado
