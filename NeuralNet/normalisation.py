import math
import numpy as np

layer_outputs = [4.3,3.3,4.4]
E = math.e

exp_values = []

for i in layer_outputs:
    exp_values.append(E**i)
print(exp_values)

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)
print(norm_values)
print(sum(norm_values))
    