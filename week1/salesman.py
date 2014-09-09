import time
import random
import itertools
import sys
import fileinput

City = complex
cities = {}
for line in fileinput.input():
    order, x, y = map(int, line.strip().split())
    cities[City(x,y)] = order

def shortest(tours):
    return min(tours, key=total_distance)

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

def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities.keys(), key=lambda x: distance(x, A))
def all_greedy_TSP(cities):
    return shortest(greedy_TSP(cities, start=c) for c in cities)

def shortest(tours):
    return min(tours, key= lambda tour: total_distance(tour))

tour = all_greedy_TSP(cities) if len(cities) < 1000 else greedy_TSP(cities)
total_dis = total_distance(tour)
print(total_dis)
for i in tour:
    print(cities[i])
