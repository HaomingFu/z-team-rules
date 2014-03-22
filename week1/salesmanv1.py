import time
import random
import itertools
import sys
import fileinput

start_time = time.time()
City = complex
cities = {}
for line in fileinput.input():
    order, x, y = map(int, line.strip().split())
    cities[City(x,y)] = order

def total_distance(tour):
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

def distance(a, b):
    return int(round(abs(a-b)))

def first(cities):
    for k in cities.keys():
        return k

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


def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities.keys(), key=lambda x: distance(x, A))

def all_greedy_TSP(cities):
    return shortest(greedy_TSP(cities, start=c) for c in cities)

def all_greedy_exact_TSP(cities, start_size=50, end_size=7):
    startcities = random.sample(cities.keys(), start_size)
    return shortest(greedy_exact_end_TSP(cities, start=c, endsize=end_size) for c in startcities)

def shortest(tours):
    return min(tours, key= lambda tour: total_distance(tour))

if len(cities) < 200:
    tour = all_greedy_exact_TSP(cities, start_size=len(cities), end_size = 8) 
elif len(cities) < 1000:
    tour = all_greedy_exact_TSP(cities, start_size=80, end_size = 8) 
else:
    all_greedy_exact_TSP(cities, start_size=20, end_size=6)
total_dis = total_distance(tour)
print(total_dis)
for i in tour:
    print(cities[i])
print time.time() - start_time, "seconds"
