import time
import matplotlib.pyplot as plt
import alg_cluster
import random
import alg_project3_solution


def gen_random_clusters(num_clusters):
    cluster_list = []
    for i in range(num_clusters):
        cluster_list.append(alg_cluster.Cluster(set(), random.uniform(-1, 1), random.uniform(-1, 1), 0, 0))
    return cluster_list

x_axis = range(2, 201)
slow_y = []
for i in range(2, 201):
    cluster_list = gen_random_clusters(i)
    start = time.time()
    closet = alg_project3_solution.slow_closest_pairs(cluster_list)
    end = time.time()
    slow_y.append((end-start)*1000)

fast_y = []
for i in range(2, 201):
    cluster_list = gen_random_clusters(i)
    start = time.time()
    closet = alg_project3_solution.fast_closest_pair(cluster_list)
    end = time.time()
    fast_y.append((end-start)*1000)

print(slow_y)
print(fast_y)

plt.plot(x_axis, slow_y, label = "slow_closest_pair")
plt.plot(x_axis, fast_y, label = "fast_closest_pair")
plt.xlabel("Number of clusters")
plt.ylabel("Running time in ms")

plt.title("Running time: fast_closest_pair vs slow_closest_pair")
plt.legend()
plt.show()


