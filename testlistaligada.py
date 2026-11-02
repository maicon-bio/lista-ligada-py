
from lista_ligada import Lista_Ligada

def test_adicionar():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.tamanho == 3


def test_exibir():
    lista = Lista_Ligada()

    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)

    assert lista.exibir() == "10 -> 20 -> 30 -> null"