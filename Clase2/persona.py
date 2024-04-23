class Persona:
    def __init__(self, nombre: str = "Ignacio", apellido: str = "Jayat", dni: int = 45722756):
        self.__nombre__ = nombre  # El nombre vive hasta que dure el objeto
        self.__apellido__ = apellido
        self.__dni__ = dni
        
    def __str__(self):
        return(f'Mis datos son: nombre = {self.__nombre__}, apellido = {self.__apellido__},  dni = {self.__dni__}')
    