from scipy import constants, stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt

caminhoResultados = "Resultados/"

def getCompLed(file):

    with open(file, "r") as f:
        for i in range(17):
            f.readline()
        data = f.readlines()
        
        comprimento = np.empty(len(data)-2)
        intensity = np.empty(len(data)-2)

        for i in range(len(data)-2):
            d = data[i].split("\t")

            comprimento[i] = float(d[0].replace(",","."))
            intensity[i] = float(d[1].replace(",","."))
        
        f.close()

    return comprimento, intensity

class ExperimentLight():
    def __init__(self, nomeArquivo, comprimento:float, color, intensity = 1) -> None:
        self.l = comprimento
        self.f = constants.c/comprimento
        self.I = intensity
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
        return abs(self.tensao[0])
    
    def getEnergiaMaxima(self):
        return self.getPotencialParada() * constants.e * -1
    
    def getVelocidadeMaxima(self):
        V0 = self.getPotencialParada()
        return mt.sqrt(abs(2 * constants.e * V0 / constants.m_e))
    
    def getNumPhoton(self):
        return self.I/(constants.h * self.f)
    
    def getEficiencia(self):
        return max(self.corrente)/(constants.e * self.getNumPhoton())
    
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
    
    def plotCorrenteTensaoTodos(self):
        fig, ax = plt.subplots()
        i = 0
        j = 0

        for light in self.lampada:
            ax.plot(light.getTensao(), light.getCorrente(), "o", color = light.color)
            i += 1
            if(i >= 3):
                i = 0
                ax.set_xlabel("Potencial (V)")
                ax.set_ylabel("Corrente (A)")
                plt.savefig(caminhoResultados + f"lampada-{j}.png")
                j += 1
                plt.close()
                fig, ax = plt.subplots()
        ax.set_xlabel("Potencial (V)")
        ax.set_ylabel("Corrente (A)")
        plt.savefig(caminhoResultados + f"lampada-{j}.png")

        i = 0
        j = 0
        
        fig, ax = plt.subplots()

        for light in self.led:
            ax.plot(light.getTensao(), light.getCorrente(), "o", color = light.color)
            i += 1
            if(i >= 3):
                i = 0
                ax.set_xlabel("Potencial (V)")
                ax.set_ylabel("Corrente (A)")
                plt.savefig(caminhoResultados + f"led-{j}.png")
                j += 1
                plt.close()
                fig, ax = plt.subplots()
        ax.set_xlabel("Potencial (V)")
        ax.set_ylabel("Corrente (A)")
        plt.savefig(caminhoResultados + f"led-{j}.png")
        
    
    def plotPlanck_lampada(self):
        freq = self.getFrequencia_lampada()
        V0 = self.getPotencialParada_lampada()

        fig, ax =   plt.subplots()

        for light in self.lampada:
            ax.plot(light.getFrequencia(),light.getPotencialParada()*constants.e,"o",color=light.color,label=light.color)

        c_ang, c_lin, r, p, desvio = stats.linregress(freq,V0*constants.e)

        ax.plot([min(freq),max(freq)],[c_lin+min(freq)*c_ang, c_lin+max(freq)*c_ang])

        ax.set_xlabel("Frequência (Hz)")
        ax.set_ylabel("Energia ($V_0\cdot e$)")
        plt.savefig(caminhoResultados + "energia_Frequencia-lampada.png")
        return c_ang, abs(c_lin), desvio

    def plotPlanck_led(self):
        freq = self.getFrequencia_led()
        V0 = self.getPotencialParada_led()

        fig, ax =   plt.subplots()

        for light in self.led:
            ax.plot(light.getFrequencia(),light.getPotencialParada()*constants.e,"o",color=light.color,label=light.color)

        c_ang, c_lin, r, p, desvio = stats.linregress(freq,V0*constants.e)

        ax.plot([min(freq),max(freq)],[c_lin+min(freq)*c_ang, c_lin+max(freq)*c_ang],label=f"{c_lin:.2e} + x*{c_ang:.2e}",color="black")

        ax.set_xlabel("Frequência (Hz)")
        ax.set_ylabel("Energia ($V_0\cdot e$)")
        plt.savefig(caminhoResultados + "energia_Frequencia-led.png")
        return c_ang, abs(c_lin), desvio
    
    def plotVelocidade_lampada(self):
        fig, ax =   plt.subplots()

        for light in self.lampada:
            # print(f"{light.getFrequencia():.3e} & {light.getVelocidadeMaxima():.3e} \\\\")
            ax.plot(light.getFrequencia(),light.getVelocidadeMaxima(),"o",color=light.color,label=light.color)

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Velocidade Máxima")
        plt.savefig(caminhoResultados + "velocidade-lampada.png")
        return
    
    def plotVelocidade_led(self):
        fig, ax =   plt.subplots()

        for light in self.led:
            # print(f"{light.getFrequencia():.3e} & {light.getVelocidadeMaxima():.3e} \\\\")
            ax.plot(light.getFrequencia(),light.getVelocidadeMaxima(),"o",color=light.color,label=light.color)

        ax.set_xlabel("Frequência (m)")
        ax.set_ylabel("Velocidade Máxima")
        plt.savefig(caminhoResultados + "velocidade-led.png")
        return

    def plotEficienty(self):
        x = []
        y = []

        fig, ax = plt.subplots()

        for i in range(len(self.led)):
            if(self.led[i].color == "green" or self.led[i].color == "blue"):
                continue
            ax.plot(constants.h * self.led[i].getFrequencia(),
                mt.sqrt(self.led[i].getEficiencia()),
                "o",
                color = self.led[i].color)
            x.append(constants.h * self.led[i].getFrequencia())
            y.append(mt.sqrt(max(self.led[i].getCorrente())/(constants.e * self.led[i].getNumPhoton())))
            
        c_lin, c_ang, r, p, desvio = stats.linregress(x,y)

        print(f"{c_lin} + {c_ang}*x")
        print(f"{(-c_lin/c_ang)*constants.e}")

        ax.set_xlabel("Energia ($V_0e$)")
        ax.set_ylabel("Raiz da Eficiência ($\sqrt{I_ef}$)")

        plt.savefig("a.png")
    
        return

    def a(self):
        for i in range(len(self.led)):
            light = self.led[i]

            print(f"h nu = {constants.h * light.getFrequencia()}\n eV = {constants.e * light.getPotencialParada()}")

# x,y = getCompLed("Dados/led4.txt")

# plt.plot(x,y)
# plt.show()

amarelo = ExperimentLight("correnteTensao-Amarelo.csv", 600e-9, "yellow")
verde = ExperimentLight("correnteTensao-Verde.csv", 546e-9, "green")
azulClaro = ExperimentLight("correnteTensao-AzulClaro.csv", 503e-9, "lightblue")
roxo = ExperimentLight("correnteTensao-Roxo.csv",445e-9, "purple")
violeta = ExperimentLight("correnteTensao-Violeta.csv",412e-9, "violet")

led1 = ExperimentLight("led-1.csv", 374.22e-9, "violet", 613e-9)
led2 = ExperimentLight("led-2.csv", 467.02e-9, "blue", 13.3e-6)
led3 = ExperimentLight("led-3.csv", 520e-9, "green", 12.4e-6)
led4 = ExperimentLight("led-4.csv", 656e-9, "darkred", 87.4e-6)
led5 = ExperimentLight("led-5.csv", 595e-9, "gold",16.5e-6)
led6 = ExperimentLight("led-6.csv", 628e-9, "salmon",45.4e-6)
led7 = ExperimentLight("led-7.csv", 638.7e-9, "red", 70e-6)

lampada = [amarelo, verde, azulClaro, roxo, violeta]
led = [led1, led2, led3, led4, led5, led6, led7]

exp = ExperimentFinal(lampada,led)

#exp.a()