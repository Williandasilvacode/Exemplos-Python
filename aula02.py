
############ Valores Booleanos #########


#Você pode avaliar qualquer expressão em python e obter uma de duas respostas, 'True' ou 'False'.

# Exemplo:
"""
print (10 > 9)
print (10 == 9)
print (10 < 9)
"""
# Quando voce executa uma condição em uma instrução 'if', o python retorna True ou Falso:

#Exemplo:

# Imprima uma mensagem com base em se a condição é True ou False:

"""
a = 200
b = 33
if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")    
"""

############# Avalie Valores e Variáveis ########

# A bool() função permite que voce avalie qualquer valor e de a voce 'True' ou 'False' em troca.

# Exemplo:
# Avalie uma string e um número:
"""
print(bool("hello"))
print(bool(15))
"""

# Exemplo:
# Avalie duas variáveis:
"""
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""

######## A maioria dos valores são verdadeiros ############

#Exemplo

# O seguinte retornará Verdadeiro:
"""
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
"""

############ Alguns Valores são Falsos ##########

# Exemplo:
# O seguinte retornará False:
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""

# Mais um valor, ou objeto neste caso, é avaliado 'False', e isto é, se voce tiver um objeto que é feito de uma classe com uma _len_ função que retorna 0 ou False:

# Exemplo:
"""
class myclass():
    def _len_(self):
        return 0
myobj = myclass ()
print(bool (myobj))        
"""

######## Funções podem retornar um booleano #######

# Voce pode criar funções que retornam um valor booleano;

# Exemplo

#Imprima a resposta de uma função:

"""
def myFunction():
    return True
print(myFunction())
"""
# Voce pode executar o código com base na resposta booleana de uma função:

# Exemplo:

#Imprima "SIM!" se a função retornar True, caso contrário imprima "Não":
'''
def myFunction():
    return True
if myFunction():
    print("SIM!")
else:
    print("NÃO!")
'''
# Python também tem muitos funções integradas que retornam um valor booleano, como a 'isinstance()' função, que pode ser usada para determinar se um objeto é de um determinado tipo de dados:

# Exemplo:

# Verifique se um objeto é um número interio ou não:

"""
x = 200
print(isinstance(x, int))
"""



