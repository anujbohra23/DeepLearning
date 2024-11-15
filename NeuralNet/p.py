import numpy as np
np.random.seed(0)

X = [[1, 2, 3, 2.5],
          [2,5,-1,2],
          [-1.5,2.7,3.3,-0.8]]

# weights in the range of -1 and 1 (smaller the better) so that there isn't explosion of values in training

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2) # output of layer 1 is input to layer 2 that's why n_inputs for layer 2 has to be 5 since it was n_neurons for layer 1 and it required for dot product


layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)








 
# weights = [[0.2,0.8,-0.5,1],
#            [0.5,-0.91,0.26,-0.5],
#            [-0.26,-0.27,0.17,0.87]]

# biases1 = [2,3,0.5] 

# weights2 = [[0.1,-0.14,0.5],
#            [-0.5,0.12,-0.33],
#            [-0.44,0.73,-0.13]]

# biases2 = [-1,2,-0.5] 

# layer1_outputs = np.dot(inputs, np.array(weights).T) + biases1
# print(layer1_outputs)


# layer2_outputs =np.dot(layer1_outputs, np.array(weights2).T) + biases2
# print(layer2_outputs)











