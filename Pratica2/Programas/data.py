from scipy import constants, stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt

caminhoResultados = "Resultados/"

class ExperimentLight():
    def __init__(self, nomeArquivo, comprimento:float, color) -> None:
        self.l = comprimento
        self.f = constants.c/comprimento
        self.data = pd.read_csv("Dados/" + nomeArquivo)
        self.tensao = self.data["tensao"].to_numpy()
        self.corrente = self.data["corrente"].to_numpy()
        self.color = color

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
    
    def getVelocidadeMaxima(self):
        V0 = self.getPotencialParada()
        return mt.sqrt(abs(2 * constants.e * V0 / constants.m_e))
    
    def plotCorrenteTensao(self,emissor):
        fig, ax = plt.subplots()

        ax.plot(self.tensao,self.corrente,'o')
        ax.set_xlabel("Potencial (V)")
        ax.set_ylabel("Corrente (A)") # escrever isso melhor
        plt.savefig(caminhoResultados + f"{self.color}-{emissor}.png")
        return
    
    def plotPotencialParada(self, nPontos: int, emissor):
        fig = plt.subplot()
        x = self.tensao[0:nPontos]
        y = self.corrente[0:nPontos]
        y[0] += 1e-13
        fig.plot(x, y,'o')
        fig.set_yscale("log")

        plt.savefig(caminhoResultados + f"{self.color}-{emissor}.png")
        return 

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
    
    def getVelocidade_lampada(self):
        v = np.empty(len(self.lampada))

        for i in range(len(self.lampada)):
            v[i] = self.lampada[i].getVelocidadeMaxima()
        
        return v
    
    def getVelocidade_led(self):
        v = np.empty(len(self.led))

        for i in range(len(self.led)):
            v[i] = self.led[i].getVelocidadeMaxima()
        
        return v
    
    def plotPlanck_lampada(self):
        freq = self.getFrequencia_lampada()
        V0 = self.getPotencialParada_lampada()

        fig, ax =   plt.subplots()

        for light in self.lampada:
            ax.plot(light.getFrequencia(),light.getPotencialParada()*constants.e,"o",color=light.color,label=light.color)

        c_ang, c_lin, r, p, desvio = stats.linregress(freq,V0*constants.e)

        ax.plot([freq[0],freq[-1]],[c_lin+freq[0]*c_ang, c_lin+freq[-1]*c_ang])

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Energia ($V_0\cdot e$)")
        plt.savefig(caminhoResultados + "energia_Frequencia-lampada.png")
        return c_ang, c_lin, desvio

    def plotPlanck_led(self):
        freq = self.getFrequencia_led()
        V0 = self.getPotencialParada_led()

        fig, ax =   plt.subplots()

        for light in self.led:
            ax.plot(light.getFrequencia(),light.getPotencialParada()*constants.e,"o",color=light.color,label=light.color)

        c_ang, c_lin, r, p, desvio = stats.linregress(freq,V0*constants.e)

        ax.plot([freq[0],freq[-1]],[c_lin+freq[0]*c_ang, c_lin+freq[-1]*c_ang],label=f"{c_lin:.2e} + x*{c_ang:.2e}",color="black")

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Energia ($V_0\cdot e$)")
        plt.savefig(caminhoResultados + "energia_Frequencia-led.png")
        return c_ang, c_lin, desvio
    
    def plotVelocidade_lampada(self):
        fig, ax =   plt.subplots()

        for light in self.lampada:
            ax.plot(light.getFrequencia(),light.getVelocidadeMaxima(),"o",color=light.color,label=light.color)

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Velocidade Máxima")
        plt.savefig(caminhoResultados + "velocidade-lampada.png")
        return
    
    def plotVelocidade_led(self):
        fig, ax =   plt.subplots()

        for light in self.led:
            ax.plot(light.getFrequencia(),light.getVelocidadeMaxima(),"o",color=light.color,label=light.color)

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Velocidade Máxima")
        plt.savefig(caminhoResultados + "velocidade-led.png")
        return

amarelo = ExperimentLight("correnteTensao-Amarelo.csv", 600e-9, "yellow")
verde = ExperimentLight("correnteTensao-Verde.csv", 546e-9, "green")
azulClaro = ExperimentLight("correnteTensao-AzulClaro.csv", 503e-9, "lightblue")
roxo = ExperimentLight("correnteTensao-Roxo.csv",445e-9, "purple")
violeta = ExperimentLight("correnteTensao-Violeta.csv",412e-9, "violet")

led1 = ExperimentLight("led-1.csv", 500e-9, "black")
led2 = ExperimentLight("led-1.csv", 600e-9, "black")
led3 = ExperimentLight("led-1.csv", 700e-9, "black")

lampada = [amarelo, verde, azulClaro, roxo, violeta]
led = [led1, led2, led3]

exp = ExperimentFinal(lampada,led)