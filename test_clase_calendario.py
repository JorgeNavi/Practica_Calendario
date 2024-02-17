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
    pass


def calcular_dia_semana(self):
        if self.year >= 2000 and self.month>2:
            A = self.year%100
            B = self.year//100
            C = 2 - B + B//4
            D = A//4
            E = 13*(self.month+1)//5
            F = A + C + D +E + self.day-1
        else:
            A = self.year%100
            B = self.year//100
            C = 2 - B + B//4
            D = A//4
            E = 13*(self.month+1)//5
            F = A + C + D +E + self.day
        
        return F % 7