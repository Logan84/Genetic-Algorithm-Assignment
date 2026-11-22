from src.genetic_algorithm.config import GAConfig
from src.genetic_algorithm.algorithm import genetic_algorithm
from src.genetic_algorithm.plotting import plot


def main():
    # Play with the configuration to see how different parameters impact the performance.
    config = GAConfig()

    population, best_fitness, avg_fitness = genetic_algorithm(config)
    plot(best_fitness, avg_fitness, config)


if __name__ == "__main__":
    main()
