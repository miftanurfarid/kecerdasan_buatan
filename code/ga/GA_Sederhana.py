# Contoh Sederhana GA
import random

# Inisialisasi populasi awal secara acak
def generate_population(size, genes):
    population = []
    for i in range(size):
        chromosome = []
        for j in range(len(genes)):
            chromosome.append(random.choice(genes))
        population.append(chromosome)
    return population

# Fungsi fitness
def fitness(chromosome):
    return sum(chromosome)

# Seleksi orangtua dengan turnamen
def tournament_selection(population, k):
    selected = []
    for i in range(k):
        candidate = random.choice(population)
        for j in range(k-1):
            rival = random.choice(population)
            if fitness(rival) < fitness(candidate):
                candidate = rival
        selected.append(candidate)
    return selected

# Crossover dengan satu titik potong
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutasi dengan flip bit
def mutation(chromosome, p):
    mutated_chromosome = []
    for gene in chromosome:
        if random.random() < p:
            mutated_chromosome.append(1 - gene)
        else:
            mutated_chromosome.append(gene)
    return mutated_chromosome

# Algoritma genetika
def genetic_algorithm(population_size, genes, generations):
    population = generate_population(population_size, genes)
    print(population)
    for i in range(generations):
        print('generation: {}'.format(i))
        parents = tournament_selection(population, 2)
        child1, child2 = crossover(parents[0], parents[1])
        child1 = mutation(child1, 0.1)
        child2 = mutation(child2, 0.1)
        population += [child1, child2]
        population = sorted(population, key=fitness, reverse=True)[:population_size]
    return population[0]

# Contoh penggunaan
genes = [0, 1, 3]
solution = genetic_algorithm(10, genes, 100)
print(solution)
