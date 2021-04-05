# forward
# Qual a probabilidade de observar essa sequência 'observations'
# Dados os parâmetros do HMM informados
import hidden_markov
import numpy as np

states = ('s', 't')
possible_observation = ('A', 'B')
#  Numpy arrays of the data
start_probability = np.asmatrix([0.5, 0.5])

transition_probability = np.asmatrix([[0.6, 0.4], [0.3, 0.7]])
emission_probability = np.asmatrix([[0.3, 0.7], [0.4, 0.6]])
# Initialize class object
test = hidden_markov.hmm(states, possible_observation, start_probability, transition_probability, emission_probability)

observations = ('A', 'B', 'B', 'A')

print(test.forward_algo(observations))
print('{:.2f}%' .format(test.forward_algo(observations)*100))
