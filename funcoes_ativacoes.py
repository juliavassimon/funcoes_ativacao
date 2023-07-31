import numpy as np

#criar uma função: faz as multiplicações dos pesos pelas entradas
    #transfer function
def stepFunction(soma):
    if(soma >=1 ):
          return 1   
       
    return 0 #se não entrar no if, retorna 0
    
teste = stepFunction(-1)
