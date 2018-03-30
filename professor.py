class Professor:
    def __init__(self, nome='', email='', ra='', celular='', cargaHoraria=0):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__cargaHoraria = cargaHoraria

    def getNome():
        return self.__nome
    def getEmail():
        return self.__email
    def getRa():
        return self.__ra
    def getCelular():
        return self.__celular
    def getCargaHoraria():
        return self.__cargaHoraria
    
    def setNome(self, nome):
        self.__nome = nome
    def setEmail(self, email):
        self.__email = email
    def setRa(self, ra):
        self.__ra = ra
    def setCelular(self, celular):
        self.__celular = celular
    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
    
    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])
    
    def adicionaCargaHoraria(self, horas):
        total = self.__cargaHoraria + horas
        if total > 40:
            return "Total de Horas Passa de 40"
        self.__cargaHoraria = total

    def removeHorasCarga(self, horas):
        total = self.__cargaHoraria - horas
        if total = 0:
            return "Total de Horas Passa de 40"
        self.__cargaHoraria = total

p1 = Professor()
