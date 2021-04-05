# Cibele 4.3 a) lançamento de 3 moedas
# Qual a sequência de Estados mais provável para essa observação?
# Viterbi Algorithm

import hidden_markov
import numpy as np

# H = Cara ; T = Coroa
states = ('E1', 'E2', 'E3')
possible_observation = ('H', 'T')
start_prob = np.asmatrix([0.34, 0.33, 0.33])

transition_prob = np.asmatrix([[0.34, 0.33, 0.33],
                               [0.33, 0.34, 0.33],
                               [0.33, 0.33, 0.34]])

emission_prob = np.asmatrix([[0.50, 0.50],
                             [0.75, 0.25],
                             [0.25, 0.75]])

model = hidden_markov.hmm(states, possible_observation, start_prob,
                          transition_prob, emission_prob)

# CCCCĈCĈĈĈĈ
observation = ('H', 'H', 'H', 'H', 'T', 'H', 'T', 'T', 'T', 'T')

print('Sequência de estados mais provável para essa observação:\n'
      '\033[33m {} \033[m' .format(model.viterbi(observation)))

print('Probabilidade dessa sequência de observações dado que o estado é E1(?)\n'
      '{:.3f}%' .format(model.forward_algo(observation)*100))

# Acredito que o segundo print está errado
# como eu defino para a sequência de estado necessariamento ser E1E1E1E1...?


