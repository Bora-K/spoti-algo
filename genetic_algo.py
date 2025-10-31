import random

# Let's assume you have your songs data as a dictionary like so:
# songs = {
#     'song1': {'artists': 'artist1', 'length': 200, 'energy': 0.8, 'name': 'song1', 'pop': 62, 'valence': 11.6},
#     'song2': {'artists': 'artist2', 'length': 210, 'energy': 0.6, 'name': 'song2', 'pop': 60, 'valence': 12.5},
#     ...
# }

# Constants
POP_SIZE = 100
TARGET_LENGTH = 3600
MAX_GEN = 500
MUT_RATE = 0.1
TOURN_SIZE = 5
SONG_LIST = list(songs.values())

# Fitness function
def get_fitness(individual, target):
    total_length = sum(song['length'] for song in individual)
    avg_energy = sum(song['energy'] for song in individual) / len(individual)
    return abs(target - total_length) - (1 - avg_energy)

# Initialization
pop = [[random.choice(SONG_LIST) for _ in range(10)] for _ in range(POP_SIZE)]

# Genetic algorithm
for gen in range(MAX_GEN):
    
    # Evaluate population
    fitnesses = [get_fitness(ind, TARGET_LENGTH) for ind in pop]
    
    # Check for termination
    if min(fitnesses) <= 0:
        break
    
    # Selection
    new_pop = []
    for _ in range(POP_SIZE):
        tournament = random.sample(list(zip(pop, fitnesses)), TOURN_SIZE)
        parent = min(tournament, key=lambda x: x[1])[0]
        new_pop.append(parent)
    
    # Crossover
    pop = []
    for i in range(0, POP_SIZE, 2):
        crossover_point = random.randint(1, len(new_pop[i]) - 1)
        child1 = new_pop[i][:crossover_point] + new_pop[i+1][crossover_point:]
        child2 = new_pop[i+1][:crossover_point] + new_pop[i][crossover_point:]
        pop.append(child1)
        pop.append(child2)
    
    # Mutation
    for ind in pop:
        if random.random() < MUT_RATE:
            mutation_point = random.randint(0, len(ind) - 1)
            ind[mutation_point] = random.choice(SONG_LIST)

# Return best solution
best_ind = min(pop, key=lambda ind: get_fitness(ind, TARGET_LENGTH))
print("Best playlist (song names):", [song['name'] for song in best_ind])
