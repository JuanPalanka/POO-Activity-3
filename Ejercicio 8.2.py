import math
import tkinter as tk
from tkinter import messagebox


class notas:
    def __init__(self):
        self.listanotas = [0.0] * 5

    def calcularpromedio(self):
        suma = 0
        for i in range(len(self.listanotas)):
            suma = suma + self.listanotas[i]
        return suma / len(self.listanotas)

    def calculardesviacion(self):
        prom = self.calcularpromedio()
        suma = 0
        for i in range(len(self.listanotas)):
            suma += math.pow(self.listanotas[i] - prom, 2)
        return math.sqrt(suma / len(self.listanotas))

    def calcularmenor(self):
        menor = self.listanotas[0]
        for i in range(len(self.listanotas)):
            if self.listanotas[i] < menor:
                menor = self.listanotas[i]
        return menor

    def calcularmayor(self):
        mayor = self.listanotas[0]
        for i in range(len(self.listanotas)):
            if self.listanotas[i] > mayor:
                mayor = self.listanotas[i]
        return mayor


class ventanaprincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Notas")
        ancho, alto = 280, 380
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.resizable(False, False)

    def inicio(self):
        self.nota1 = tk.Label(self, text="Nota 1:", anchor="w")
        self.nota1.place(x=20, y=20, width=80, height=23)
        self.camponota1 = tk.Entry(self)
        self.camponota1.place(x=105, y=20, width=135, height=23)

        self.nota2 = tk.Label(self, text="Nota 2:", anchor="w")
        self.nota2.place(x=20, y=50, width=80, height=23)
        self.camponota2 = tk.Entry(self)
        self.camponota2.place(x=105, y=50, width=135, height=23)

        self.nota3 = tk.Label(self, text="Nota 3:", anchor="w")
        self.nota3.place(x=20, y=80, width=80, height=23)
        self.camponota3 = tk.Entry(self)
        self.camponota3.place(x=105, y=80, width=135, height=23)

        self.nota4 = tk.Label(self, text="Nota 4:", anchor="w")
        self.nota4.place(x=20, y=110, width=80, height=23)
        self.camponota4 = tk.Entry(self)
        self.camponota4.place(x=105, y=110, width=135, height=23)

        self.nota5 = tk.Label(self, text="Nota 5:", anchor="w")
        self.nota5.place(x=20, y=140, width=80, height=23)
        self.camponota5 = tk.Entry(self)
        self.camponota5.place(x=105, y=140, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(
            self, text="Limpiar",
            command=lambda: self.actionperformed(self.limpiar))
        self.limpiar.place(x=125, y=170, width=80, height=23)

        self.promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.promedio.place(x=20, y=210, width=240, height=23)

        self.desviacion = tk.Label(self, text="Desviacion = ", anchor="w")
        self.desviacion.place(x=20, y=240, width=240, height=23)

        self.mayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.mayor.place(x=20, y=270, width=240, height=23)

        self.menor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.menor.place(x=20, y=300, width=240, height=23)

    def validarnotas(self):
        campos = [self.camponota1, self.camponota2, self.camponota3,
                  self.camponota4, self.camponota5]
        valores = []
        for i, campo in enumerate(campos, start=1):
            texto = campo.get().strip()
            if texto == "":
                messagebox.showwarning(
                    "Dato faltante",
                    f"La nota {i} no ha sido ingresada. "
                    "Es obligatorio ingresar las cinco notas.")
                campo.focus_set()
                return None
            try:
                valor = float(texto.replace(",", "."))
                if not math.isfinite(valor):
                    raise ValueError
            except ValueError:
                messagebox.showwarning(
                    "Dato no valido",
                    f"La nota {i} debe ser un valor numerico "
                    f"(se ingreso: '{texto}').")
                campo.focus_set()
                campo.select_range(0, tk.END)
                return None
            valores.append(valor)
        return valores

    def actionperformed(self, evento):
        if evento is self.calcular:
            valores = self.validarnotas()
            if valores is None:
                return
            n = notas()
            for i in range(5):
                n.listanotas[i] = valores[i]

            self.promedio.config(
                text="Promedio = " + "%.2f" % n.calcularpromedio())
            self.desviacion.config(
                text="Desviacion estandar = " + "%.2f" % n.calculardesviacion())
            self.mayor.config(text="Valor mayor = " + str(n.calcularmayor()))
            self.menor.config(text="Valor menor = " + str(n.calcularmenor()))

        if evento is self.limpiar:
            self.camponota1.delete(0, tk.END)
            self.camponota2.delete(0, tk.END)
            self.camponota3.delete(0, tk.END)
            self.camponota4.delete(0, tk.END)
            self.camponota5.delete(0, tk.END)


miventanaprincipal = ventanaprincipal()
miventanaprincipal.mainloop()