class Paciente:
    #Atributos de la clase
    def __init__(self, nombre, edad, id, horaLlegada):
        self.nombre = nombre
        self.edad = edad
        self.id = id
        self.triaje = None
        self.alta = None
        self.horaLlegada = horaLlegada
        self.horaSalida = None
        self.medicamentos = None