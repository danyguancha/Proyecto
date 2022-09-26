import graphviz
import json
class Union:
    def unionAutomata(self,diccionario1,diccionario2,nombreArchivo):
        union = graphviz.Digraph('Union Automatas', filename=nombreArchivo)
        union.attr(rankdir='LR', size='8,5')

        transiciones1 = diccionario1['transiciones']
        transiciones2 = diccionario2['transiciones']

        estadoAceptacion1 = diccionario1['estados'].get('Aceptacion')
        estadoAceptacion2 = diccionario2['estados'].get('Aceptacion')
        self.estado1 =""
        self.estado2 =""
        self.origen=""
        self.destino =""
        self.transicion=""

        for i in transiciones1:
            for j in transiciones2:
                if i.get("transicion")== j.get("transicion"):
                    estado1 = i.get("Origen")+j.get("Origen")
                    estado2 = i.get("Destino")+j.get("Destino")
                    #if estado1==estado2 or estadoAceptacion1 ==i.get("Origen") and estadoAceptacion2==i.get("Destino")  :
                    if estadoAceptacion1 == i.get("Origen") and estadoAceptacion1 == i.get("Destino") or estadoAceptacion2 == j.get("Origen") and estadoAceptacion2 == j.get("Destino"):
                    #or estadoAceptacion1 == j.get("Origen") and estadoAceptacion1 == j.get("Destino")

                        union.attr('node', shape='doublecircle')
                        union.node(estado1)

        for i in transiciones1:
            for j in transiciones2:
                if i.get("transicion")== j.get("transicion"):
                    estado1 = i.get("Origen")+j.get("Origen")
                    estado2 = i.get("Destino")+j.get("Destino")
                    #if estado1==estado2 or estadoAceptacion1 ==i.get("Origen") and estadoAceptacion2==i.get("Destino")  :
                    """if estadoAceptacion1 == i.get("Origen") and estadoAceptacion1 == i.get("Destino") or estadoAceptacion2 == j.get("Origen") and estadoAceptacion2 == j.get("Destino"):
                    #or estadoAceptacion1 == j.get("Origen") and estadoAceptacion1 == j.get("Destino")

                        union.attr('node', shape='doublecircle')
                        union.node(estado1)"""

                    union.attr('node', shape='circle')
                    union.edge(estado1, estado2, label=i.get("transicion"))
        #union.save()