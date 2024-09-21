from calibracao import *

elementsDictHall = {1:"Cobre",2:"Zinco",3:"Germanio-p",4:"Germanio-n"}

def _getData(element:int):
    corrente,tensao = getData_array(f"Dados/hall-{elementsDictHall[element]}.csv")
    tensao = -1*tensao # A gente mediu ao contrário
    fatorCalibracao = funcaoCalibracao()

    campo = fatorCalibracao(corrente)

    c_linear, c_angular, desvio = linearRegression(campo,tensao)

    return campo, tensao, c_linear, c_angular, desvio

def _coeficienteHall(I:float,cAngular:float,l:float):
    return (cAngular*l)/(I)

def _densidadePortadores(I:float,cAngular:float,l:float):
    R = _coeficienteHall(I,cAngular,l)
    return constants.e/R

def graphHall(element:int):
    campo, tensao, c_linear, c_angular, desvio = _getData(element)

    g = createGraph()
    plotList_points_regression(g,campo,tensao)

    axisNames(g,"Campo Magnético (T)","Tensão Hall (V)")

    graphGrid(g)

    return g

def hallData(element:int):
    _,_,_,cAngular,_ = _getData(element)
    match element:
        case 1:
            I = cobre["corrente"]
            l = cobre["espessura"]
        case 2:
            I = zinco["corrente"]
            l = zinco["espessura"]
        case 3:
            I = germanio_p["corrente"]
            l = germanio_p["espessura"]
        case 4:
            I = germanio_n["corrente"]
            l = germanio_n["espessura"]
    return _coeficienteHall(I,cAngular,l),_densidadePortadores(I,cAngular,l)

def getInfo_Germanico_p():
    """Retorna corrente na placa e tensão na placa"""

    return 0.0303,0.766

def getInfo_Germanico_n():
    """Retorna corrente na placa e tensão na placa"""

    return 0.03,1.134

def getInfo_Cobre():
    """Retorna corrente na placa"""

    return 15.07

def getInfo_Zinco():
    """Retorna corrente na placa"""

    return 14.92

def numeroPortadores(I,B,Vh,l):
    e = -constants.e

    return (I*B)/(Vh*e*l)

#Tensão na placa 1.134 V
#Corrente na placa 30.0 mA
#Corrente na bobina por Tensão Hall