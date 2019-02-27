# Name: Im, Heung Yong (Glen)
# RedID: 823395723
# Date: Feb 27
# PyCharm debugging tools


# Q1

import random
import math
import statistics


# Q2

# create random 100 numbers in range from 0 to 100
list_rand = []
for i in range(100):
    rand_i = random.randrange(0,100)
    list_rand.append(rand_i)

# calculate distance between 2 dimensional points
point_a = (list_rand[random.randrange(0,100)], list_rand[random.randrange(0,100)])
point_b = (list_rand[random.randrange(0,100)], list_rand[random.randrange(0,100)])
distance_a_b = math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)
print(distance_a_b)
print(statistics.mean(list_rand))
print(statistics.stdev(list_rand))


# Q3
# 1 main mod and 2 sub mod
# 1 simple class, 1 simple function in the sub mod
# import the sub mod, create 1 instance of the sub mod class, call the func defined in the sub mod


# 6
class MyKmeans:
    def __init__(self, k, num_points, dimension, lower_bound, upper_bound, points, centroids):
        self.k = k
        self.num_points = num_points
        self.dimension = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.points = points
        self.centroids = centroids

    def set_parameters(self, k, num_points, dimension, lower_bound, upper_bound):




    def generate_points(self, ):



    def initialize_centroids(self):



    def assign_random_clust_number(self):



    def assign_clust_number(self:
        for i in self.points:
            min_dist = sys.maxint

        for j in self.centroids:
            dist = i.calc_distance(self.centroids[j])

            if (min_dist > dist):
                min_dist = dist
                i.clust_id = j



