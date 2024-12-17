from tools import *

data = pd.read_csv("Dados/extra-2.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"p", label="1",color="green")
plt.plot(freq,U1,color="green")

plt.plot(freq,U2,"p",color="green")
plt.plot(freq,U2,color="green")

# =========== #

data = pd.read_csv("Dados/extra-0.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"o", label="2",color="blue")
plt.plot(freq,U1,color="blue")

plt.plot(freq,U2,"o",color="blue")
plt.plot(freq,U2,color="blue")

# =========== #

data = pd.read_csv("Dados/extra-1.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]
U2 = data["U2(V)"]

plt.plot(freq,U1,"s", label="3",color="red")
plt.plot(freq,U1,color="red")

plt.plot(freq,U2,"s",color="red")
plt.plot(freq,U2,color="red")

data = pd.read_csv("Dados/extra-nulo.csv")

freq = data["frequencia(MHz)"]
U1 = data["U1(V)"]

plt.plot(freq,U1,"x",color="black")
plt.plot(freq,U1,color="black")

plt.legend()
plt.xlabel("Frequência (MHz)")
plt.ylabel("Tensão (V)")
plt.grid()
plt.savefig("Resultados/extra-todos.png", bbox_inches='tight')
plt.show()
plt.clf()
