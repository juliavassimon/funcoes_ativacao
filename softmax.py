import numpy as np 

#Softmax - conjunto de valores (vetor)
def softmaxFunction(x):
    ex = np.exp(x) #se for 5 valores, vai retornar 5 valores
    return ex/ex.sum() #já faz o somatorio 
valores = [5.0, 2.0, 1.3] #valor de saida, precisa associar a probabilidade 
print(softmaxFunction(valores))

