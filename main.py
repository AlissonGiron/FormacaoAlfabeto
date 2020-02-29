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
        regraMinimo = repeticao[simbolo.letra][0]
        regraMaximo = repeticao[simbolo.letra][1]
        
        valorMinimo = regraMinimo.valor + (1 if regraMinimo.operador == Operador.Maior else 0)
        valorMaximo = regraMaximo.valor + (1 if regraMaximo.operador == Operador.MenorIgual else 0)
        
        for i in range(valorMinimo, valorMaximo):
            listaSimbolos[simbolo.letra] = set()
            possibilidade = ""
            
            for j in range(i):
                possibilidade += simbolo.letra
            
            print(possibilidade)
            
            listaSimbolos[simbolo.letra].add(possibilidade)
    
    print(listaSimbolos)
        
simbolos = [
    Simbolo('c', 'j'),
    Simbolo('d', 'k')
]

repeticao = {
    'c': [Regra(Operador.Maior, 1), Regra(Operador.Menor, 4)],
    'd': [Regra(Operador.Maior, 0), Regra(Operador.Menor, 5)],
}

L(simbolos, repeticao)
