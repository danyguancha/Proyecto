import graphviz
import json
import ntpath
from Modelo.clases.OperacionesAutomatas.Union import *
from Modelo.clases.OperacionesAutomatas.Interseccion import *
from Modelo.clases.OperacionesAutomatas.Complemento import *
from Modelo.clases.OperacionesAutomatas.Reverso import *
class GraficoAutomata:
    def cargarDatos(self, listaRutas):
        ruta1 = listaRutas[0]
        ruta2 = listaRutas[1]
        with open(ruta1) as contenido:
            datos1 = json.load(contenido)
        nombreCadena1 = 'Cadena1'
        self.cargarAutomata1(datos1,nombreCadena1)
        with open(ruta2) as contenido:
            datos2 = json.load(contenido)
        nombreCadena2 = 'Cadena2'
        self.cargarAutomata2(datos2,nombreCadena2)

        union = Union()
        inters = Interseccion()
        complemento = Complemento()
        reverso = Reverso()

        nombreUnion = 'UnionCadena1_cadena2'
        nombreInterseccion = 'InterseccionCadena1_cadena2'
        nombreComplemento = 'Complemento'
        nombreReverso = 'Reverso'

        union.unionAutomata(datos1,datos2,nombreUnion)
        inters.interseccionAutomata(datos1,datos2,nombreInterseccion)
        complemento.complementoAutomata(datos1,nombreComplemento)
        reverso.reversoAutomata(datos1,nombreReverso)

    def cargarAutomata1(self, diccionario,nombre):
        f = graphviz.Digraph('Cadena 1', filename=nombre)
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='doublecircle')

        transiciones = diccionario['transiciones']
        estado = diccionario['estados']

        estadoAceptacion = estado["Aceptacion"]
        f.node(estadoAceptacion)
        f.attr('node', shape='circle')
        print(estadoAceptacion)
        for i in range(len(transiciones)):
            origen = transiciones[i].get("Origen")
            destino = transiciones[i].get("Destino")
            transicion = transiciones[i].get("transicion")
            f.edge(origen,destino, label=transicion)
        f.save()

    def cargarAutomata2(self, diccionario,nombre):
        #j = graphviz.Digraph('finite_state_machine', filename='termine_tres_unos.gv')
        j = graphviz.Digraph('Cadena 2', filename=nombre)
        j.attr(rankdir='LR', size='8,5')

        j.attr('node', shape='doublecircle')

        transiciones = diccionario['transiciones']
        estado = diccionario['estados']

        estadoAceptacion = estado["Aceptacion"]
        estadoInicial = estado["inicial"]
        j.node(estadoAceptacion)
        j.attr('node', shape='circle')
        for i in range(len(transiciones)):
            origen = transiciones[i].get("Origen")
            destino = transiciones[i].get("Destino")
            transicion = transiciones[i].get("transicion")
            j.edge(origen, destino, label=transicion)
        j.save()


a = GraficoAutomata()
rutas = []
ruta1 = "C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena1.3.json"
ruta2 = "C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena2.3.json"
rutas.append(ruta1)
rutas.append(ruta2)

rutas2 =[]
ruta3="C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena1.json"
ruta4="C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena2.json"
rutas2.append(ruta3)
rutas2.append(ruta4)

rutas3 = []
ruta5="C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena1.1.json"
ruta6="C:/Users/aguir/PycharmProjects/proyecto_automatas/venv/Modelo/Automatas/cadena2.1.json"
rutas3.append(ruta5)
rutas3.append(ruta6)


a.cargarDatos(rutas2)