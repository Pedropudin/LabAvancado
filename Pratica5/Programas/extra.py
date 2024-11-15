from tools import *

data = pd.read_csv("Dados/extra-0.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"o",color="blue")
plt.plot(freq,U1,label="U1",color="blue")

plt.plot(freq,U2,"o",color="red")
plt.plot(freq,U2,label="U2",color="red")


data = pd.read_csv("Dados/extra-1.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"s",color="blue")
plt.plot(freq,U1,label="U1",color="blue")

plt.plot(freq,U2,"s",color="red")
plt.plot(freq,U2,label="U2",color="red")


data = pd.read_csv("Dados/extra-0.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"p",color="blue")
plt.plot(freq,U1,label="U1",color="blue")

plt.plot(freq,U2,"p",color="red")
plt.plot(freq,U2,label="U2",color="red")



plt.show()
