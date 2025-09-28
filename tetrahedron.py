import random
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def check_valid_imput():
    while True:
        value = input("Enter the side length of the tetrahedron: ")
        if value > 1000:
            print("Please enter a number less than 1,000.")
            continue1
        try:
            val = float(value)
            if val > 0:
                return val
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    

def get_dimentions(side_length):
    p1 = (0, 0, 0)
    p2 = (side_length, 0, 0)
    p3 = (side_length/2, (sqrt(3)/2) * side_length, 0)
    p4 = (side_length/2, (sqrt(3)/6) * side_length, sqrt(2/3) * side_length) 
    return [p1, p2, p3, p4]


def start_point_in_teatraheadron(vertices):
        vertices = np.array(vertices)
        p1, p2, p3, p4 = vertices
        r1, r2, r3 = np.random.rand(3)
        r1, r2, r3 = sorted([r1, r2, r3])
        a = r1
        b = r2 - r1
        c = r3 - r2
        d = 1 - r3
        point = a * p1 + b * p2 + c * p3 + d * p4
        return point



def generate_random_points(vertices, num_points, start_point):
    points = []
    current_point = start_point
    for i in range(num_points):
        chosen_vertex = random.choice(vertices)
        current_point = ((current_point[0] + chosen_vertex[0]) / 2,
                         (current_point[1] + chosen_vertex[1]) / 2,
                         (current_point[2] + chosen_vertex[2]) / 2)
        points.append(current_point)
    return points

def plot_terahedron_and_points(vertices, points):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d') 

    edges = [(0,1), (1,2), (2,0), (0,3), (1,3), (2,3)]
    for i, j in edges:
        ax.plot([vertices[i][0], vertices[j][0]],
                [vertices[i][1], vertices[j][1]],
                [vertices[i][2], vertices[j][2]], 'r-')


    ax.scatter(*zip(*points), s=1, color='blue') 
    ax.set_title("Tetrahedron fractal")
   
    plt.show()
    return



    

side_length = float(5.0)
num_points = 100
start_point = (0, 0)


side_length = check_valid_imput()
vertices = get_dimentions(side_length)
start_point = start_point_in_teatraheadron(vertices)
#print(f"Vertices of the triangle: {vertices}")
#print(f"Random starting point inside the triangle: {start_point}")



num_points = int(input("Enter the number of random points to generate: "))
points = generate_random_points(vertices, num_points, start_point)

print(f"Generated random points inside the triangle; {points}")
plot_terahedron_and_points(vertices, points)





