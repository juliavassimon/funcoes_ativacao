import numpy as np


#hyperbolic tanget - valores entre -1 e 1
def tanhFunction (soma):
    return (np.exp(soma) - np.exp(-soma))/ (np.exp(soma) + np.exp(-soma))
teste = tanhFunction(-0.358)

