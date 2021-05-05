#print('hello word')

"""
Isto é um comentario
ecrito em
varias linhas
"""

                        ######### Variável ##########
"""
Exemplo de Variável
x = 5
y = "John"
print( x )
print( y )
"""
#Tipo específico de variável
"""
x = 4
x = "Sally"
print( x )
"""
#Casting
"""
Se você deseja especificar o tipo de dados de uma variável, isso pode ser feito com o casting.

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
"""
#Obtenha o tipo de Classe
"""
x = 5
y = "John"
print (type (x))
print (type (y))
"""
#aspas simples ou duplas? tanto faz, o resultado será o mesmo.
"""
x = "John"
y = 'John'
print(x)
print(y)
"""
#Maiúsculas e Minúsculas
"""
a = 4
A = "Sally"
print(a)
print(A)
"""
#Nomes de variáveis legais:
"""
myvar ="John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR ="John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
"""
#Muitos Valores p/ Variáveis Multiplas
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
#Um valor p/ Múltiplas variaveis

#Exemple 01
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""

#Exemplo 02
"""
x = y = z = "Orange"
print((x),(y),(z))
"""
#Descompactação
#Descompacte uma lista
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print((x), (y), (z))
"""
                        ######### Variáveis de saída ##########

#Exemplo 01
"""
x = "Mundo! "
print("Olá, " + x)
"""
#Exemplo 02
"""
x = "Olá, "
y = "Mundo!"
z = x + y
print(z)
"""
#Para números, o + funciona como operador matemático.

#Exemplo:
"""
x =5
y =10
print(x + y)
"""
                 ########### Variáveis globais. ###############

#Exemplos 01:

# Crie uma variável fora de uma função e use-a dentro da função.
"""
x = "Mundo! "
def myfunc():
     print("olá, " + x)

myfunc()
"""
#Exemplo 02:

#Crie uma variável dentro da função, com o mesmo nome da variável global:
"""
x = "Mundo!"
def myfunc():
    x = "Fantastico"
    print("Mundo!, " + x)

myfunc()
print("Olá, " + x)
"""
            ############# Palavra-chave Global ######

#Exemplo 01
# Se você usar a golbal plavra-chave, a variável pertence ao escopo global:          
"""          
def myfunc():
    global x
    x = "Mundo!"
myfunc()
print("Olá, " + x)
"""
#Exemplo 02
#Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a global palavra-chave:
"""
x = " Olá, Mundo!"

def myfunc():
    global x
    x = "fantastic "

myfunc()

print("python é " + x)
"""
############ Obtendo o tipo de dados  ##########

#Exemplo:
#Imprima o tipo de dados da variável x:
"""
x = 5
print(type(x))
"""

############## Definir o tipo de dados #########

#Em python, o tipo de dados é definido quando você atribui um valor a uma variável.

#Exemplos:
"""
x = "Hello world!"
print(x)
print(type (x))
"""
"""
x =20
print(x)
print(type(x))
"""
"""
x = 20.5
print(x)
print(type(x))
"""
"""
x = 1j
print(x)
print(type(x))
"""
"""
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
"""
"""
x = ("apple", "banana", "cherry")
print(x)
print(type(x))
"""
"""
x = range(6)
print(x)
print(type(x))
"""
"""
x = {"nome" : "John", "idade" : 36}
print(x)
print(type(x))
"""
"""
x= frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
"""
"""
x = True
print(x)
print(type(x))
"""
"""
x = b"Hello"
print(x)
print(type(x))
"""
"""
x= bytearray(5)
print(x)
print(type(x))
"""
"""
x= memoryview(bytes(5))
print(x)
print(type(x))
"""
##### Configurando o Tipo de Dados Específico ####

# Se você deseja especificar o tipo de dados, pode usar as seguintes funções de construtor:
"""
x = str("Hello World!")
print(x)
print(type(x))
"""
"""
x= int(20)
print(x)
print(type(x))
"""
"""
x = float(20.5)
print(x)
print(type(x))
"""
"""
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))
"""
"""
x = bool(5)
print(x)
print(type(x))
"""
############## Números Python ##########

#Existem três tipos numéricos em Python:
"""
      # int
      # float
      # complex
"""
#Exemplo:
"""
x= 1     int
y = 2.8  float
z = 1j   complex
"""

# Para verificar o tipo de qualquer objeto em python, use a type() função:

#Exemplo:
"""
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
"""
############## Conversão de Tipo #############
#Exemplo:
"""
x = 1    # int
y = 2.8  #float
z = 1j   #complex

a = float (x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""
########### As strings em python são colocadas entre aspas simples ou aspas duplas. #########

# Exemplo:
"""
print("hello, World!")
print('hello, World!')
"""
########## Atribuir String a uma variável #######

#Exemplo:
"""
a = 'Hello, World!'
print(a)
"""

########### Multiline Strings #############

#Exemplo:
# Você pode usar três aspas duplas:


# a = """Lorem ipsum dolor sit amet,
#  consectetur adipiscing elit,
#  sed do eiusmod tempor incididunt
#  ut labore et dolore magna aliqua."""

#  print(a)

# Ou três aspas simples
#Exemplo:
"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)
"""
########### Looping através de uma string ######
#Exemplo:
#Faça um loop pelas letras da palavra "banana":
"""
for x in "banana":
  print(x)
"""
########### Comprimento da String ##########

#Para obter o comprimento de uma string, use a len() função.

#Exemplo:
# A len() função retorna o comprimento de uma string.
"""
a = 'Hello, world!'
print(len(a))
"""

############# Verificar String #############

# Para verificar se uma determinda frase ou caractere está presente em uma string, podemos usar a palavra-chave in.

#Exemplo:

# Verifique se "free" está presente no seguinte texto:
"""
txt = "The best things in life are free!"
print("free" in txt)
"""
# Use-o em uma if declaração:

#Exemplo:
# Imprima apenas se "free" estever presente:
"""
txt = "The best things in life are free!"
if "free" in txt:
    print("Sim, 'free' está presente.")
"""


############ Verifique se Não #############
"""
Para verifica se uma determinada frase ou caractere NÃO está presente em uma string, podemos usar a palavra-chave (not in).
"""
#Exemplo:

#Verifique se "caro" NÃO está presente no sequinte texto:
"""
txt = "As melhores coisas da vida são de graça!"
print("caro" not in txt)
"""
# Use-o em uma if declaração:

#Exemplo:
#Imprimir apenas se "caro" não estive presente:
"""
txt = "As melhores coisas da vida são de graça!"
if "caro" not in txt:
    print("sim, 'caro' não está presente.")
"""

############# Fatiar String ##############

# Exemplo:
# Obtenha os caracteres de posição 2 à posição 5  (não incluido):
"""
b = 'hello, World!'
print(b[ :0])
"""
# Nota: O primeiro caractere tem índice 0.

########### Fatia desde o início #############

# Ao omitir o índice inicial, o intervalo começará no primeiro caractere.

# Exemplo:
# Obtenha os personagens do início até a posição 5 (não incluído):
"""
b = 'hello, world!'
print(b[:5])
"""

########### Fatia até o fim ############

#ao omitir o índice final, o intervalo irá para o final:

# Exemplo:

# Pegue os personagens da posição 2 e todo o caminho até o final:
"""
b = 'Hello, World!'
print(b[2:])
"""

############# Indexação Negativa ########

# Use índeces negativos para iniciar a fatia do final da string:

#Exemplo:

#Obtenha os personagens:
#De: "o" em "world!" (posição -5)
#Para, mas não incluído: "d" em "world!" (posição -2):
"""
b = 'Hello, World!'
print(b[-5:-2])
"""

########## Modificar Strings ##########

#Maiúsculas:

#Exemplo:

# O upper() método retorna a string em maiúsculas:
"""
a = 'hello, world!'
print(a)
print(a.upper())
"""

#Minúsculas

# O lower() método retorna a string em letras minúsculas:

#Exemplo:
"""
a = 'Hello, World!'
print(a)
print(a.lower())
"""

############ Remover espaço em branco ############

# O strip() método remove qualquer espaço em branco do início ou do final:

#Exemplo:

"""
a = '  Hello, World!'
print(a)
print(a.strip())
"""

########### Substituir String ##############

# O replace() método substitui uma string por outra string:

#Exemplo:
"""
a = 'Hello, World!'
print(a)
print(a.replace("H", "J"))
"""

############ Dividir String #########

# O split() método retorna uma lista onde o texto entre o separador especificado se trona os itens da lista.

#Exemplo:

"""
a = "Hello, World!"
print(a)
print(a.split(","))
"""

################ String Concatenation ############

# Para concatenar ou combinar duas string, você pode usar o operador +.

# Mesclar variável 'a' com variável 'b' na variável 'c':

#Exemplo:
"""
a = 'Hello'
b = 'World!'
c = a + b
print(c)
"""
# Para adicionar um espaço entre eles, adione um " ":

#Exemplo:
"""
a = 'Hello'
b = 'World'
c = a + " " + b
print(c)
"""

############ Formato de String ###########

# Não podemos combinar strings e números como este:

#Exemplo:
"""
idade = 36
txt = 'My name is john, I am' + idade
print(txt)
"""

# Mas podemos combinar string e números usando o format() método!

# O format () método pega os argumentos passados, os formata e os coloca na string onde os marcadores são: {}.

#Exemplo:

# Use o format() método para inserir números em strings:
"""
idade = 27
txt = 'My name is willian, and I am {}'
print(txt.format(idade))
"""

# O método format() aceita um número ilimitado de argumentos e são colocados nos respectivos marcadores de posição:

#Exemplo:
"""
quantidade = 3
item = 567
preço = 49.95
myorder = "Eu quero {} peças do item {} por {} dollares."
print(myorder.format(quantidade, item, preço))
"""

# Você pode usar números de índice {0} para garantir que os argumentos sejam colocados nos marcadores de posição corretos:

#Exemplo:
"""
quantidade = 3
item = 567
preço = 49.95
meupedido = "Eu quero pagar {2} dólares por {0} peças do item {1}."

print(meupedido.format(quantidade, item, preço))
"""

############ Caracteres de Escape #############

# O caractere de escape permite que você use aspas duplas quando não seria permitido.

#Exemplo:
"""
txt = "Nós somos os chamados \"Vikings\" do norte."
print(txt)
"""


