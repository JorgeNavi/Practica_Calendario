class Dia:
    
    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = self.nombrar_dia_semana
        
        if not self.validar_dias_en_meses and not self.validez_fecha:
            raise ValueError('Introduzca una fecha válida')
    
    def info(self):
        return f'El día {self.day} de {self.nombrar_mes} del año {self.year} cayó en {self.weekday}'
    
    def validez_fecha(self):
        if self.year < 0 or self.month < 1 or self.month > 12 or self.day < 1 or self.day > 31:
           return False
        return True
        
    def es_bisiesto(self, year):
        if self.year % 4 == 0:
            if self.year % 100 == 0 and self.year % 400 == 0:
                return True
        return False
    
    def validar_dias_en_meses(self, month):
        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            assert self.day == range(1, 32)
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            assert self.day == range(1, 31)
        elif self.month == 2:
            if self.es_bisiesto:
                assert self.day == range(1, 30)
            else:
                assert self.day == range(1, 29)

    def calcular_dia_semana(self):
        if self.year >= 2000 and self.month>2:
            A = self.year%100
            B = self.year//100
            C = 2 - B + B//4
            D = A//4
            E = 13*(self.month+1)/5
            F = A + C + D +E + self.day -1
        else:
            A = self.year%100
            B = self.year//100
            C = 2 - B + B//4
            D = A//4
            E = 13*(self.month+1)/5
            F = A + C + D +E + self.day
        
        return F % 7
    
    def nombrar_dia_semana(self):
        if self.calcular_dia_semana == 0:
            self.weekday = 'sábado'
        elif self.calcular_dia_semana == 1:
            self.weekday = 'domingo'
        elif self.calcular_dia_semana == 2:
            self.weekday = 'lunes'
        elif self.calcular_dia_semana == 3:
            self.weekday = 'martes'
        elif self.calcular_dia_semana == 4:
            self.weekday = 'miércoles'
        elif self.calcular_dia_semana == 5:
            self.weekday = 'jueves'
        elif self.calcular_dia_semana == 6:
            self.weekday = 'viernes'
    
    def nombrar_mes(self):
        if self.month == 1:
            return 'enero'
        elif self.month == 2:
            return 'febrero'
        elif self.month == 3:
            return 'marzo'
        elif self.month == 4:
            return 'abril'
        elif self.month == 5:
            return 'mayo'
        elif self.month == 6:
            return 'junio'
        elif self.month == 7:
            return 'julio'
        elif self.month == 8:
            return 'agosto'
        elif self.month == 9:
            return 'septiembre'
        elif self.month == 10:
            return 'octubre'
        elif self.month == 11:
            return 'noviembre'
        elif self.month == 12:
            return 'diciembre'
        





dia = Dia()

print(dia.es_bisiesto)



        