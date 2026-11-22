from .config import GAConfig
import random
import copy

def mutation(chromosome: str, config: GAConfig) -> str:
    """
    This function performs the mutation operation on a single chromosome at a rate predefined in the config.
    You should create a probability. Then it should determine if you perform the mutation operation based on the 
    generated probability. If perform mutation, copy the parent chromosome and perform the operation on that copy.
    If you do not perform mutation, return the original.
    Input:
        chromosome: str, chromosome to potentially perform mutation on
        config: GAConfig, configuration for the run
    """
    pass
