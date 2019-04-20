import numpy as np
from scipy import spatial
from fractions import Fraction
import math
from scipy.stats.stats import pearsonr

def cosine_distance(u, v):
    """
    Returns the cosine of the angle between vectors v and u. This is equal to
    u.v / |u||v|.
    """
    return np.dot(u, v) / (math.sqrt(np.dot(u, u)) * math.sqrt(np.dot(v, v)))

# a=[0.67, 0, 0, 1.67, -2.33, 0, 0]
b=[0.33, 0.33, -0.67, 0, 0, 0, 0]

# a = [0.67, 0, 0, 1.67, -2.33, 0, 0]
# c = [0, 0, 0, -1.67, 0.33, 1.33, 0]

a = [1.67, -2.33]
c = [-1.67, 0.33]

# from scipy.stats import linregress
# print(linregress(a, c))


print(np.corrcoef(a, c)[0, 1])

