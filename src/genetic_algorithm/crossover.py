import random
import copy
from .config import GAConfig

def crossover(parent1: str, parent2: str, config: GAConfig) -> tuple(str):
    """
    Performs the crossover operation on two binary string chromosomes.
    You should create a probability. If you the predefined threshold in the configuration variable,
    you perform the crossover operation. If you do not, you return a tuple that is the original chromosomes.
    If you do perform crossover, return a tuple of the new chromosomes.

    When you are performing crossover, make copies of the original to operate on rather than performing
    the crossover on the originals.

    Input:
        parent1: str, first string of binary
        parent2: str, second string of binary
        config: GAConfig, configuration for the run
    """
    pass
