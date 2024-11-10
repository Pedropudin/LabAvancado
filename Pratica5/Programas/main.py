from tools import *

data = pd.read_csv("Dados/campo-corrente-frequencia.csv")

campo = data["campo Magnético (mT)"]*1e-3
corrente = data["corrente (A)"]
frequencia = data["frequencia (MHz)"]*1e6

campoCalculado = campoHell(corrente/2) # Passa para mT

regCalculado = stats.linregress(campoCalculado,frequencia)
regMedido = stats.linregress(campo,frequencia)

gCalculado = constanteG(regCalculado[0])
gMedido = constanteG(regMedido[0])

plt.plot(campo,frequencia,label="Sonda Hall")
plt.plot(campoCalculado,frequencia,label="Equação Bobina")
plt.legend()
plt.grid()
plt.savefig("Resultados/" + "campo-frequencia.png")
# plt.show()
plt.clf()

print(f"g com sonda Hall: {gMedido:.3f}\ng com equação da Bobina: {gCalculado:.3f}")
print(f"g esperado: {g:.3f}")