from clase_calendario import Dia

def test_create_day():
    dia = Dia()

    assert dia.year == 1970
    assert dia.month == 1
    assert dia.day == 1
    

def test_user_introduce_day():

    dia = Dia(1985, 2, 12)

    assert dia.year == 1985
    assert dia.month == 2
    assert dia.day == 12


def test_comprobar_dia_meses_y_anyos():

    dia = Dia()

    assert dia.year > 0
    assert dia.month > 0 and dia.month < 13
    assert dia.day > 0 and dia.day < 32

def test_es_bisiesto():
    