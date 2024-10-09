from data import *

#========= Pegando Gráficos =========#

#Lâmpada
for ele in lampada:
    ele.plotCorrenteTensao("lampada")

#Leds
for ele in led:
    ele.plotCorrenteTensao("led")

    exp.plotCorrenteTensaoTodos()

# Planck
h_lamp, phi_lamp, erro_lamp = exp.plotPlanck_lampada()
h_led, phi_led, erro_led = exp.plotPlanck_led()

# Velocidade
exp.plotVelocidade_lampada()
exp.plotVelocidade_led()

# Função Trabalho
exp.plotEficienty()

#========= Analisando Valores ========#

with open("Resultados/results.txt", "w") as file:

# Constante de Planck
    file.write("# Constante de Planck\n")
    file.write(f"Real: {constants.h:.3e}\n")
    file.write(f"Obtido pela lâmpada: {h_lamp:.3e} \u00B1 {erro_lamp:.2e} \n")
    file.write(f"Obtido pelo led: {h_led:.3e} \u00B1 {erro_led:.2e}\n")
    
# Função Trabalho
    file.write("\n# Função Trabalho\n")
    file.write(f"\N{latin small letter phi} Coletor Lâmpada: {phi_lamp/constants.e:.3f}\n")
    file.write(f"\N{latin small letter phi} Coletor Led: {phi_led/constants.e:.3f}")

    # Função pra verificar e os valores estão condizentes
    # Calcular velocidade máxima de saída dos elétrons
    # Calcular funções trabalho do ânodo e do cátodo

    file.close()