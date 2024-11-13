from tools import *

data = pd.read_csv("Dados/campo-corrente-frequencia.csv")

campo = data["campo Magnético (mT)"]*1e-3
corrente = data["corrente (A)"]
frequencia = data["frequencia (MHz)"]*1e6

campoCalculado = campoHell(corrente/2)

regCalculado = stats.linregress(campoCalculado,frequencia)
regMedido = stats.linregress(campo,frequencia)

xMedido,yMedido = curveFunction(regMedido[0],regMedido[1],0,3.5e-3)
xCalculado, yCalculado = curveFunction(regCalculado[0],regCalculado[1],0,3.5e-3)
xEsperado, yEsperado = curveFunction(g*mu_b/constants.h,0,0,3.5e-3)

gCalculado = constanteG(regCalculado[0])
gMedido = constanteG(regMedido[0])


plt.plot(campo*1e3,frequencia*1e-6, "o",color="blue")
plt.plot(xMedido*1e3,yMedido*1e-6,label="Sonda Hall",color="blue")
plt.plot(campoCalculado*1e3,frequencia*1e-6, "o",color="red")
plt.plot(xCalculado*1e3,yCalculado*1e-6,label="Equação Bobina",color="red")
plt.plot(xEsperado*1e3,yEsperado*1e-6,label="Esperado",color="green")
plt.legend()
plt.grid()
plt.xlabel("Campo Magnético (mT)")
plt.ylabel("Frequência (MHz)")
plt.savefig("Resultados/" + "campo-frequencia.png")
plt.show()
plt.clf()

print(f"g com sonda Hall: {gMedido:.3f}\ng com equação da Bobina: {gCalculado:.3f}")
print(f"g esperado: {g:.3f}")

writeNewCollumn(freq=frequencia,campo=campo,corrente=corrente)