from math import exp
from .chromosome import bit_to_num_pipeline

def fitness_function(x: float, y: float) -> float:
    return (1 - x)**2 * exp(-x**2 - (y + 1)**2) - (x - x**3 - y**3) * exp(-x**2 - y**2)

def calculate_fitness(chromosome: str, length: int):
    midpoint = int(length / 2)
    x = chromosome[:midpoint]
    y = chromosome[midpoint:]
    fitness = fitness_function(bit_to_num_pipeline(x), bit_to_num_pipeline(y))
    return fitness
