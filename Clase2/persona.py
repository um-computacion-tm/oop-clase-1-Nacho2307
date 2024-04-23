
class Persona:
    def __init__(self, nombre: str = "Ignacio", apellido: str = "Jayat", dni: int = 45722756, correo: str = "Baigorriajayat@gmail.com", nacionalidad: str = "Argentina", direccion: str = "Sarmiento 14", localidad: str = "La Paz", hobbies: dict = None):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
        self.__correo__ = correo
        self.__nacionalidad__ = nacionalidad
        if hobbies is None:
            hobbies = {"leer", "correr", "gym"}
        self.__hobbies__ = hobbies
        self.__direccion__ = direccion
        self.__localidad__ = localidad
        
    def __str__(self):
        return f'Mis datos son: nombre = {self.__nombre__}, apellido = {self.__apellido__},  dni = {self.__dni__}, correo = {self.__correo__}, nacionalidad = {self.__nacionalidad__}, direccion = {self.__direccion__}, localidad = {self.__localidad__}, hobbies = {self.__hobbies__}'