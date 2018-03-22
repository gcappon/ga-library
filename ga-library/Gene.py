import numpy as np

class Gene(object):

    def __init__(self,id = 0,dna_size=10):
        self.id = id
        self.dna_size = dna_size
        self.gene = self._initGene()

    def _initGene(self):
        return np.random.randint(2, size=self.dna_size)

    def crossover(self):
        pass

    def __repr__(self):
        return 'Gene: ' + str(self.gene)

