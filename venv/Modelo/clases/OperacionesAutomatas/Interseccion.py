import graphviz
import json
class Interseccion:
    def interseccionAutomata(self, diccionario1, diccionario2, nombreArchivo):
        inter = graphviz.Digraph('Interseccion Automatas', filename=nombreArchivo)
        inter.attr(rankdir='LR', size='8,5')

        transiciones1 = diccionario1['transiciones']
        transiciones2 = diccionario2['transiciones']

        estadoAceptacion1 = diccionario1['estados'].get('Aceptacion')
        estadoAceptacion2 = diccionario2['estados'].get('Aceptacion')
        self.estado1=""
        self.estado2=""
        for i in transiciones1:
            for j in transiciones2:
                if i.get("transicion") == j.get("transicion"):
                    self.estado1 = i.get("Origen") + j.get("Origen")
                    self.estado2 = i.get("Destino") + j.get("Destino")
                    # if estado1==estado2 or estadoAceptacion1 ==i.get("Origen") and estadoAceptacion2==i.get("Destino")  :
                    if  estadoAceptacion1 == i.get("Origen") and estadoAceptacion2 == j.get("Origen"):

                        inter.attr('node', shape='doublecircle')
                        inter.node(self.estado1)

        for i in transiciones1:
            for j in transiciones2:
                if i.get("transicion") == j.get("transicion"):
                    self.estado1 = i.get("Origen") + j.get("Origen")
                    self.estado2 = i.get("Destino") + j.get("Destino")
                    # if estado1==estado2 or estadoAceptacion1 ==i.get("Origen") and estadoAceptacion2==i.get("Destino")  :
                    """if  estadoAceptacion1 == i.get("Origen") and estadoAceptacion2 == j.get("Origen"):

                        inter.attr('node', shape='doublecircle')
                        inter.node(self.estado1)"""

                    inter.attr('node', shape='circle')
                    inter.edge(self.estado1, self.estado2, label=i.get("transicion"))

        inter.save()