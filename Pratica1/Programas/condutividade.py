from hall import *

elementsDictCond = {1:"Cobre",2:"Germanio-puro",3:"Germanio-p",4:"Germanio-n"}

def _getData(element:int):
    correnteOhm,tensaoOhm = getData_array(f"Dados/condutividade-lei_ohm-{elementsDictCond[element]}.csv")
    resistencia, temperatura, tensao, corrente = getData_array(f"Dados/condutividade-{elementsDictCond[element]}.csv")

    return correnteOhm, tensaoOhm, resistencia, temperatura, tensao, corrente

def _getCondutividadeR(element:int, R:float):
    match element:
        case 1:
            L = cobre["comprimento"]
            A = cobre["espessura"] * cobre["largura"]
        case 2:
            L = germanio_puro["comprimento"]
            A = germanio_puro["espessura"] * germanio_puro["largura"]
        case 3:
            L = germanio_p["comprimento"]
            A = germanio_p["espessura"] * germanio_p["largura"]
        case 4:
            L = germanio_n["comprimento"]
            A = germanio_n["espessura"] * germanio_n["largura"]
    return L/(R * A)

def _getCondutividadeOhm(element:int, U:float, I:float):
    return _getCondutividadeR(element, U/I)

def a(element):
    Iohm, Vohm, R, T, V, I = _getData(element)

    match element:
        case 1:
            L = cobre["comprimento"]
            A = cobre["espessura"] * cobre["largura"]
        case 2:
            L = germanio_puro["comprimento"]
            A = germanio_puro["espessura"] * germanio_puro["largura"]
        case 3:
            L = germanio_p["comprimento"]
            A = germanio_p["espessura"] * germanio_p["largura"]
        case 4:
            L = germanio_n["comprimento"]
            A = germanio_n["espessura"] * germanio_n["largura"]

    x = T
    y = []
    for i in range(len(R)):
        y.append((I[i] * L)/(V[i] * A))

    g = createGraph()
    plotList_points(g,x,y)
    showGraph()

def graphResistencia(element:int):
    corrente, tensao, _, _, _, _ = _getData(element)
    
    g = createGraph()
    plotList_points_regression(g,corrente,tensao)
    return g

def getResistenciaGraph(element:int) -> float:
    corrente, tensao, _, _, _, _ = _getData(element)
    _, c_angular, _ = linearRegression(corrente,tensao)
    return c_angular

def graphCondutividade(element:int):
    _, _, resistenciaTemp, temp, tensao, corrente = _getData(element)
    resistividade = []
    for i in range(len(tensao)):
        resistividade.append(_getCondutividadeOhm(element, tensao[i], corrente[i]))
    
    g = createGraph()
    plotList_points(g,temp,resistividade)
    graphGrid(g)
    return g

def graphResistividade(element:int):
    _, _, resistenciaTemp, temp, tensao, corrente = _getData(element)
    resistividade = []
    for i in range(len(tensao)):
        resistividade.append(1/(_getCondutividadeOhm(element, tensao[i], corrente[i])))
    
    g = createGraph()
    plotList_points(g,temp,resistividade)
    return g

def convertR_em_T(R,R0,T0):
    return T0 + ((R/R0 - 1)/0.00385)