from pickle import APPEND

from Veiculos import *

class Sistema():
    def __init__(self):
        self.__alugados = []
        self.__n_alugados = []

    def create_carro(self, placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas):
        return self.__n_alugados.append(placa, modelo, marca, ano_fabricao, cor, tanque, versao, tp_combustivel, tipo_carro, quant_portas)

    def create_moto(self, placa, modelo, marca, ano_fabricao, cor, tanque, cilindrada, tipo_partida, categoria, tipo_moto):
        return self.__n_alugados.append(placa, modelo, marca, ano_fabricao, cor, tanque, cilindrada, tipo_partida, categoria, tipo_moto)

    