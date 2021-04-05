# forward
# Cibele ex 2.1.1: Chuva ou não chuva

import hidden_markov
import numpy as np

# Chuva = A, não chuva = B
# Estados = Observações (simplificação)

states = ('A', 'B')
possible_observation = ('A', 'B')
# 40% de chance de chuva, 60% de não chuva
start_probability = np.asmatrix([0.4, 0.6])  # [length(states) X 1]
print(start_probability)
# Propondo alfa = 50% e beta = 80%
transition_probability = np.asmatrix([[0.5, 0.5], [0.8, 0.2]])  # [len(states) X len(states)]
emission_probability = np.asmatrix([[1, 0], [0, 1]])  # [len(states) X len(observations)]
# emission: probabilidade de estarmos no estado x, dado que observamos o dado y
test = hidden_markov.hmm(states, possible_observation, start_probability, transition_probability, emission_probability)

observations1 = ('A', 'A', 'B', 'A', 'A')
observations2 = ('B', 'B', 'A', 'A', 'A')

print('Probabilidade sequência {}\n'
      '{:.2f}%' .format(observations1, test.forward_algo(observations1)*100))
print('Probabilidade sequência {}\n'
      '{:.2f}%' .format(observations2, test.forward_algo(observations2)*100))


