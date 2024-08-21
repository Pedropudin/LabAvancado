from plot import *

def graphCalibracao():
    #Pegando Dados
    corrente, campo = getData_list("calibracao.csv")

    c_linear, c_angular, _ = linearRegression(corrente,campo)

    #Plotando
    g = createGraph()
    plotList_points_regression(g,corrente,campo)

    axisNames(g,"Corrente (A)","Campo Magnético (T)")

    graphGrid(g)

    saveGraph("grafico-calibracao.png")

    showGraph()

    return

def coeficientCalibracao():
    #Pegando Dados
    corrente, campo = getData_list("calibracao.csv")

    c_linear, c_angular, _ = linearRegression(corrente,campo)

    return c_linear, c_angular
