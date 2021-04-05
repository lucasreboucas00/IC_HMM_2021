# forward; Cibele 2.1.2;
import hidden_markov
import numpy as np

# chuvoso, nublado, ensolarado
states = ('C', 'N', 'E')
possible_observation = ('C', 'N', 'E')

start_probability = np.asmatrix([0, 0, 1])

transition_probability = np.asmatrix([[0.4, 0.3, 0.3],
                                      [0.2, 0.6, 0.2],
                                      [0.1, 0.1, 0.8]])

emission_probability = np.asmatrix([[1, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 1]])

test = hidden_markov.hmm(states, possible_observation, start_probability, transition_probability, emission_probability)

# sol-sol-chuva-chuva-sol-nublado-sol
# 7 dias + Dia Xo == 'E'
observations = ('E', 'E', 'E', 'C', 'C', 'E', 'N', 'E')

print('Probabilidade da sequência \033[1:33msol-sol-chuva-chuva-sol-nublado-sol \033[m')
print('{:.2f}%' .format(test.forward_algo(observations)*100))
print('{:.8f}' .format(test.forward_algo(observations)))