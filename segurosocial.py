import utils as u
from severidad import Severidad
import matplotlib.pyplot as plt
import pandas as pd

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

    def filtrar_datos(self):
        df_pacientes = pd.DataFrame(self.lista_pacientes)
        df_enfermedades = pd.DataFrame(self.lista_enfermedades)
        df_joined = df_pacientes.merge(df_enfermedades, how='left', left_on='enfermedad', right_on='id')
        while True:
            print("Filtros disponibles:")
            print("1. Por edad")
            print("2. Por enfermedad")
            print("3. Por urgencia")
            print("4. Salir")
            opcion = int(input("Seleccione la forma en que desea filtrar la informacion: "))

            if opcion == 4:
                break
            elif opcion == 1:
                # edad_max = df_pacientes["edad"].max()
                # edad_min = df_pacientes["edad"].min()
                filtro = input("Desea filtrar por mayor a, menor a o igual que? [>,<,=]: ")
                if filtro == "<":
                    edad = int(input("Digite la edad por la que desea filtrar por: "))
                    print(df_joined[df_joined["edad"] < edad])
                elif filtro == ">":    
                    edad = int(input("Digite la edad por la que desea filtrar por: "))
                    print(df_joined[df_joined["edad"] > edad])
                elif filtro == "=":
                    edad = int(input("Digite la edad por la que desea filtrar por: "))
                    print(df_joined[df_joined["edad"] == edad])  
                else:
                    print("Comando no reconocido")         
