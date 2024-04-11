#Definindo várias como funções
def soma_um(numero):
    return numero + 1

    f1 = soma_um
    f1(1)

def soma_um(numero):
    def adiciona_um(numero):
        return numero +1
    return adiciona_um(numero)
soma_um(4)

#Passando funções como argumentos de outras funções
def soma_um(numero):
    return numero + 1

def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)
function_call(soma_um)

#FUnções retornando outras funções

def function_hi():
    def say_hi():
        return "Hi"
    return say_hi
hello = function_hi()
hello()
