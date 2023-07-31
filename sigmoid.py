import numpy as np

#sigmoid - valores entre 0 e 1
def sigmoidFunction(soma):
    return 1/(1+np.exp(-soma))


teste = sigmoidFunction(30)
