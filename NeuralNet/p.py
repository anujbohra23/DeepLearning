import numpy as np 
import nnfs
from nnfs.datasets import spiral_data  # See for code: https://gist.github.com/Sentdex/454cb20ec5acf0e76ee8ab8448e6266c

nnfs.init()




X = [[1, 2, 3, 2.5],
          [2,5,-1,2],
          [-1.5,2.7,3.3,-0.8]]

X, y = spiral_data(100, 3)   

inputs= [0.2,-1,3.3,-2.7,1.1,2.2,-100]
output = []

for i in inputs:
    if i>0:
        output.append(max(0,i))
    elif i<=0:
        output.append(0)
print(output)
        

#weights in the range of -1 and 1 (smaller the better) so that there isn't explosion of values in training

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
        
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)

        

layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()


layer1.forward(X)
# print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)





