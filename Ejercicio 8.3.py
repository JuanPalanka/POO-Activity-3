import base64
import math
import tkinter as tk
import urllib.request
from tkinter import messagebox

urlcilindro = "https://commons.wikimedia.org/wiki/Special:FilePath/Red_cylinder.png?width=110"
urlesfera = "https://commons.wikimedia.org/wiki/Special:FilePath/Sphere_wireframe_10deg_6r.svg?width=110"
urlpiramide = "https://commons.wikimedia.org/wiki/Special:FilePath/Square_pyramid.png?width=110"
urlcubo = "https://commons.wikimedia.org/wiki/Special:FilePath/Hexahedron.svg?width=110"
urlprisma = "https://commons.wikimedia.org/wiki/Special:FilePath/Cuboid_no_label.svg?width=110"


def obtenerimagen(url):
    try:
        peticion = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (compatible; ejerciciofiguras/1.0)"})
        with urllib.request.urlopen(peticion, timeout=8) as respuesta:
            datos = respuesta.read()
        return tk.PhotoImage(data=base64.b64encode(datos))
    except Exception:
        return None


def centrarventana(ventana, ancho, alto):
    x = (ventana.winfo_screenwidth() - ancho) // 2
    y = (ventana.winfo_screenheight() - alto) // 2
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def mostrarimagen(ventana, url, ancho):
    ventana.imagen = tk.Label(ventana)
    ventana.imagen.place(x=0, y=10, width=ancho, height=110)
    ventana.foto = obtenerimagen(url)
    if ventana.foto is not None:
        ventana.imagen.config(image=ventana.foto)
    else:
        ventana.imagen.config(text="Imagen no disponible")


class figurageometrica:
    def __init__(self):
        self.__volumen = 0.0
        self.__superficie = 0.0

    def setvolumen(self, volumen):
        self.__volumen = volumen

    def setsuperficie(self, superficie):
        self.__superficie = superficie

    def getvolumen(self):
        return self.__volumen

    def getsuperficie(self):
        return self.__superficie


class cilindro(figurageometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.__radio = radio
        self.__altura = altura
        self.setvolumen(self.calcularvolumen())
        self.setsuperficie(self.calcularsuperficie())

    def calcularvolumen(self):
        volumen = math.pi * self.__altura * math.pow(self.__radio, 2.0)
        return volumen

    def calcularsuperficie(self):
        arealadoa = 2.0 * math.pi * self.__radio * self.__altura
        arealadob = 2.0 * math.pi * math.pow(self.__radio, 2.0)
        return arealadoa + arealadob


class esfera(figurageometrica):
    def __init__(self, radio):
        super().__init__()
        self.__radio = radio
        self.setvolumen(self.calcularvolumen())
        self.setsuperficie(self.calcularsuperficie())

    def calcularvolumen(self):
        volumen = (4*math.pi*self.__radio**3)/3
        return volumen

    def calcularsuperficie(self):
        superficie = (4*math.pi*self.__radio**2)
        return superficie


class piramide(figurageometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.__base = base
        self.__altura = altura
        self.__apotema = apotema
        self.setvolumen(self.calcularvolumen())
        self.setsuperficie(self.calcularsuperficie())

    def calcularvolumen(self):
        volumen = (math.pow(self.__base, 2.0) * self.__altura) / 3.0
        return volumen

    def calcularsuperficie(self):
        areabase = math.pow(self.__base, 2.0)
        arealado = 2.0 * self.__base * self.__apotema
        return areabase + arealado


class cubo(figurageometrica):
    def __init__(self, lado):
        super().__init__()
        self.__lado = lado
        self.setvolumen(self.calcularvolumen())
        self.setsuperficie(self.calcularsuperficie())

    def calcularvolumen(self):
        volumen = math.pow(self.__lado, 3.0)
        return volumen

    def calcularsuperficie(self):
        superficie = 6.0 * math.pow(self.__lado, 2.0)
        return superficie


class prisma(figurageometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.__largo = largo
        self.__ancho = ancho
        self.__altura = altura
        self.setvolumen(self.calcularvolumen())
        self.setsuperficie(self.calcularsuperficie())

    def calcularvolumen(self):
        volumen = self.__largo * self.__ancho * self.__altura
        return volumen

    def calcularsuperficie(self):
        areabase = self.__largo * self.__ancho
        arealadoa = self.__largo * self.__altura
        arealadob = self.__ancho * self.__altura
        return 2.0 * (areabase + arealadoa + arealadob)


class ventanacilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Cilindro")
        centrarventana(self, 280, 320)
        self.resizable(False, False)

    def inicio(self):
        mostrarimagen(self, urlcilindro, 280)

        self.radio = tk.Label(self, text="Radio (cms):", anchor="w")
        self.radio.place(x=20, y=150, width=80, height=23)
        self.camporadio = tk.Entry(self)
        self.camporadio.place(x=100, y=150, width=135, height=23)

        self.altura = tk.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=180, width=80, height=23)
        self.campoaltura = tk.Entry(self)
        self.campoaltura.place(x=100, y=180, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=100, y=210, width=135, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=240, width=240, height=23)

        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=270, width=240, height=23)

    def actionperformed(self, evento):
        if evento is self.calcular:
            error = False
            radio = 0
            altura = 0
            try:
                radio = float(self.camporadio.get())
                altura = float(self.campoaltura.get())
                micilindro = cilindro(radio, altura)
                self.volumen.config(
                    text="Volumen (cm3): " + "%.2f" % micilindro.calcularvolumen())
                self.superficie.config(
                    text="Superficie (cm2): " + "%.2f" % micilindro.calcularsuperficie())
            except Exception:
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de numero")


class ventanaesfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Esfera")
        centrarventana(self, 280, 300)
        self.resizable(False, False)

    def inicio(self):
        mostrarimagen(self, urlesfera, 280)

        self.radio = tk.Label(self, text="Radio (cms):", anchor="w")
        self.radio.place(x=20, y=150, width=80, height=23)
        self.camporadio = tk.Entry(self)
        self.camporadio.place(x=100, y=150, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=100, y=180, width=135, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=220, width=240, height=23)

        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=250, width=240, height=23)

    def actionperformed(self, evento):
        if evento is self.calcular:
            error = False
            try:
                radio = float(self.camporadio.get())
                miesfera = esfera(radio)
                self.volumen.config(
                    text="Volumen (cm3): " + "%.2f" % miesfera.calcularvolumen())
                self.superficie.config(
                    text="Superficie (cm2): " + "%.2f" % miesfera.calcularsuperficie())
            except Exception:
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de numero")


class ventanapiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Piramide")
        centrarventana(self, 280, 350)
        self.resizable(False, False)

    def inicio(self):
        mostrarimagen(self, urlpiramide, 280)

        self.base = tk.Label(self, text="Base (cms):", anchor="w")
        self.base.place(x=20, y=150, width=100, height=23)
        self.campobase = tk.Entry(self)
        self.campobase.place(x=120, y=150, width=135, height=23)

        self.altura = tk.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=180, width=100, height=23)
        self.campoaltura = tk.Entry(self)
        self.campoaltura.place(x=120, y=180, width=135, height=23)

        self.apotema = tk.Label(self, text="Apotema (cms):", anchor="w")
        self.apotema.place(x=20, y=210, width=100, height=23)
        self.campoapotema = tk.Entry(self)
        self.campoapotema.place(x=120, y=210, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=120, y=240, width=135, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=270, width=240, height=23)

        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=300, width=240, height=23)

    def actionperformed(self, evento):
        if evento is self.calcular:
            error = False
            base = 0
            altura = 0
            apotema = 0
            try:
                base = float(self.campobase.get())
                altura = float(self.campoaltura.get())
                apotema = float(self.campoapotema.get())
                mipiramide = piramide(base, altura, apotema)
                self.volumen.config(
                    text="Volumen (cm3): " + "%.2f" % mipiramide.calcularvolumen())
                self.superficie.config(
                    text="Superficie (cm2): " + "%.2f" % mipiramide.calcularsuperficie())
            except Exception:
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de numero")


class ventanacubo(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Cubo")
        centrarventana(self, 280, 300)
        self.resizable(False, False)

    def inicio(self):
        mostrarimagen(self, urlcubo, 280)

        self.lado = tk.Label(self, text="Lado (cms):", anchor="w")
        self.lado.place(x=20, y=150, width=80, height=23)
        self.campolado = tk.Entry(self)
        self.campolado.place(x=100, y=150, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=100, y=180, width=135, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=220, width=240, height=23)

        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=250, width=240, height=23)

    def actionperformed(self, evento):
        if evento is self.calcular:
            error = False
            try:
                lado = float(self.campolado.get())
                micubo = cubo(lado)
                self.volumen.config(
                    text="Volumen (cm3): " + "%.2f" % micubo.calcularvolumen())
                self.superficie.config(
                    text="Superficie (cm2): " + "%.2f" % micubo.calcularsuperficie())
            except Exception:
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de numero")


class ventanaprisma(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Prisma")
        centrarventana(self, 280, 350)
        self.resizable(False, False)

    def inicio(self):
        mostrarimagen(self, urlprisma, 280)

        self.largo = tk.Label(self, text="Largo (cms):", anchor="w")
        self.largo.place(x=20, y=150, width=80, height=23)
        self.campolargo = tk.Entry(self)
        self.campolargo.place(x=100, y=150, width=135, height=23)

        self.ancho = tk.Label(self, text="Ancho (cms):", anchor="w")
        self.ancho.place(x=20, y=180, width=80, height=23)
        self.campoancho = tk.Entry(self)
        self.campoancho.place(x=100, y=180, width=135, height=23)

        self.altura = tk.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=210, width=80, height=23)
        self.campoaltura = tk.Entry(self)
        self.campoaltura.place(x=100, y=210, width=135, height=23)

        self.calcular = tk.Button(
            self, text="Calcular",
            command=lambda: self.actionperformed(self.calcular))
        self.calcular.place(x=100, y=240, width=135, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=270, width=240, height=23)

        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=300, width=240, height=23)

    def actionperformed(self, evento):
        if evento is self.calcular:
            error = False
            largo = 0
            ancho = 0
            altura = 0
            try:
                largo = float(self.campolargo.get())
                ancho = float(self.campoancho.get())
                altura = float(self.campoaltura.get())
                miprisma = prisma(largo, ancho, altura)
                self.volumen.config(
                    text="Volumen (cm3): " + "%.2f" % miprisma.calcularvolumen())
                self.superficie.config(
                    text="Superficie (cm2): " + "%.2f" % miprisma.calcularsuperficie())
            except Exception:
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de numero")


class ventanaprincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Figuras")
        centrarventana(self, 460, 160)

    def inicio(self):
        self.cilindro = tk.Button(
            self, text="Cilindro",
            command=lambda: self.actionperformed(self.cilindro))
        self.cilindro.place(x=20, y=50, width=75, height=23)

        self.esfera = tk.Button(
            self, text="Esfera",
            command=lambda: self.actionperformed(self.esfera))
        self.esfera.place(x=105, y=50, width=75, height=23)

        self.piramide = tk.Button(
            self, text="Piramide",
            command=lambda: self.actionperformed(self.piramide))
        self.piramide.place(x=190, y=50, width=75, height=23)

        self.cubo = tk.Button(
            self, text="Cubo",
            command=lambda: self.actionperformed(self.cubo))
        self.cubo.place(x=275, y=50, width=75, height=23)

        self.prisma = tk.Button(
            self, text="Prisma",
            command=lambda: self.actionperformed(self.prisma))
        self.prisma.place(x=360, y=50, width=75, height=23)

    def actionperformed(self, evento):
        if evento is self.esfera:
            ventanaesfera()
        if evento is self.cilindro:
            ventanacilindro()
        if evento is self.piramide:
            ventanapiramide()
        if evento is self.cubo:
            ventanacubo()
        if evento is self.prisma:
            ventanaprisma()


miventanaprincipal = ventanaprincipal()
miventanaprincipal.resizable(False, False)
miventanaprincipal.mainloop()