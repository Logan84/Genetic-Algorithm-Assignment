from dataclasses import dataclass

@dataclass
class GAConfig:
    population_size: int = 6
    bit_length: int = 8
    generations: int = 200
    crossover_rate: float = 0.9
    mutation_rate: float = 0.01
    seed: int | None = None
