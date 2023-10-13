from Paciente import Paciente
import queue
import random

class Urgencias:
    def __init__(self):
        self.pacientes = queue.Queue()
        self.cola_llegada = []
        self.doctor1 = True
        self.doctor2 = True
        self.hora = 10.00
        self.hora_doctor1 = 10.00
        self.hora_doctor2 = 10.00

    #dummies
    def getPaciente(self):
        names = ["Samuel", "Alejandro", "Juan Esteban", "Mariana", "Sofia", "Isabela", "Alejandra", "Salome", "Pedro",
                 "Miguel Angel", "Andrea", "Melissa", "Daniela", "Daniel", "Felipe", "Rafael", "Mariana", "Hair",
                 "Miguel", "Yeisson", "Olga", "Sara"]

        name = random.choice(names)
        return name

    def getRandEdad(self):
        e = random.randint(1, 99)
        return e

    def getRandtriaje(self):
        tri = [1,2,3,4]
        return random.choices(tri, weights=[2, 4, 7, 10])[0]
    def getRandRisk(self):
        RMA = [0, 1]
        return random.choices(RMA, weights=[9, 1])[0]

    def getRandAlta(self):
        opciones = ["Se le dió de alta", "Usted decidio irse (alta voluntaria)",
                    "Se te remitió a hospitalización", "Se te remitió a especialista",
                    "Se te remitió a la morgue, lo sentimos"]

        return random.choices(opciones, weights=[5, 5, 5, 5, 5])[0]

    def getRandMedicamentos(self):
        array_medicamentos= ["Acetaminofén", "Sulfato ferroso", "Citramicina", "Desloratadina", "Complejo B", "Complejo A",
                             "Vitamina C", "Noraver Garganta", "Aguita", "Bicarbonato y limóm", "Una inyección y pa´la casa",
                             "Nada, está en perfectas condiciones"]

        if (self.triaje() == 1):
            medicamentos = "Nada, no se le puede dar nada"
        else:
            medicamentos = random.choice(array_medicamentos)
            return medicamentos

    #Metodo de admisión
    def admision(self):
        print("Estas en el proceso de admisión...")
        print()
        personas = int(input("Cuantas personas/pacientes quiere admitir: "))
        cont = 1
        while (cont <= personas):
            ri = self.getRandRisk()
            if (ri == 1):
                print("Su vida esta en riesgo: Si")
                nombre = (f"Desconocido {cont}")
                edad = None
            elif (ri == 0):
                print("Su vida esta en riesgo: No")
                nombre = self.getPaciente()
                edad = self.getRandEdad()
            else:
                print(
                    "ERROR, responda con (si o no) únicamente")
                continue

            id = random.randint(100000, 200000)  # En ambos caso geenera un ID aleatorio y se lo asigna
            horaLlegada = 10.00
            horaSalida = None
            triaje = None
            alta = None
            p = Paciente(nombre, edad, id)
            print("Usted es el paiente con esta info:", "Nombre:", nombre, "Edad:", edad, "ID:", id)
            print("Fuiste agregado correctamente, espera tu turno para ser atendido")

            cola = [cont, nombre, edad, triaje, id, horaLlegada, horaSalida, alta]
            self.cola_llegada.append(cola)
            self.pacientes.put(cont)
            cont += 1
            print("------------------------------------------------------------------------------")

    def cola_pacientes(self):
        print()
        print("La cola de pacientes en orden de llegada: \n")
        for i in self.cola_llegada:
            print(f"Número de paciente: {i[0]}, Nombre: {i[1]}, Edad: {i[2]}, ID: {i[4]}, con hora de llegada: {i[5]}")
        print()
        print("------------------------------------------------------------------------------")


    def triaje(self):
        for i in range(self.pacientes.qsize()):
            pi = self.pacientes.get()
            if (self.cola_llegada[pi - 1][2] == None):
                self.cola_llegada[pi - 1][3] = 1
            elif (self.cola_llegada[pi - 1][3] == None):
                self.cola_llegada[pi - 1][3] = self.getRandtriaje()

            self.pacientes.put(pi)

    def mostrarTriaje(self):
        print()
        print("La cola de pacientes después de realizado el triaje: \n")
        for i in self.cola_llegada:
            print(f"Número de paciente: {i[0]}, Nombre: {i[1]}, Edad: {i[2]}, ID: {i[4]}, Triaje: {i[3]}")
        print()
        print("------------------------------------------------------------------------------")

    def organizarColaPrioridad(self):
        for i in range(len(self.cola_llegada)):
            min_elem = i
            for j in range(i + 1, len(self.cola_llegada)):
                if self.cola_llegada[j][3] < self.cola_llegada[min_elem][3]:
                    min_elem = j

            temp = self.cola_llegada[i]
            self.cola_llegada[i] = self.cola_llegada[min_elem]
            self.cola_llegada[min_elem] = temp

        for k in self.cola_llegada:
            cont = k[0]
            self.pacientes.put(cont)

    def mostrarColaPrioridad(self):
        print()
        print("La cola de pacientes organizados por el triaje para la atención: \n")
        for i in self.cola_llegada:
            print(f"Número de paciente: {i[0]}, Nombre: {i[1]}, Edad: {i[2]}, ID: {i[4]}, Triaje: {i[3]}, Hora de llegada: {i[5]}")
        print()
        print("------------------------------------------------------------------------------")

    def alta(self):
        for i in range(self.pacientes.qsize()):
            pi = self.pacientes.get()
            if (self.cola_llegada[pi - 1][3] == 1 ):
                nrand = random.randint(1, 2)
                if (nrand == 1):
                    self.cola_llegada[pi - 1][7] ="Se te remitió a hospitalización"
                elif (nrand == 2):
                    self.cola_llegada[pi - 1][7] = "Se le remitió a la morgue, lo sentimos"
            elif (self.cola_llegada[pi - 1][3] > 1 ):
                self.cola_llegada[pi - 1][7] = self.getRandAlta()

            self.pacientes.put(pi)

    def mostrarAlta(self):
        print()
        print("------------------------------------------------------------------------------")
        print()
        print("La cola de pacientes después del alta: \n")
        for i in self.cola_llegada:
            print(f"Número de paciente: {i[0]}, Nombre: {i[1]}, Edad: {i[2]}, ID: {i[4]}, Triaje: {i[3]}, Alta: {i[7]}")
        print()

    def atenderPacientes(self):
        print()
        print("Los médicos atendiendo...")
        if self.pacientes.empty():
            print("No hay pacientes en la cola")

        while not self.pacientes.empty():
            print()
            if self.doctor1 == True:
                paciente = self.pacientes.get()
                nombre_paciente = self.cola_llegada[paciente - 1][1]
                id_paciente = self.cola_llegada[paciente - 1][4]
                hora_llegada = self.cola_llegada[paciente - 1][5]
                print(f"El doctor 1 está disponible a las {self.hora_doctor1} y atiende al paciente {nombre_paciente} con ID {id_paciente} con hora de llegada: {hora_llegada}")
                tiempo_consulta = 0.5
                self.doctor1 = False
                self.doctor2 = True
                self.hora_doctor1 += tiempo_consulta
                alta1 = self.cola_llegada[paciente - 1][7]
                print(f"El paciente {nombre_paciente} fue dado de alta: {alta1}. y su hora de salida fue: {self.hora_doctor1} y su medicamento fue: {self.getRandMedicamentos()}")
            elif self.doctor2 == True:
                paciente = self.pacientes.get()
                nombre_paciente = self.cola_llegada[paciente - 1][1]
                id_paciente = self.cola_llegada[paciente - 1][4]
                hora_llegada = self.cola_llegada[paciente - 1][5]
                print(f"El doctor 2 está disponible a las {self.hora_doctor2} y atiende al paciente {nombre_paciente} con ID {id_paciente} con hora de llegada: {hora_llegada}")
                tiempo_consulta = 0.5
                self.doctor2 = False
                self.doctor1 = True
                self.hora_doctor2 += tiempo_consulta
                alta2 = self.cola_llegada[paciente - 1][7]
                print(f"El paciente {nombre_paciente} fue dado de alta: {alta2}. y su hora de salida fue: {self.hora_doctor2} y su medicamento fue: {self.getRandMedicamentos()}")


    def menu(self):
        print("Bienvenido al hospital de estructuras de datos y algoritmos")
        l1 = Urgencias()
        while True:
            print()
            opc = int(input("Seleccione una opción:\n1.Hacer la admisión de pacientes (Aseguráte de entrar todos los que quieres)\n2.Mostrar la cola de pacientes\n3.Hacer Triaje a los pacientes\n4.Mostrar la cola organizada de pacientes según su prioridad (Primero debió haber realizado triaje)\n5.Atender a los pacientes \n6.Mostrar el alta (Primero debió hacer atendido a los pacientes)\n7.Abandonar el hospital\n->"))
            if(opc == 1):
                l1.admision()
            elif(opc == 2):
                l1.cola_pacientes()
            elif(opc == 3):
                l1.triaje()
                l1.mostrarTriaje()
                l1.organizarColaPrioridad()
            elif(opc == 4):
                l1.mostrarColaPrioridad()
            elif(opc == 5):
                l1.alta()
                l1.atenderPacientes()
            elif(opc == 6):
                l1.mostrarAlta()
            elif(opc == 7):
                print("Chao, esperamos no vuelvas pronto")
                exit()




