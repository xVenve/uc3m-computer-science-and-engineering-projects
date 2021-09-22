import random
import numpy as np
import requests

NUM_STATIONS = 4
SIZE_POPULATION = 100

web_to_request = "http://memento.evannai.inf.uc3m.es/age/test?c="


def initial_population():
    population = np.zeros((SIZE_POPULATION, NUM_STATIONS * 16), dtype=int)
    for i in range(0, len(population)):
        for j in range(0, len(population[0])):
            population[i][j] = random.randint(0, 1)
    return population


def evaluate_population(population):
    evaluations = []
    for i in population:
        chromosome = list_to_string(i)
        evaluation = requests.get(web_to_request + chromosome)
        evaluations.append(float(evaluation.text))
    return evaluations


def list_to_string(list_of_integers):
    return ''.join([str(v) for v in list_of_integers])


def tournament_selection(population, evaluation, num_candidates):
    new_population = []
    for k in range(0, SIZE_POPULATION):
        candidates = []
        for i in range(0, num_candidates):
            n = random.randint(0, len(population) - 1)
            candidates.append([n, evaluation[n]])
        min_evaluation = None
        min_index = None
        for j in range(0, num_candidates):
            if min_evaluation is None or min_evaluation > candidates[j][1]:
                min_evaluation = candidates[j][1]
                min_index = candidates[j][0]
        new_population.append(population[min_index])
    return new_population


def uniform_crossover(population):
    new_population = []
    for i in range(0, len(population), 2):
        a = []
        b = []
        for j in range(0, len(population[0])):
            n = random.randint(0, 1)
            if n == 0:
                a.append(population[i][j])
                b.append(population[i + 1][j])
            else:
                b.append(population[i][j])
                a.append(population[i + 1][j])
        new_population.append(a)
        new_population.append(b)
    return new_population


def mutation(population, factor):
    for i in range(0, len(population)):
        for j in range(0, len(population[0])):
            n = random.randint(0, 100)
            if n < factor:
                population[i][j] = 1 - population[i][j]
    return population


def get_best_chromosome(population, evaluations):
    min_value = min(evaluations)
    min_index = evaluations.index(min_value)
    return min_value, population[min_index]


def AG(cycles, size_tournament, mutation_factor):
    output_file = open('output_genetic_algorithm.txt', 'w')

    population = initial_population()
    evaluations = evaluate_population(population)
    for i in range(0, cycles):
        population_post_selection = tournament_selection(population, evaluations, size_tournament)
        population_post_crossover = uniform_crossover(population_post_selection)
        population = mutation(population_post_crossover, mutation_factor)
        evaluations = evaluate_population(population)

        best_fitness, best_chromosome = get_best_chromosome(population, evaluations)
        print("Generación " + str(i) + ": " + str(best_fitness) + "\t" + list_to_string(best_chromosome))
        output_file.write(str(best_fitness) + " " + list_to_string(best_chromosome) + "\n")
    output_file.close()


if __name__ == '__main__':
    AG(100, 20, 5)
