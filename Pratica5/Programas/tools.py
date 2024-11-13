from imports import *

R = 6.8e-2
n = 320
g = 2.0036

mu_b = constants.physical_constants["Bohr magneton"][0]

def campoHell(I=1, R=R, n=n):
    return constants.mu_0 * (4/5)**(3/2) * n / R * I

def constanteG(ang_cft=1):
    return constants.h * ang_cft / mu_b

def writeNewCollumn(filename="Resultados/frequencia-campoHall-campoMedido.csv",freq=None,corrente=None,campo=None):
    campoCalculado = campoHell(corrente/2)
    with open(filename,"w") as file:
        file.write("Frequência,Campo Hall,Campo Calculado\n")
        for i in range(len(campoCalculado)):
            t = f"{freq[i]:.3e},{campo[i]:.3e},{campoCalculado[i]:.3e}"
            file.write(t)
            file.write("\n")

def curveFunction(c_ang,c_lin,start,stop):
    x = np.linspace(start,stop,4)
    y = []
    for i in x:
        y.append(c_lin + c_ang*i)
    y = np.array(y)

    return x,y