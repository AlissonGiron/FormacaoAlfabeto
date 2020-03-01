class Operador:
    Maior = 1
    Menor = 2
    MaiorIgual = 3
    MenorIgual = 4
    
class Regra:
    def __init__(self, operador, valor):
        self.operador = operador
        self.valor = valor
        
        
class Simbolo:
    def __init__(self, letra, expoente):
        self.letra = letra
        self.expoente = expoente
        

def L(simbolos, repeticao):
    
    listaSimbolos = {}
    
    for simbolo in simbolos:
        regraMinimo = repeticao[simbolo.expoente][0]
        regraMaximo = repeticao[simbolo.expoente][1]
        
        valorMinimo = regraMinimo.valor + (1 if regraMinimo.operador == Operador.Maior else 0)
        valorMaximo = regraMaximo.valor + (1 if regraMaximo.operador == Operador.MenorIgual else 0)
        
        listaSimbolos[simbolo.letra] = list()

        for i in range(valorMinimo, valorMaximo):
            possibilidade = ""
            
            for j in range(i):
                possibilidade += simbolo.letra
            
            listaSimbolos[simbolo.letra].append(possibilidade)
    
    sequenciaFinal = list()

    for sequencia in listaSimbolos:
        if(len(sequenciaFinal) == 0): 
            sequenciaFinal = listaSimbolos[sequencia]
            continue

        aux = list()
        for s in sequenciaFinal:
            for ss in listaSimbolos[sequencia]:
                aux.append("".join([s, ss]))
            
            sequenciaFinal = aux

    print(sequenciaFinal)

simbolos = [
    Simbolo('ae', 'i'),
    Simbolo('b', 'j'),
    Simbolo('c', 'k'),
]

repeticao = {
    'i': [Regra(Operador.Maior, 1), Regra(Operador.Menor, 4)],
    'j': [Regra(Operador.Maior, 0), Regra(Operador.Menor, 5)],
    'k': [Regra(Operador.MaiorIgual, 2), Regra(Operador.MenorIgual, 6)],
}

L(simbolos, repeticao)
