inputs = [1, 2, 3]
weights = [
    0.2,
    0.8,
    -0.5,
]  # so here there is one neuron with 3 connections i.e. 3 weights and inputs
bias = 2  # one bias as it is just one neuron

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)
