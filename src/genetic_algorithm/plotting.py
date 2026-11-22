import matplotlib.pyplot as plt
from .config import GAConfig

def plot(best_fit: list[float], avg_fit: list[float], config:GAConfig):
    x = [x+1 for x in range(config.generations)]
    plt.plot(x, best_fit, color="red", label="Best Fit")
    plt.plot(x, avg_fit, color="blue", label="Average Fit")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title(f"GA with {config.generations} generations, {config.crossover_rate} crossover, {config.mutation_rate} mutation")
    plt.legend()
    plt.savefig(f"Generation_{config.generations}_cross_{config.crossover_rate}_mutate_{config.mutation_rate}.png")

