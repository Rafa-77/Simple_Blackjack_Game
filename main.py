from itertools import combinations
import pandas
import numpy
from collections import Counter


class probabilidades:
    def _init_(self):
        self.mano_final_jugador = []
        self.mano_final_dealer = []
        self.suma_mano_dealer = []
        self.suma_mano_jugador = []
        self.cards = []
        suits = ["♠", "♣️", "♥️", "♦️"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append((suit, rank))

        self.para_shuffle = self.cards[:]
        numpy.random.shuffle(self.para_shuffle)

        self.repartir_cartas_manos()

    def repartir_cartas_manos(self):
        manos = [[], []]
        for tarjeta in range(2):
            for n in manos:
                n.append(self.para_shuffle.pop())
        self.opciones_jugador(manos)

    def opciones_jugador(self, manos):
        mano_dealer = manos[-1]
        mano_jugador = manos[0]
        print("Mano del jugador", mano_jugador)
        print("Mano del dealer", mano_dealer)
        suma = 0
        has_ace = False
        for carta in mano_jugador:
            for value in carta:
                if type(value) == dict:
                    x = value.get("value")
                    suma += x
                    y = value.get("rank")
                    if y == "A":
                        has_ace = True
                else:
                    pass
        if suma > 21 and has_ace is True:
            suma -= 10
            if suma > 21:
                print("Tu mano suma: ", suma)
                print("Perdio el jugador")
            elif suma == 21:
                print("Tu mano suma: ", suma)
                print("Gano el jugador")
            elif suma < 21:
                print("Tu mano suma: ", suma)
                print("Jugador Puede continuar")
                self.suma_mano_jugador = suma
                self.continuar_jugador(manos)
        elif suma > 21 and has_ace is False:
            if suma > 21:
                print("Tu mano suma: ", suma)
                print("Perdio el jugador")
            elif suma == 21:
                print("Tu mano suma: ", suma)
                print("Gano el jugador")
            elif suma < 21:
                print("Tu mano suma: ", suma)
                print("Jugador puede continuar")
                self.suma_mano_jugador = suma
                self.continuar_jugador(manos)
        elif suma == 21:
            print("Tu mano suma: ", suma)
            print("Gano el jugador")
        elif suma < 21:
            print("Tu mano suma: ", suma)
            print("Jugador puede continuar")
            self.suma_mano_jugador = suma
            self.continuar_jugador(manos)

    def continuar_jugador(self, manos):
        print("\n")
        while True:
            x = input(
                "Presione 'P' para quedarse con su mano o 'H' para sacar nueva carta:  ")
            if x == "P":
                print("Jugador decide quedarse con esta mano: ", manos[0])
                print("\n")
                self.mano_final_jugador = manos[0]
                self.opciones_dealer(manos)
                break
            if x == "H":
                manos[0].append(self.para_shuffle.pop())
                self.opciones_jugador(manos)
                break
            else:
                print("Escoga un valor correcto")
                continue

    def opciones_dealer(self, manos):
        mano_dealer = manos[-1]
        mano_jugador = manos[0]
        suma = 0
        has_ace = False
        for carta in mano_dealer:
            for value in carta:
                if type(value) == dict:
                    x = value.get("value")
                    suma += x
                    y = value.get("rank")
                    if y == "A":
                        has_ace = True
                else:
                    pass
        if suma > 21 and has_ace is True:
            suma -= 10
            if suma > 21:
                print("Tu mano dealer suma: ", suma)
                print("Perdio el dealer")
            elif suma == 21:
                print("Tu mano dealer suma: ", suma)
                print("Gano el dealer")
            elif suma < 21:
                print("Tu mano dealer suma: ", suma)
                print("Dealer Puede continuar")
                self.suma_mano_dealer = suma
                self.combinaciones(manos)
        elif suma > 21 and has_ace is False:
            if suma > 21:
                print("Tu mano dealer suma: ", suma)
                print("Perdio el dealer")
            elif suma == 21:
                print("Tu mano dealer suma: ", suma)
                print("Gano el dealer")
            elif suma < 21:
                print("Tu mano dealer suma: ", suma)
                print("dealer puede continuar")
                self.suma_mano_dealer = suma
                self.combinaciones(manos)
        elif suma == 21:
            print("Tu mano dealer suma: ", suma)
            print("Gano el dealer")
        elif suma < 21:
            print("Tu mano dealer suma: ", suma)
            print("dealer  puede continuar")
            self.suma_mano_dealer = suma
            self.combinaciones(manos)

    def combinaciones(self, manos_de_jugadores):
        mano_dealer = manos_de_jugadores[-1]
        mano_jugador = manos_de_jugadores[0]

        numero_de_cartas_en_mano = 0
        for tarjeta in manos_de_jugadores[-1]:
            numero_de_cartas_en_mano += 1
        lista = list(combinations(self.cards, numero_de_cartas_en_mano + 1))

        posibles_manos = []
        for combinacion in lista:
            check = all(items in combinacion for items in mano_dealer)
            if check is True:
                posibles_manos.append(combinacion)

        posibles_manos_final = posibles_manos[:]
        for posible in posibles_manos:
            check2 = any(items in posible for items in mano_jugador)
            if check2 is True:
                posibles_manos_final.remove(posible)

        no_de_posibles_manos_final = len(posibles_manos_final)
        self.valor_combinaciones(posibles_manos_final, manos_de_jugadores)

    def valor_combinaciones(self, lista_para_sacar_valores, manos):
        valores = []
        for mano in lista_para_sacar_valores:
            d = dict()
            suma = 0
            has_ace = False
            for carta in mano:
                for second in carta:
                    if type(second) == dict:
                        x = second.get("value")
                        suma += x
                        y = second.get("rank")
                        if y == "A":
                            has_ace = True
                    else:
                        pass
            d.update({"Suma": suma})
            d.update({"Has ace": has_ace})
            valores.append(d)
        self.valores_de_21(valores, manos)

    def valores_de_21(self, valores_lista, manos):
        valores_mayores = 0
        valores_exactos = 0
        valores_menores = 0
        for cuadro in valores_lista:
            suma = cuadro.get("Suma")
            ace = cuadro.get("Has ace")
            if suma > 21 and ace is True:
                suma -= 10
                if suma > 21:
                    valores_mayores += 1
                elif suma == 21:
                    valores_exactos += 1
                elif suma < 21:
                    valores_menores += 1
            elif suma > 21 and ace is False:
                if suma > 21:
                    valores_mayores += 1
                elif suma == 21:
                    valores_exactos += 1
                elif suma < 21:
                    valores_menores += 1
            elif suma == 21:
                valores_exactos += 1
            elif suma < 21:
                valores_menores += 1

        cien = len(valores_lista)
        exactos_porcentaje = (valores_exactos/cien)
        mayores_porcentaje = (valores_mayores/cien)
        menores_porcentaje = (valores_menores/cien)
        # print("""
        # Probabilidad de obtener con su proxima carta un valor (dealer):
        # Mayor a 21: {}%
        # Exacto a 21: {}%
        # Menor a 21: {}%
        # """.format(mayores_porcentaje*100, exactos_porcentaje*100, menores_porcentaje*100))

        self.porcentajes(mayores_porcentaje,
                         exactos_porcentaje, menores_porcentaje, manos)

    def porcentajes(self, mayor, exacto, menor, manos):
        if (mayor) > 0.65:
            print("Dealer decide no ir a siguiente ronda")
            self.mano_final_dealer = manos[-1]
            self.determinar_ganador()
        else:
            print("Dealer decide tomar una carta")
            manos[-1].append(self.para_shuffle.pop())
            print("Mano del dealer: ", manos[-1])
            self.opciones_dealer(manos)

    def determinar_ganador(self):
        print("\n")
        print("Mano final del dealer: ", self.mano_final_dealer)
        print("Con una suma de: ", self.suma_mano_dealer)

        print("Mano final del jugador: ", self.mano_final_jugador)
        print("Con una suma de: ", self.suma_mano_jugador)

        if self.suma_mano_dealer == self.suma_mano_jugador:
            print("EMPATE")
        elif self.suma_mano_dealer < self.suma_mano_jugador:
            print("Ganó el jugador")
        elif self.suma_mano_dealer > self.suma_mano_jugador:
            print("Gano el dealer")


x = probabilidades()
x._init_()
