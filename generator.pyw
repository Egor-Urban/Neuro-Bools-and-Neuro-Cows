#IMPORT
import random

#CLASSES
class Neuron1: 
    def __init__(self, num_inputs): 
        self.weights = [random.uniform(1, 9) for _ in range(num_inputs)] 

    def activate(self, inputs): 
        result = 0  
        for i in range(len(inputs)): 
            result += inputs[i] * self.weights[i]
        return result  
    def generate_output(self):  
        inputs = [random.randint(1, 9) for _ in range(45)]  
        activation = self.activate(inputs)  
        output = int(activation % 9) + 1  
        return output
    
class Neuron2: 
    def __init__(self, num_inputs): 
        self.weights = [random.uniform(1, 9) for _ in range(num_inputs)] 

    def activate(self, inputs):  
        result = 0  
        for i in range(len(inputs)):  
            result += inputs[i] * self.weights[i]  
        return result  

    def generate_output(self): 
        inputs = [random.randint(1, 9) for _ in range(45)]  
        activation = self.activate(inputs)  
        output = int(activation % 9) + 1  
        return output
    
class Neuron3: 
    def __init__(self, num_inputs): 
        self.weights = [random.uniform(1, 9) for _ in range(num_inputs)] 

    def activate(self, inputs):  
        result = 0  
        for i in range(len(inputs)):  
            result += inputs[i] * self.weights[i]  
        return result 

    def generate_output(self):  
        inputs = [random.randint(1, 9) for _ in range(45)]  
        activation = self.activate(inputs) 
        output = int(activation % 9) + 1 
        return output
    
class Neuron4: 
    def __init__(self, num_inputs): 
        self.weights = [random.uniform(1, 9) for _ in range(num_inputs)] 

    def activate(self, inputs):  
        result = 0 
        for i in range(len(inputs)):  
            result += inputs[i] * self.weights[i]  
        return result  

    def generate_output(self):  
        inputs = [random.randint(1, 9) for _ in range(45)]  
        activation = self.activate(inputs)  
        output = int(activation % 9) + 1 
        return output  



neuron1 = Neuron1(45) 
num1 = neuron1.generate_output()  
neuron2 = Neuron2(45)  
num2 = neuron2.generate_output()  
neuron3 = Neuron3(45)  
num3 = neuron3.generate_output()  
neuron4 = Neuron4(45)  
num4 = neuron4.generate_output() 

def make_numbers_different(numbers):
    for i in range(len(numbers)):
        while numbers.count(numbers[i]) > 1:
            if numbers[i] < 9:
                numbers[i] += 1
            else:
                numbers[i] -= 1
    return numbers

numbers = [num1, num2, num3, num4]
result = make_numbers_different(numbers)

class Neuron:
    def __init__(self, n_inputs):
        self.n_inputs = n_inputs
        self.weights = [random.random() for _ in range(n_inputs)]

    def activate(self, inputs):
        n = min(len(inputs), self.n_inputs)
        return sum(w * i for w, i in zip(self.weights[:n], inputs[:n]))

    def process(self, inputs):
        output = self.activate(inputs)
        random.seed(output)
        new_list = inputs.copy()
        random.shuffle(new_list)
        return new_list


neuron = Neuron(45)
input_list = numbers
g_numbers = neuron.process(input_list)
result_g = ''.join(map(str, g_numbers))
print(result_g)






