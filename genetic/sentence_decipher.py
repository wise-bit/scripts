'''

for: https://tech.io/playgrounds/334/genetic-algorithms/algorithm?utm_source=codingame&utm_medium=details-page&utm_campaign=puzzle-to-playground&utm_content=mars-lander-2
does not work without is_answer and get_mean_score

'''

import random
from math import *
import sys
## from answer import is_answer, get_mean_score
# from encoding import create_chromosome
# from tools import selection, crossover, mutation

## START

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

'''
Scoring sample

def get_score(chrom):
    key = 'QweJWLgWLIhdvkwyHouO'
    c = list(chrom)
    k = list(key)
    i=0
    while i < len(k):
        if k[i] in c:
            c.remove(k[i])
            k.pop(i)
        else:
            i += 1
    a = (len(chrom)-len(c))/len(chrom)
    return a

'''

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    s=""
    for i in range(size):
        s+=get_letter()
    return(s)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3
    NONGRADED_RETAIN_PERCENT = 0.2 
    scores_dict = {}
 
    for i in range(len(chromosomes_list)):
        curr = chromosomes_list[i]
        scores_dict[curr] = get_mean_score(curr)
        
    selected = []
    scores = sorted(scores_dict.items(), key=lambda kv: kv[1])
    scores.reverse()
    l = len(scores)
    for i in range(ceil(GRADED_RETAIN_PERCENT*l)):
        selected.append(scores[i][0])
        scores.pop(i)
        
    for i in range(ceil(NONGRADED_RETAIN_PERCENT*l)):
        z = random.choice(scores)
        selected.append(z[0])
        scores.remove(z)
    
    return selected

def crossover(parent1, parent2):
    return parent1[0:int(len(parent1)/2)]+parent2[int(len(parent2)/2):]

def mutation(chrom):
    c = list(chrom)
    i = random.randint(0,len(chrom)-1)
    c[i] = get_letter()
    chrom = "".join(c)
    return chrom
    
## END

def create_population(pop_size, chrom_size):
    arr = [] # Create the base population
    for i in range(pop_size):
        chrom = create_chromosome(chrom_size)
        arr.append(chrom)
    return arr

def generation(population):
    select = selection(population) # selection
    # reproduction
    children = []
    # TODO: implement the reproduction
    while len(children) < len(select):
        ## crossover
        parent1 = random.choice(select) # randomly selected
        parent2 = random.choice(select) # randomly selected
        child = crossover(parent1, parent2) # use the crossover(parent1, parent2) function created on exercise 2
        
        if random.random()*100 < 50:
            child = mutation(child) ## mutation
        children.append(child)
    #print("I work: " + str(len(population)), file=sys.stderr)
    return select + children  # return the new generation

def algorithm():
    chrom_size = int(input())
    population_size = 300
    
    # create the base population
    population = create_population(population_size, chrom_size)
    #print(population, file=sys.stderr)
    answers = []
    # while a solution has not been found :
    while not answers:
        #print(answers, file=sys.stderr)
        #print("this is working")
        population = generation(population) ## create the next generation
        
        ## display the average score of the population (watch it improve)
        # print(get_mean_score(population), file=sys.stderr)
    
        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    
    # TODO: print the solution
    print(answers[0])

algorithm()
