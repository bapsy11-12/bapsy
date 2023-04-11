class parImpar:
    
    numeros:int = []

    def __init__(self, lista):
        self.numeros = lista

    def add(self, n:int):
        self.numeros.append(n)

    def sumarPar(self)->int:
        sumarPar:int = 0
        for x in self.numeros:
            if x%2==0:
                sumarPar += x
        return sumarPar
    
    def sumaImpares(self)->int:
        sumaImpares:int = 0
        for x in self.numeros:
            if x%2!=0:
                sumaImpares += x
        return sumaImpares
    
    def cuadradoLista(self):
        numerosCuadrado:int = []
        for x in self.numeros:
            numerosCuadrado.append(x*x)
        return numerosCuadrado