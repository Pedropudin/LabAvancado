from condutividade import *

def printStart():
    print("Qual prática?")
    print("1 - Calibração")
    print("2 - Efeito Hall")
    print("3 - Condutividade")
    x = int(input())
    return x

def printCalibracao():
    print("O que você quer da calibracao?")
    print("1 - Ver o gráfico")
    print("2 - salvar o gráfico")
    print("3 - Ver a função que aproxima o gráfico")
    x = int(input())
    return x

def printHall():
    print("O que você quer sobre o experimento do efeito hall?")
    print("1 - Ver gráficos (Tensão Hall em função do campo Magnético)")
    print("2 - Salvar os gráficos")
    print("3 - Ver os coeficientes Hall e a densidade de portadores")
    x = int(input())
    return x

def printCondutividade():
    print("O que você quer sobre o experimento da Condutividade?")
    print("1 - Ver resistências dos materiais")
    print("2 - Ver resistividade em função da temperatura")
    x = int(input())
    return x

def calibracao(task:int):
    match task:
        case 1:
            g = graphCalibracao()
            showGraph()
            clearGraph()
        case 2:
            g = graphCalibracao()
            print("Qual o nome? (Deixar vazio coloca \"grafico-calibracao.png\")")
            name = input()
            if name == "":
                saveGraph("grafico-calibracao.png")
            else:
                saveGraph(name)
            clearGraph()
        case 3:
            linear,angular = coeficientesCalibracao()
            print("A função que aproxima o fator de calibração é:")
            print(f"{linear} + {angular} * x")

    return 0

def chooseElement(exp:int) -> int:
    match exp:
        case 2:
            print("1 - Cobre")
            print("2 - Zinco")
            print("3 - Germânio-p")
            print("4 - Germânio-n")
        case 3:
            print("1 - Cobre")
            print("2 - Germânio Intrínseco")
            print("3 - Germânio-p")
            print("4 - Germânio-n")
    return int(input())

def hall(task:int):
    match task:
        case 1:
            print("Esse experimento envolve múltiplos elementos, qual você gostaria de analisar?")
            ele = chooseElement(2)
            g = graphHall(ele)
            graphTitle(g,f"Efeito Hall - {elementsDictHall[ele]}")
            showGraph()
            clearGraph()
        case 2:
            print("Esse experimento envolve múltiplos elementos, qual você gostaria de analisar?")
            ele = chooseElement(2)
            g = graphHall(ele)
            graphTitle(g,f"Efeito Hall - {elementsDictHall[ele]}")
            print(f"Qual o nome? (Deixar vazio coloca \"grafico-hall-{elementsDictHall[ele]}.png\")")
            name = input()
            if name == "":
                saveGraph(f"grafico-hall-{elementsDictHall[ele]}.png")
            else:
                saveGraph(name)
            clearGraph()
        case 3:
            for i in range(1,5):
                R,n = hallData(i)
                print(f"{elementsDictHall[i]}:\n\tCoeficiente Hall:{R:.3e}; Densidade de Portadores:{n:.3e}")
    return 0

def condutividade(task:int):
    match task:
        case 1:
            for i in range(1,5):
                R = getResistenciaGraph(i)
                print(f"{elementsDictCond[i]}: {R:.3e}")
                g = graphResistencia(i)
                showGraph()
        case 2:
            for i in range(1,5):
                g = graphCondutividade(i)
                graphTitle(g,f"{elementsDictCond[i]}")
                showGraph()
    return 0

def main():
    exp = printStart()
    
    match exp:
        case 1:
            task = printCalibracao()
            calibracao(task)
        case 2:
            task = printHall()
            hall(task)
        case 3:
            task = printCondutividade()
            condutividade(task)
        case 4:
            g = createGraph()
            x,y = getData_array("Dados/condutividade-lei_ohm-Cobre.csv")
            plotList_points_regression(g,x,y)
            showGraph()
        case 5:
            a(1)

    return 0

if __name__ == "__main__":
    main()
