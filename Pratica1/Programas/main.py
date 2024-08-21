from plot import *
from calibracao import *
from concentracao import *

condutividade,tensao = getData_array("apagar.csv")

condutividade = (1/condutividade)*100

g = createGraph()

plotList_line(g,condutividade,tensao)

showGraph()