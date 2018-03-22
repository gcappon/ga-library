from Gene import *

import numpy as np

class Population(object):

    def __init__(self, 
        generation_id = 0, pop_size=100, dna_size = 10,
        crossover_method = 'one-point', crossover_probability = 1,
        mutation_probability = 0.01):

        self.generation_id = generation_id
        self.pop_size = pop_size
        self.dna_size = dna_size
        self.genes = self._initPopulation()

        self.crossover_method = crossover_method
        self.crossover_probability = crossover_probability

        self.mutation_probability = mutation_probability

    def _initPopulation(self):
        population = []
        for g in range(self.pop_size):
            population.append(Gene(dna_size = self.dna_size))
        return population

    def __repr__(self):
        ret = 'Population (Generation '+ str(self.generation_id) + '): \n'
        ret += '(Population size: ' + str(self.pop_size) + ', DNA size: ' + str(self.dna_size) + ',\n' 
        ret += 'Crossover method: ' + self.crossover_method + ', Crossover probability: ' + str(self.crossover_probability) + ',\n'
        ret += 'Mutation probability: ' + str(self.mutation_probability) + ')\n'  
        for g in self.genes:
            ret += str(g) + '\n'
        return ret

