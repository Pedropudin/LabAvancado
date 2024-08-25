from plot import *

def _getData():
    corrente, campo = getData_list("calibracao.csv")

    c_linear, c_angular, desvio = linearRegression(corrente,campo)

    return corrente, campo, c_linear, c_angular, desvio

def graphCalibracao():
    #Pegando Dados
    corrente, campo, c_linear, c_angular, desvio = _getData()

    #Plotando
    g = createGraph()
    plotList_points_regression(g,corrente,campo)

    axisNames(g,"Corrente (A)","Campo Magnético (T)")

    graphGrid(g)

    return g

def coeficientesCalibracao():
    corrente, campo, c_linear, c_angular, desvio = _getData()
    return c_linear, c_angular

def funcaoCalibracao():
    """Retorna a função que transforma o valor da corrente no campo magnético do eletroíma"""
    corrente, campo, c_linear, c_angular, _ = _getData()

    def f(x):
        return c_angular*x

    return f
