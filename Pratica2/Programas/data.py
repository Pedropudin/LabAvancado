from scipy import constants, stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ExperimentLight():
    def __init__(self, nomeArquivo, comprimento:float) -> None:
        self.l = comprimento
        self.f = constants.c/comprimento
        self.data = pd.read_csv("Dados/" + nomeArquivo)
        self.tensao = self.data["tensao"].to_numpy()
        self.corrente = self.data["corrente"].to_numpy()

        return

    def getFrequencia(self):
        return self.f
    
    def getTensao(self):
        return self.tensao
    
    def getCorrente(self):
        return self.corrente
    
    def getComprimento(self):
        return self.l
    
    def getData(self):
        return self.data
    
    def getPotencialParada(self):
        return self.tensao[0]
    
    def getEnergiaMaxima(self):
        return self.getPotencialParada() * constants.e * -1
    
    def plotCorrenteTensao(self):
        fig, ax = plt.subplots()

        ax.plot(self.tensao,self.corrente,'o')
        ax.set_title("Corrente fotoelétrica em função do Potencial") # talvez meio grande
        ax.set_xlabel("Potencial (V)")
        ax.set_ylabel("Corrente (A.10^(-11))") # escrever isso melhor
        plt.show()
        return
    
    def plotPotencialParada(self, nPontos: int):
        fig = plt.subplot()
        x = self.tensao[0:nPontos]
        y = self.corrente[0:nPontos]
        y[0] += 1e-13
        fig.plot(x, y,'o')
        fig.set_yscale("log")

        plt.show()

class ExperimentFinal():
    def __init__(self,lampadaMercurio:list[ExperimentLight], led:list[ExperimentLight]) -> None:
        self.lampada = lampadaMercurio
        self.led = led

    def getPotencialParada_lampada(self):
        V0 = np.empty(len(self.lampada))

        for i in range(len(self.lampada)):
            V0[i] = self.lampada[i].getPotencialParada()
        
        return V0
    
    def getPotencialParada_led(self):
        V0 = np.empty(len(self.led))

        for i in range(len(self.led)):
            V0[i] = self.led[i].getPotencialParada()
        
        return V0

    def getFrequencia_lampada(self):
        f = np.empty((len(self.lampada)))

        for i in range(len(self.lampada)):
            f[i] = self.lampada[i].getFrequencia()
        
        return f

    def getFrequencia_led(self):
        f = np.empty(len(self.led))

        for i in range(len(self.led)):
            f[i] = self.led[i].getFrequencia()
        
        return f
    
    def plotPlanck_lampada(self):
        freq = self.getFrequencia_lampada()
        V0 = self.getPotencialParada_lampada()

        fig, ax =   plt.subplots()

        ax.plot(freq,V0, "o")
        plt.savefig("planckLampada.png")

    def plotPlanck_led(self):
        freq = self.getFrequencia_led()
        V0 = self.getPotencialParada_led()

        fig, ax =   plt.subplots()

        ax.plot(freq,V0, "o")
        plt.savefig("planckLed.png")

amarelo = ExperimentLight("correnteTensao-Amarelo.csv", 600e-9)
verde = ExperimentLight("correnteTensao-Verde.csv", 546e-9)
azulClaro = ExperimentLight("correnteTensao-AzulClaro.csv", 503e-9)
roxo = ExperimentLight("correnteTensao-Roxo.csv",445e-9)
violeta = ExperimentLight("correnteTensao-Violeta.csv",412e-9)

exp = ExperimentFinal([azulClaro,verde,amarelo,roxo,violeta],[])
