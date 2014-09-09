import time
import random
import itertools
import sys
import fileinput

def nearest_neighbor(A, cities):
    cities1 = dict(cities)
    if A in cities:
        del cities1[A]
    "Find the city in cities that is nearest to city A."
    return min(cities1.keys(), key=lambda x: distance(x, A))

def all_greedy_TSP(cities):
    return shortest(greedy_TSP(cities, start=c) for c in cities)

def all_greedy_exact_TSP(cities, start_size=50, end_size=7):
    startcities = random.sample(cities.keys(), start_size)
    return shortest(greedy_exact_end_TSP(cities, start=c, endsize=end_size) for c in startcities)

def shortest(tours):
    return min(tours, key= lambda tour: total_distance(tour))

def total_distance(tour):
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

def distance(a, b):
    return int(round(abs(a-b)))

def first(cities):
    for k in cities.keys():
        return k
start_time = time.time()
City = complex
cities = {}
for line in fileinput.input():
    order, x, y = map(int, line.strip().split())
    cities[City(x,y)] = order

NN = {C: nearest_neighbor(C, cities) for C in cities}


def greedy_TSP(cities, start=None):
    "At each step, visit the nearest neighbor that is still unvisited."
    if start is None: start = first(cities)
    tour = [start]
    unvisited = dict(cities)
    del unvisited[start]
    #unvisited = cities - {start}
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        del unvisited[C]
        #unvisited.remove(C)
    return tour

def greedy_exact_end_TSP(cities, start=None, endsize=6):
    if start is None: start = first(cities)
    tour = [start]
    unvisited = dict(cities)
    del unvisited[start]
    #unvisited = cities - {start}
    while len(unvisited)>endsize:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        del unvisited[C]
        #unvisited.remove(C)
    ends = map(list, itertools.permutations(set(unvisited.keys())))
    best = shortest([tour[0], tour[-1]] + end for end in ends)
    return tour + best[2:]

def double_greedy_TSP(cities, start=None):
    """At each step, call the last city in the tour A, and consider the
    nearest neighbor B, and also any city D that has A as nearest neighbor."""
    if start is None: start = first(cities)
    tour = [start]
    unvisited = dict(cities)
    del unvisited[start]
    while unvisited:
        A = tour[-1]
        B = NN[A] if NN[A] in unvisited else nearest_neighbor(A, unvisited)
        Ds = [D for D in unvisited if NN[D] == A and D != B]
        C = (min(Ds, key=lambda D: distance(D, A))) if Ds else B
        tour.append(C)
        del unvisited[C]
    return tour

def all_double_greedy_TSP(cities):
    return shortest(double_greedy_TSP(cities, start=c) for c in cities)


def improved_greedy(cities, start_size=10, end_size=4, num_fails=None): 
    "Improve the result of greedy_TSP from each starting point."
    #starts = cities if start_size >= len(cities) else random.sample(cities, start_size)
    #return shortest(improve(greedy_exact_end_TSP(cities, start, end_size), num_fails) 
    #for start in starts)
    return improve(all_greedy_TSP(cities), num_fails)

def improved_greedy3(cities, start_size=10, end_size=4, num_fails=None): 
    "Improve the result of greedy_TSP from each starting point."
    #starts = cities if start_size >= len(cities) else random.sample(cities, start_size)
    #return shortest(improve(greedy_exact_end_TSP(cities, start, end_size), num_fails) 
    #for start in starts)
    return improve(greedy_TSP(cities), 5000)

RNG = random.randrange 

def improve(tour, num_fails=None):
    "Improve the tour by moving or reversing segments (tour[i:j])."
    N = len(tour)
    num_fails = num_fails or 6*N
    # Try moving each individual city to a better spot
    maybe_move_cities(tour)
    # Try reversing each 2- and 3-long segments
    for i in range(N-2):
        maybe_reverse_segment(tour, i, i+2)
    for i in range(N-3):
        maybe_reverse_segment(tour, i, i+3)

    # Randomly pick segment tour[i:j], try to reverse or move it.
    # If Ntries in a row fail to improve, then give up. 
    consecutive_fails = 0
    while consecutive_fails < num_fails:
        i = RNG(N-2)
        j = RNG(i+2, N)
        better = maybe_reverse_segment(tour, i, j)#or maybe_move_somewhere(tour, i, j, cities)
        consecutive_fails = 0 if better else consecutive_fails + 1
    return tour
def maybe_reverse_segment(tour, i, j):
    "If reversing tour[i:j] helps, then do it. Return True if it helps" 
    A, B, C, D = tour[i-1], tour[i], tour[j-1], tour[j]
    # Are edges added less than edges taken away?
    if distance(A, C) + distance(B, D) < distance(A, B) + distance(C, D):
        tour[i:j] = reversed(tour[i:j])
        return True
def maybe_move_cities(tour):
    "Try to relocate each city to the best spot in the tour (closest to neighbors)."
    N = len(tour)
    positions = range(N)
    dummy = object()
    for i in positions:
        A, B, C = tour[i-1], tour[i], tour[(i+1)%N]
        # Try to move city B to the best place it could go: the minimum detour distance
        j = min(positions, key=lambda j: detour(B, tour[j], tour[j-1]))
        D, E = tour[j-1], tour[j]                                                                                            
        if detour(B, D, E) < detour(B, A, C):
            tour[i], tour[j:j] = dummy, [B]
            tour.remove(dummy)

def detour(B, A, C):
    "In going A-B-C, how much of a detour is this over just A-C?"
    return distance(A, B) + distance(B, C) - distance(A, C)
if len(cities)<1000:
    tour = improved_greedy(cities)
else:
    tour = improved_greedy3(cities)
#tour = all_greedy_exact_TSP(cities)
#tour = double_greedy_TSP(cities)
total_dis = total_distance(tour)
print(total_dis)
for i in tour:
    print(cities[i])
print time.time() - start_time, "seconds"
print len(tour)
