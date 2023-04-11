from parImpar import parImpar

def test_add():
    listaNum = parImpar([11,20,15,25,14,85])
    listaNum.add(5)
    assert len(listaNum.numeros) == 6

def test_sumarPar():
    listaNum = parImpar([11,20,15,25,14,85])
    assert listaNum.sumarPar() == 30

def test_sumaImpares():
    listaNum = parImpar([11,20,15,25,14,85,69,44,24])
    assert listaNum.sumaImpares() == 25

def test_cuadradoLista():
    listaNum = parImpar([11,20,15,25,14,85,69,44,24])
    assert listaNum.cuadradoLista() == [30,1,5,7,11,8,6,2]