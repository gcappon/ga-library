import numpy as np

def mutation(population):
        
    for g in population.genes:
        for i in range(population.dna_size):
            mute = np.random.random()
            if(mute<=population.mutation_probability):
                g.gene[i] = int(not(g.gene[i]))