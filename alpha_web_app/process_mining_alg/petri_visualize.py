import graphviz

class PetriNet:
    """This class visualizes a Petri Net using graphviz library.
    
    :param transitions: set of transitions to be illustrated in the Petri Net
    :type transitions: set{str}
    :param places: set of places to be illustrated in the Petri Net
    :type places: set{tuple(frozenset(), frozenset())}
    :param start_transitions: set of start transition
    :type start_transitions: set{str}
    :param end_transitions: set of end transition
    :type end_transitions: set{str}
    """
    def __init__(self, transitions, places, start_transitions, end_transitions ):
        self.places = places    # maximal_causal_pairs - YL-set
        self.transitions = transitions # events_set - TL-set
        self.start_transitions = start_transitions
        self.end_transitions = end_transitions
    
    def visualize(self):
        """Return a Digraph for visualization with graphviz."""
        
        ptn = graphviz.Digraph(graph_attr={'rankdir': 'LR', 'fontname': 'Helvetica', 'center' : 'True', 'margin':'0.3'})
        ptn.node('Start', shape = "circle", fontsize = '10')
        ptn.node('End', shape = "doublecircle", fontsize = '10')
        for t in self.transitions:
            ptn.node(t, shape = "box", fontsize = '20')
        for place in self.places:
            p_name = self._create_place_name(place)
            ptn.node(p_name, shape = "circle", width = '0.5', fixedsize = 'true', fontsize = '0', fontcolor = 'white')
            for i in place[0]:
                ptn.edge(i, p_name)
            for j in place[1]:
                ptn.edge(p_name, j)
        for s in self.start_transitions:
            ptn.edge('Start', s)
        for e in self.end_transitions:
            ptn.edge(e, 'End')
        
        return ptn
    
    def _create_place_name(self, place):
        A = "{" + self._frozenset_to_string(place[0]) + "}"
        B = "{" + self._frozenset_to_string(place[1]) + "}"
        return 'p('+A+', '+B+')'
    
    def _frozenset_to_string(self, frs):
        # Converting frozenset into string without the prefix 'frozenset'
        s = ""
        j = 0
        for e in frs:
            if j > 0:
                s = s + ", "
            s = s + e
            j = j + 1
        return s
