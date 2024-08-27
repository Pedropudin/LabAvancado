import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy import constants
import numpy as np

def getData_pandas(file_path):
    data = pd.read_csv(file_path)
    return data

def getData_list(file_path):
    data = getData_pandas(file_path)
    columnNumber = len(data.columns)
    return [data[data.columns[i]].tolist() for i in range(columnNumber)]

def getData_array(file_path):
    data = getData_pandas(file_path)
    columnNumber = len(data.columns)
    return [data[data.columns[i]].to_numpy() for i in range(columnNumber)]

def listFromFunction(func,start,end):
    """Retorna pontos em x e y para a função dada"""

    x = np.linspace(start,end,2)
    y = []
    for n in x:
        y.append(func(n))

    return x,y

def createGraph():
    fig, ax = plt.subplots()
    
    return [fig,ax]

def saveGraph(name):
    plt.savefig(name)

    return

def showGraph():
    plt.legend()
    plt.show()

    return

def clearGraph():
    plt.clf()
    return

def plotList_line(graph, x, y, label = "", colorName = ""):
    if(label == "" and colorName == ""):
        graph[1].plot(x,y)
    elif(label == ""):
        graph[1].plot(x,y,color = colorName)
    elif(colorName == ""):
        graph[1].plot(x,y,label = label)
    else:
        graph[1].plot(x,y,label = label, color = colorName)

    return

def plotList_points(graph, x, y, label = "", colorName = ""):
    if(label == "" and colorName == ""):
        graph[1].scatter(x,y)
    elif(label == ""):
        graph[1].scatter(x,y,color = colorName)
    elif(colorName == ""):
        graph[1].scatter(x,y,label = label)
    else:
        graph[1].scatter(x,y,label = label, color = colorName)

    return 

def plotList_points_regression(graph, x,y):
    """Plota os pontos fornecidos e a melhor reta entre eles"""

    c_linear, c_angular, desvio = linearRegression(x,y)

    def f(x):
        return c_linear + c_angular * x
    
    xLine, yLine = listFromFunction(f,x[0],x[-1])

    plotList_points(graph,x,y,"Data","red")
    plotList_line(graph,xLine, yLine,f"{c_linear}+{c_angular}x","blue")

    return

def graphTitle(graph, title):
    graph[1].set_title(title)

    return

def axisNames(graph, xName, yName):
    graph[1].set_xlabel(xName)
    graph[1].set_ylabel(yName)

    return 

def graphGrid(graph):
    graph[1].grid(True,"major","both")

    return

def linearRegression(x,y):
    """Faz a regressão linear
    Recebe:
        Posição x e y dos pontos
    Retorna:
        Coeficiente angular,
        Coeficiente linear
        Desvio Médio"""
    
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    return intercept, slope, std_err

#y = 0.0084145 + 0.1644x