import math
from MaquinaEstados import *

tokens = []
numbers = []
operators = []
special_symbols = []
results = []
identifiers = []
variaveis = {}
lexemas = []
expressions = ""

def validate_tokens(tokens):
  for token in tokens:
    if token[0] == "NUMERO":
      numbers.append(token[1])
    if token[0] == "OPERADORES":
      operators.append(token[1])
    if token[0] == "INICIAL":
      special_symbols.append(token[1])
    if token[0] == "RESULTADO":
      results.append(token[1])
    if token[0] == "VARIAVEL":
      identifiers.append(token[1])
      if token[1] in variaveis:
        numbers.append(variaveis[token[1]])
        results.remove(variaveis[token[1]])
  calculate()


def calculate():
  if (len(operators) == 0):
    results.append(numbers[0])
    numbers.pop(0)
    armazenarVar()

  for operator in operators[::-1]:
    if operator == "+":
      conta = float(numbers[0]) + float(numbers[1])
      remove(2)
    elif operator == "-":
      conta = float(numbers[0]) - float(numbers[1])
      remove(2)
    elif operator == "*":
      conta = float(numbers[0]) * float(numbers[1])
      remove(2)
    elif operator == "/":
      conta = float(numbers[0]) / float(numbers[1])
      remove(2)
    elif operator == "exp":
      conta = float(numbers[0])**float(numbers[1])
      remove(2)
    elif operator == "rot":
      conta = float(numbers[0])**(1 / float(numbers[1]))
      remove(2)
    elif operator == "sin":
      conta = math.sin(float(math.radians(float(numbers[0]))))
      remove(1)
    elif operator == "cos":
      conta = math.cos(float(math.radians(float(numbers[0]))))
      remove(1)

    numbers.append(conta)
    results.append(conta)

    if "?" in special_symbols:
        refaz()
    if len(identifiers) != 0:
      armazenarVar()


def refaz():
  for especial in special_symbols:
    if especial == "?":
      numbers.append(results[-1])


def remove(n):
  for i in range(n):
    numbers.pop(0)
  operators.pop(0)


def armazenarVar():
  for nome in identifiers:
    if nome not in variaveis.keys():
      variaveis[nome] = results[-1]

def inicial(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["?", "(", ")", ";"]:
        novoEstado = "INICIAL"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def numero(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["1","2","3","4","5","6","7","8","9","0","."]:
        novoEstado = "NUMERO"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def operation(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["+","-","/","*","sin","cos","rot","exp"]:
        novoEstado = "OPERADORES"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def identifier(string):
    if len(string) > 1:
      novoEstado = "VARIAVEL"
    else:
        novoEstado = "ERRO"
    return (novoEstado, string)




def limpa():
  numbers.clear()
  tokens.clear()
  special_symbols.clear()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas
  
if __name__ == '__main__':
    expressions = [['( op ( 1 )', '( 2 op + )']]

    fsm = MaquinaEstados()
    fsm.adicionarEstado("INICIAL", inicial, 1)
    fsm.adicionarEstado("NUMERO", numero, 1)
    fsm.adicionarEstado("OPERADORES", operation ,1)
    fsm.adicionarEstado("VARIAVEL", identifier, 1)
    fsm.setStart("INICIAL")
    for contas in expressions:
      for calculo in contas:
        for caractere in calculo.split():
          caractere = caractere.strip()
          fsm.rodar(caractere)
        validate_tokens(fsm.tokens)
        fsm.tokens.clear()
    print("Resultado: ", "%.3f" % results[-1])
    limpa()