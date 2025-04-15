import utils as u
from severidad import Severidad
import matplotlib.pyplot as plt

class SeguroSocial:
    def __init__(self):
        self.lista_pacientes = []
        self.lista_espera = []
        self.lista_enfermedades = []
        self.lista_pacientes_rojo = []
        self.lista_pacientes_naranja = []
        self.lista_pacientes_verde = []

    def agregar_pacientes(self):
        try:
            self.lista_pacientes = u.leer_json("lista_pacientes")
        except:
            print("Hubo un error leyendo el archivo")    

    def agregar_enfermedades(self):
        try:
            self.lista_enfermedades = u.leer_json("lista_enfermedades")
        except:
            print("Hubo un error leyendo el archivo")   

    def generar_lista_espera(self):
        for paciente in self.lista_pacientes:
            id_enfermedad = paciente['enfermedad']
            enfermedad = None
            for e in self.lista_enfermedades:
                if e["id"] == id_enfermedad:
                    enfermedad = e
 
            if enfermedad["urgencia"] == Severidad.VERDE.value:
                self.lista_pacientes_verde.append({
                    "nombre_paciente": " ".join([paciente["nombre"], paciente["apellido"]]),
                    "edad": paciente["edad"],
                    "enfermedad": enfermedad["nombre_enfermedad"]
                })
            elif enfermedad["urgencia"] == Severidad.NARANJA.value:
                self.lista_pacientes_naranja.append({
                    "nombre_paciente": " ".join([paciente["nombre"], paciente["apellido"]]),
                    "edad": paciente["edad"],
                    "enfermedad": enfermedad["nombre_enfermedad"]
                })
            else:
                self.lista_pacientes_rojo.append({
                    "nombre_paciente": " ".join([paciente["nombre"], paciente["apellido"]]),
                    "edad": paciente["edad"],
                    "enfermedad": enfermedad["nombre_enfermedad"]
                })       

    def generar_reporte(self):
        categorias = ["verde", "rojo", "naranja"]
        pacientes = [len(self.lista_pacientes_verde), len(self.lista_pacientes_rojo), len(self.lista_pacientes_naranja)]
        bar_colors = ['green', 'red', 'orange']
        plt.bar(categorias, pacientes, color=bar_colors)
        plt.xlabel('Severidad')
        plt.ylabel('Cantidad')
        plt.title('Resumen de pacientes')
        plt.show()    