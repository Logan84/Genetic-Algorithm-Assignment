from .config import GAConfig
from .population import create_population
from .fitness import calculate_fitness
from .selection import roulette_wheel
from .crossover import crossover
from .mutation import mutation

import numpy as np

def genetic_algorithm(config: GAConfig, verbose: bool = False) -> tuple:
    """
    This function holds the full genetic algorithm that you will implement.
    Input:
        config: GAConfig. This is a configuration variable used to configure your experiment.
        verbose: boolean. This is used for if you wish to print certain information during running an experiment.
    Output:
        tuple of three arrays: final population, best fitness at each generation, average fitness at each generation
    """
    pop = []
    best_fitness = []
    avg_fitness = []
    for i in range(config.generations):
        if verbose:
            print(f"Generation: {i+1}\n=======================")
    return (pop, best_fitness, avg_fitness)
