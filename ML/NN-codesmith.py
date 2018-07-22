# refer to Section 1 - Numpy
import numpy as np


# refer to 1.1 - Creating Numpy Arrays
input_signal_00 = np.array([0,0])
# Below, create the variables input_signal01, input_signal10, and input_signal11
input_signal_01 = np.array([0,1])
input_signal_10 = np.array([1,0])
input_signal_11 = np.array([1,1])

# refer to 1.2 - Shape of an Array
print('shape of input_signal_00: ', input_signal_00.shape)
two_dimensional_array = np.array([
  [1,2,3],
  [4,5,6]
])
print('shape of two_dimensional_array: ', two_dimensional_array.shape)
# Below, create the variable three_dimensional_array. It should have shape (2,3,4)
print('shape of input_signal_00: ', input_signal_00.shape)
three_dimensional_array = np.array([
  [[1,1,1,1],[1,1,1,1],[1,1,1,1]],
  [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
])
print('shape of three_dimensional_array: ', three_dimensional_array.shape)
# refer to 1.3 - Numpy Broadcasting
# Try adding numpy arrays with different shapes, (or adding a number to an array).
# for instance:
print('Broadcasting example: ', np.array([-1,-2,-3]) + two_dimensional_array)


# refer to Section 2 - A Python Class for Neurons
class Neuron:
    # refer to 2.1 - Initializing Weights and Bias
    def __init__(self, weights = None, bias = None):
      self.weights = weights
      self.bias = bias
      
      if self.weights is None:
        print('in weights if')
        self.weights = (1,2)
        
      if self.bias is None:
        print('in bias if')
        self.bias = 3
      # if weights is None:
      #   self.weights =
      # else:
      #   self.weights = weights
    
    # refer to 2.2 - Activation Function
    def activate(self, n):
      if n >= 0:
        return 1
      else:
        return 0
      
    # refer to 2.3 - Evaluation
    def evaluate(self, input_signal):
      val = np.dot(input_signal, self.weights)
      val = val + self.bias
      val = self.activate(val)
      return val


# Example Neuron:
first_input_above_half = Neuron(weights = [1, 0], bias = -0.5)

# refer to 3.1 - And Neuron
# create the variable and_neuron below
and_neuron = Neuron(weights = [1, 1], bias = -0.5)


# refer to 3.2 - NAND Neuron
# create the variable nand_neuron below
and_neuron = Neuron(weights = [0, 1], bias = -0.5)

# refer to 3.3 - OR Neuron
# create the variable or_neuron below
and_neuron = Neuron(weights = [0, 1], bias = -0.5)


# refer to 3.4 - NOR Neuron
# create the variable nor_neuron below
and_neuron = Neuron(weights = [0, 0], bias = -0.5)

  
# Write the tests outlined by 3.5
#and_neuron.evaluate()



# refer to Section 4 - Dense Networks
class Dense_Network:
  # refer to 4.1
  def __init__(self, layers = None):
    self.layers = layers
  
  # refer to 4.2
  def feed_forward(self, input_signal):
    input_val = []
    output = []
    for layer,i  in self.layers:
      
      if i == 1:
        input_val = input_signal
      else:
        input_val = output
        output = []
      for neuron in layer:
        result = neuron.evaluate(input_val)
        output.append(result)
    return output


# Example Network:
example_network = Dense_Network(layers = [
  [first_input_above_half, first_input_above_half],
  [first_input_above_half]
])
# Once you've completed the feed_forward method, this should print "Feed forward example: 0"
print('Feed forward example: ', example_network.feed_forward([0,1]))

# refer to 4.3 - XOR Network
# create the variable xor_network below


# refer to Section 5 - Activations and Loss
# complete 5.1 by refactoring the Neuron class above

# refer to 5.2 - Mean Squared Error
def mse(expected, actual):
  pass

# complete 5.3 by refactoring the Neuron class above
