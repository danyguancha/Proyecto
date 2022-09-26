import graphviz
import json
class Reverso:
    def reversoAutomata(self, diccionario,nombre):
        j = graphviz.Digraph('Automata reverso', filename=nombre)
        j.attr(rankdir='LR', size='8,5')

        j.attr('node', shape='doublecircle')
        estado = diccionario['estados']
        estadoAceptacion = estado['inicial']
        j.node(estadoAceptacion)
        j.attr('node', shape='circle')

        transiciones = diccionario['transiciones']

        self.aux = ""
        tr = self.encontrarPozo(transiciones)

        for i in range(0,len(transiciones)):
            if transiciones[i]['Destino'] == tr:
                transiciones[i].clear()
            else:
                for c, v in transiciones[i].items():
                    if c == 'Origen':
                        self.aux = transiciones[i]['Origen']
                        transiciones[i]['Origen'] = transiciones[i]['Destino']
                    if c == 'Destino':
                        transiciones[i]['Destino']=self.aux
                j.edge(transiciones[i]['Origen'],transiciones[i]['Destino'],label=transiciones[i]['transicion'])
        #j.save()
    def encontrarPozo(self,listaTransiciones):
        destino =[]
        for i in listaTransiciones:
            destino.append(i['Destino'])
        masRelacionesLlegada = max(set(destino),key=destino.count)
        return str(masRelacionesLlegada)

