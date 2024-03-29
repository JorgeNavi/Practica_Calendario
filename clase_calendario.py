class Dia:
    
    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = 0
        if not self.validar_dias_en_meses and not self.validez_fecha:
            raise ValueError('Introduzca una fecha válida')
    
    def info(self):
        return f'El día {self.day} de {self.month} del año {self.year} fue {self.weekday}'
    
    def validez_fecha(self):
        if self.year < 0 or self.month < 1 or self.month > 12 or self.day < 1 or self.day > 31:
           return False
        return True
        
    def es_bisiesto(self):
        if self.year % 4 == 0: 
            if self.year % 100 != 0 or self.year % 400 == 0:
                return True
        else:
            return False
    
    def validar_dias_en_meses(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.day > 31 or self.day < 1:
                raise ValueError('Introducir una fecha válida')
        elif self.month == 2:
            if self.es_bisiesto():
                if self.day > 29 or self.day < 1:
                    raise ValueError('Introducir una fecha válida')
            else:
                if self.day > 28 or self.day < 1:
                    raise ValueError('Introducir una fecha válida')
        else:
            if self.day > 30 or self.day < 1:
                raise ValueError('Introducir una fecha válida')
        return True

    def calcular_dia_semana(self):
        if self.month <= 2:
            self.year = self.year - 1
            self.month = self.month + 12
            

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

        self.weekday = F % 7
        
        return self.weekday
    
    def arreglar_valores_mes_y_año(self):
        """
        al usar calcular_dia_semana, si el mes es enero o febrero, al imprimir la info se le resta 1 al año y se le suma 12 al mes.
        aqui se arregla para que en la info aparezca bien
        """
        if self.month == 13 or self.month == 14:
            self.month = self.month - 12
            self.year = self.year + 1
    
    def nombrar_dia_semana(self):
        if self.weekday == 0:
            self.weekday = 'sábado'
        elif  self.weekday == 1:
            self.weekday = 'domingo'
        elif self.weekday == 2:
            self.weekday = 'lunes'
        elif self.weekday == 3:
            self.weekday = 'martes'
        elif self.weekday == 4:
            self.weekday = 'miércoles'
        elif self.weekday == 5:
            self.weekday = 'jueves'
        else:
            self.weekday = 'viernes'
        
        return self.weekday
    
    def nombrar_meses(self):
        if self.month == 1:
            self.month = 'enero'
        elif self.month == 2:
            self.month = 'febrero'
        elif self.month == 3:
            self.month = 'marzo'
        elif self.month == 4:
            self.month = 'abril'
        elif self.month == 5:
            self.month = 'mayo'
        elif self.month == 6:
            self.month = 'junio'
        elif self.month == 7:
            self.month = 'julio'
        elif self.month == 8:
            self.month = 'agosto'
        elif self.month == 9:
            self.month = 'septiembre'
        elif self.month == 10:
            self.month = 'octubre'
        elif self.month == 11:
            self.month = 'noviembre'
        else:
            self.month = 'diciembre'
    
    
       


        

dia = Dia(1996, 1, 30)
dia.validez_fecha()
dia.validar_dias_en_meses()
dia.calcular_dia_semana()
dia.arreglar_valores_mes_y_año()
dia.nombrar_dia_semana()
dia.nombrar_meses()
print(dia.info())


        