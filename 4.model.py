import numpy as np
import pandas as pd
from hmmlearn import hmm

from hmmlearn.hmm import MultinomialHMM

np.random.seed(42)

df = pd.read_csv('obs_covid.csv')


model = hmm.MultinomialHMM(n_components=2, startprob_prior =1.0,transmat_prior =1.0,
                           algorithm='viterbi',random_state=None,n_iter=1000,tol=0.01,
                           verbose=False,params='ste',init_params=' ')

# params = ste = state, transmission, emission

model.startprob_ = np.array([1/2, 1/2]) # 

model.transmat_ = np.array([[2/3, 1/3], 
                            [1/3, 2/3]])

model.emissionprob_ = np.array([[3/3, 2/6, 1/6],
                                [1/6, 2/6, 3/6]])

Obs_sim1, Est_sim1 = model.sample(len(df),random_state=None) # faz uma simulação pelo dados inseridos

P1 = np.array([[df['observation_14'][i]] for i in range(0, int(len(df)/2))]) 
P2 = np.array([[df['observation_14'][i]] for i in range(int(len(df)/2), len(df))])

X = np.concatenate([P1, P2])
lengths = [len(P1), len(P2)]

log_modelo_inicial = model.score(X) 


import pickle
with open("modelo_inicial.pkl", "wb") as file: pickle.dump(model, file)
                               
model_opt = model.fit(X, lengths) # modelo otimizado

Obs_sim2, Est_sim2 = model_opt.sample(len(df),random_state=None)

#score after optimization
log_modelo_opt = model_opt.score(X)

# print(log_modelo_opt)

model_opt.decode(X, lengths, algorithm='viterbi')

with open("modelo_otimizado.pkl", "wb") as file: pickle.dump(model_opt, file)

np.random.seed(42)

print('\nMatrizes otimizadas\n\n')
print(f'{model_opt.transmat_}\n\n')
print(f'{model_opt.emissionprob_}\n\n')
print(f'{model_opt.startprob_}')

# criando um novo modelo 'comparativo' 

remodel = hmm.MultinomialHMM(n_components=2, n_iter=10) 
remodel.fit(X)

#score after optimization
log_remodelo = remodel.score(X)

print(f'SCORE INICIAL: {log_modelo_inicial}')
print(f'\nSCORE OTIMIZADO: {log_remodelo}')

with open("modelo_otimizado_2.pkl", "wb") as file: pickle.dump(remodel, file)

# 1. Fazer mais testes ---> Melhor otimização possível
# 2. Com a matrizes iniciais... aplicar simulações
# 3. Comparar por meio de boxplot com óbitos diários
# 4. Gerar boxplot sim1 e sim2 ----> Qual está mais próximo do real??

# (Futuro) Utilizando os estados Est_sim1 --> Utilizar algoritmo de viterbi...
a = model_opt.decode(X, lengths, algorithm='viterbi')

viterbi_list = pd.DataFrame(a[1])

viterbi_list.to_csv('viterbi_list.csv', index = None)


deaths = np.array([[df['new_deaths'][i]] for i in range(0, len(df) - 1)]) 

df_obs2 = pd.DataFrame(Obs_sim2, columns = ['observation'])
df_obs2['deaths'] = np.array([[df['new_deaths'][i]] for i in range(0, len(df))]) 
df_obs2.to_csv('obs_sim2.csv', index = None)

df_obs1 = pd.DataFrame(Obs_sim1, columns = ['observation'])
df_obs1['deaths'] = np.array([[df['new_deaths'][i]] for i in range(0, len(df))]) 
df_obs1.to_csv('obs_sim1.csv', index = None)

