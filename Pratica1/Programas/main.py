from calibracao import *
from hall import *

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
    print("")
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
            print("2 - Germânio Intrinseco")
            print("3 - Germânio-p")
            print("4 - Germânio-n")
    return int(input())

def hall(task:int):
    match task:
        case 1:
            print("Esse experimento envolve múltiplos elementos, qual você gostaria de analisar?")
            ele = chooseElement(2)
            g = graphHall(ele)
            graphTitle(g,f"Efeito Hall - {elementsDict[ele]}")
            showGraph()
            clearGraph()
        case 2:
            print("Esse experimento envolve múltiplos elementos, qual você gostaria de analisar?")
            ele = chooseElement(2)
            g = graphHall(ele)
            graphTitle(g,f"Efeito Hall - {elementsDict[ele]}")
            print(f"Qual o nome? (Deixar vazio coloca \"grafico-hall-{elementsDict[ele]}.png\")")
            name = input()
            if name == "":
                saveGraph("grafico-hall-{elementsDict[ele]}.png")
            else:
                saveGraph(name)
            clearGraph()
        case 3:
            for i in range(1,5):
                R,n = hallData(i)
                print(f"{elementsDict[i]}:\n\tCoeficiente Hall:{R}; Densidade de Portadores:{n}")
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

    return 0

if __name__ == "__main__":
    main()