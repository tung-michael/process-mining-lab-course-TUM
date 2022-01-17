from process_mining_alg.petri_visualize import PetriNet
from process_mining_alg.xes_importer import EventLog, simplify_log
from itertools import *


class Alpha_alg:
    """ Implementation of Alpha algorithm.
    
    :param log: the full log parsed by xes_importer
    :type log: EventLog
    """
    def __init__(self, log: EventLog):
        self.full_log = log
        self.compact_log = simplify_log(log)
        self.start_event = set()    # TI-set
        self.end_event = set()      # TO-set
        self.events_set = set()     # TL-set
        
        self._events_extraction()
        
        self.direct_followers= self._direct_follow_set()
        self.causal_pairs = self._causality()
        self.independent_pairs = self._independence()
        self.parallel_pairs = self._parallelism()
        self.all_causal_pairs = set() # XL-set
        self.max_causal_pairs = set() # YL-set
        
        self._maximal_causality()
        
    def _events_extraction(self):
        for trace in self.compact_log:
            self.start_event.add(trace[0]) # get first transaction
            self.end_event.add(trace[-1]) # get last transaction
            self.events_set.update(trace) # get all transactions
    
    def generate_petri_net(self):
        """Return the corresponding Petri Net."""
        ptn = PetriNet(self.events_set, self.max_causal_pairs, self.start_event, self.end_event)
        return ptn.visualize()
        
    
    def _check_independence(self, set):
        product_set = product(set, set)
        for element in product_set:
            if element not in self.independent_pairs:
                return False
        return True

    def _check_causality(self, setA, setB):
        product_set = product(setA, setB)
        for element in product_set:
            if element not in self.causal_pairs:
                return False
        return True
      
    def _maximal_causality(self): # build Xl and Yl
        power_set = set() # create a powerset of the events_set TL
        for i in range (1, len(self.events_set)+1):
            power_set.update(combinations(self.events_set,i))
        
        # consider every setA in the powerset if there exists any setB that fulfills:
        # all elements inside set A are independent to the eachother
        # all elements inside set B are independent to the eachother
        # every element in setA causes every element in setB
        for setA in power_set:
            for setB in power_set:
                # if setA and setB satisfy these conditions, add the tuple (setA, setB) into self.all_causal_pairs (XL-set)
                if self._check_independence(setA) and self._check_independence(setB) and self._check_causality(setA, setB):
                    self.all_causal_pairs.add((frozenset(setA), frozenset(setB))) 

        # compare every pair in XL to the eachother to find the max pairs, add them to self.max_causal_pairs (YL-set)
        for pairA in self.all_causal_pairs:
            maxpair = pairA
            for pairB in self.all_causal_pairs:
                if set(maxpair[0]).issubset(pairB[0]) and set(maxpair[1]).issubset(pairB[1]):
                    maxpair = pairB
            self.max_causal_pairs.add(maxpair)
    
    def _direct_follow_set(self): # the '>' relationship
        direct_followers = set()
        for trace in self.compact_log:
            for i in range(0,len(trace) - 1):
                direct_followers.add((trace[i], trace[i+1]))
        return direct_followers

    def _causality(self): # the '->' relationship
        causal_set= set()
        for (a,b) in self.direct_followers:
            if (b,a) not in self.direct_followers:
                causal_set.add((a,b))
        return causal_set

    def _parallelism(self): # the '||' relationship
        parallel_set = set()
        for (a,b) in self.direct_followers:
            if (b,a) in self.direct_followers:
                parallel_set.add((a,b))
        return parallel_set
    
    def _independence(self): # the '#' relationship
        independent_set = set()
        for a in self.events_set:
            for b in self.events_set:
                if (a,b) not in self.direct_followers and (b,a) not in self.direct_followers:
                    independent_set.add((a,b))
        return independent_set
    