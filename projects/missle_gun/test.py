import numpy as np
import math
vector_1 = [0, 1]

vector_2 = [1, 0]


unit_vector_1 = vector_1 / np.linalg.norm(vector_1)

unit_vector_2 = vector_2 / np.linalg.norm(vector_2)

dot_product = np.dot(unit_vector_1, unit_vector_2)

angle = math.degrees(np.arccos(dot_product))


print(angle)

def my_angle(v1, v2):

    unit_vector_1 = v1 / np.linalg.norm(v1)
    unit_vector_2 = v2 / np.linalg.norm(v2)

    dot_product = np.dot(unit_vector_1, unit_vector_2)

    angle = math.degrees(np.arccos(dot_product))
