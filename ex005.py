# Cibele 4.3 c) e se mudássemos a matriz de transição?
# Qual a sequência de Estados mais provável para essa observação?
# Viterbi Algorithm

import hidden_markov
import numpy as np

# H = Cara ; T = Coroa
states = ('E1', 'E2', 'E3')
possible_observation = ('H', 'T')
start_prob = np.asmatrix([0.34, 0.33, 0.33])

transition_prob = np.asmatrix([[0.90, 0.05, 0.05],
                               [0.45, 0.10, 0.45],
                               [0.45, 0.45, 0.10]])

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

# probabilidade da observação estar associdada à sequência de estados E1 x 8

