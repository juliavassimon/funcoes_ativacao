import numpy as np

#ReLU - valores entre 0 e sem maximo.
def reluFunction(soma):
    if(soma>=0):
        return soma
    return  0
teste = reluFunction(10)
