class Persona():
    def __init__(self,nombre,edad,altura,sexo,añosPracticando=0):
        self.__nombre=nombre
        self.__edad=edad
        self.__altura=altura
        self.__sexo=sexo
        super().__init__(añosPracticando)

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self,edad):
        self.__edad=edad

    def getAltura(self):
        return self.__altura

    def setAltura(self,altura):
        self.__altura=altura
    
    def getSexo(self):
            return self.__sexo

    def setSexo(self,sexo):
        self.__sexo=sexo


class Deportista():
    def __init__(self,añosPracticando):
        self.__deporte="Futbol"
        self.__añosPracticando=añosPracticando

    def getDeporte(self):
        return self.__deporte

    def setDeporte(self,deporte):
        self.__deporte=deporte

    def getAñosPracticando(self):
        return self.__añosPracticando

    def setAñosPracticando(self,añosPracticando):
        self.__añosPracticados=añosPracticando

class Futbolista(Persona,Deportista):
    __listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        super().__init__(nombre,edad,altura,sexo,añosPracticando)
        self.__golesMarcados=golesMarcados
        self.__tarjetasRojas=tarjetasRojas
        self.__piernaHabil=piernaHabil
        self.__listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.__golesMarcados

    def setGolesMarcados(self,golesMarcados):
        self.__golesMarcados=golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetasRojas

    def setTarjetasRojas(self,tarjetasRojas):
         self.__tarjetasRojas=tarjetasRojas
        
    def getPiernaHabil(self):
        return self.__piernaHabil

    def setPiernaHabil(self,piernaHabil):
        self.__piernaHabil=piernaHabil

    def __str__(self):
        return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad()) +" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"
