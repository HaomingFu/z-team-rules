"""
Template for Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

import math
import alg_cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2

    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), idx1, idx2)


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2)
    where the cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.

    """
    closest_pairs = set()
    closest_distance = float('inf')
    list_size = len(cluster_list)
    for first_index in range(1, list_size):
        for second_index in range(first_index):
            distance = pair_distance(cluster_list, first_index, second_index)
            if distance[0] < closest_distance:
                closest_distance = distance[0]
    for first_index in range(1, list_size):
        for second_index in range(first_index):
            distance = pair_distance(cluster_list, second_index, first_index)
            if distance[0] == closest_distance:
                closest_pairs.add(distance)
    return closest_pairs



def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """
    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))

        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters

        """
        # base case
        if len(horiz_order) <= 3:
            dist = (float('inf'), -1, -1)
            for indice_first in range(1, len(horiz_order)):
                for indice_second in range(indice_first):
                        dist = min(dist, pair_distance(cluster_list, horiz_order[indice_second], horiz_order[indice_first]))
            return dist
        # divide
        half_number = int(math.ceil(len(horiz_order)/float(2)))
        mid = (cluster_list[horiz_order[half_number-1]].horiz_center()+cluster_list[horiz_order[half_number]].horiz_center())/float(2)
        horiz_order_left = horiz_order[:half_number]
        vert_order_left, vert_order_right = [], []
        for indice in vert_order:
            if indice in set(horiz_order_left):
                vert_order_left.append(indice)
            else:
                vert_order_right.append(indice)
        dist_left = fast_helper(cluster_list, horiz_order_left, vert_order_left)
        dist_right = fast_helper(cluster_list, horiz_order[half_number:], vert_order_right)
        min_dist = min(dist_left, dist_right)
        mid_list = [item for item in vert_order if abs(cluster_list[item].horiz_center()-mid) < min_dist[0]]
        mid_list_size = len(mid_list)
        # conquer
        for indice_u in range(mid_list_size-1):
            for indice_v in range(indice_u+1, min(indice_u+3, mid_list_size)):
                min_dist = min(min_dist, pair_distance(cluster_list, mid_list[indice_u], mid_list[indice_v]))

        return min_dist

    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
                        for idx in range(len(cluster_list))]
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
                        for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    return (answer[0], min(answer[1:]), max(answer[1:]))



def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list

    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """
    cluster_size = len(cluster_list)
    while cluster_size > num_clusters:
        first, second = fast_closest_pair(cluster_list)[1:]
        cluster_list[first].merge_clusters(cluster_list[second])
        cluster_list[-1], cluster_list[second] = cluster_list[second], cluster_list[-1]
        cluster_list.pop()
        cluster_size -= 1
    return cluster_list



def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters

    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """
    cluster_list_backup = [item.copy() for item in cluster_list]
    cluster_size = len(cluster_list)
    # initialize k-means clusters to be initial clusters with largest populations
    cluster_list_backup.sort(key = lambda x:x.total_population(), reverse=True)
    clusters = cluster_list_backup[:num_clusters]
    for _ in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for _ in range(num_clusters)]
        for iter_j in range(cluster_size):
            indice = min([(cluster_list_backup[iter_j].distance(clusters[cluster_indice]), cluster_indice) for cluster_indice in range(num_clusters)])[1]
            new_clusters[indice].merge_clusters(cluster_list_backup[iter_j])
        clusters = [item.copy() for item in new_clusters]

    return clusters
