# Los objetos son como variables
#init es el constructor 
 
#Clase
class Profesor:
    def __init__(self, el_nombre, edad): #El parametro que pasan por fuera se lo pone el mismo (prof)
        self.nombre = el_nombre # El self es yo 
        self.edad = edad
    def dame_tu_nombre(self):
     return self.nombre
   
class Alumno:
    def __init__(self, Nombre_Alumno, apellido):
        self.__nombre__ = Nombre_Alumno
        self.__apellido__ =  apellido
        self.__inasistencias__ = 0 
        self.__dieta__ = ""
        self.__mentor__ = None
    
    def mentoria(self, Profesor):
        self.__mentor__ = Profesor
    
    def falta(self):
        self.__inasistencias__ += 1 
    
    def elegir_dieta(self, dieta):
        self.__dieta__ = dieta
    
    def Carnivoro(self):
     self.__dieta__ = "carnivoro"

    def libre(self):
     if self.__inasistencias__ > 5 :
         return "Esta hasta las manos el pib@"
     else:
         return "ta piola"



# Objetos
prof_elio = Profesor("Elio", "23")
prof_gabi = Profesor("Gabriel", "52")

print(prof_elio.dame_tu_nombre())
print(prof_gabi.dame_tu_nombre())

alumno_Igna = Alumno("Ignacio", "Aguilera")
alumno_Mati = Alumno("Matias", "Rojas")

alumno_Igna.falta()
alumno_Mati.falta()
print(alumno_Mati.libre())
alumno_Mati.falta
print(alumno_Mati.libre())

alumno_Mati.elegir_dieta("Carnivoro")
print(alumno_Mati.dieta)
alumno_Mati.Carnivoro()
print(alumno_Mati.dieta)

alumno_Igna.mentoria(prof_elio)

print(alumno_Igna.mentor)


import ipdb; ipdb.set_trace()