import graphviz
import json
class Complemento:
    def complementoAutomata(self,diccionario,nombre):
        j = graphviz.Digraph('Complemento automatas', filename=nombre)
        j.attr(rankdir='LR', size='8,5')
        j.attr('node', shape='circle')

        transiciones = diccionario['transiciones']
        estado = diccionario['estados']

        estadoAceptacion = estado["Aceptacion"]
        estadoInicial = estado["inicial"]
        j.node(estadoAceptacion)
        j.attr('node', shape='doublecircle')
        for i in range(len(transiciones)):
            origen = transiciones[i].get("Origen")
            destino = transiciones[i].get("Destino")
            transicion = transiciones[i].get("transicion")
            j.edge(origen, destino, label=transicion)
        j.save()