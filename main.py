import math
from StateMachine import *


numbers_vocabulary = ["1","2","3","4","5","6","7","8","9","0","."]
operators_vocabulary = ["+","-","/","*","sin","cos","rot","exp"]
tokens = []
numbers = []
operators = []
special_symbols = []
results = []
identifiers = []
variables = {}
expressions = ""

def file_reader(filename):
    file = open(filename, "r")
    lines = file.read().split("\n")
    file.close()
    return [lines]

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
      if token[1] in variables:
        numbers.append(variables[token[1]])
        results.remove(variables[token[1]])
  calculate()

def calculate():
  if (len(operators) == 0):
    results.append(numbers[0])
    numbers.pop(0)
    set_variable()

  for operator in operators[::-1]:
    if operator == "+":
      calculation = float(numbers[0]) + float(numbers[1])
      remove(2)
    elif operator == "-":
      calculation = float(numbers[0]) - float(numbers[1])
      remove(2)
    elif operator == "*":
      calculation = float(numbers[0]) * float(numbers[1])
      remove(2)
    elif operator == "/":
      calculation = float(numbers[0]) / float(numbers[1])
      remove(2)
    elif operator == "exp":
      calculation = float(numbers[0])**float(numbers[1])
      remove(2)
    elif operator == "rot":
      calculation = float(numbers[0])**(1 / float(numbers[1]))
      remove(2)
    elif operator == "sin":
      calculation = math.sin(float(math.radians(float(numbers[0]))))
      remove(1)
    elif operator == "cos":
      calculation = math.cos(float(math.radians(float(numbers[0]))))
      remove(1)

    numbers.append(calculation)
    results.append(calculation)

    if "?" in special_symbols:
      refaz()
    if len(identifiers) != 0:
      set_variable()


def remove(n):
  for i in range(n):
    numbers.pop(0)
  operators.pop(0)

def refaz():
  for especial in special_symbols:
    if especial == "?":
      numbers.append(results[-1])

def set_variable():
  for identifier in identifiers:
    if identifier not in variables.keys():
      variables[identifier] = results[-1]

def set_initial_state(string):
    splitted_string = string.split(None, 1)[0]
    splitted_string = splitted_string.strip()
    if splitted_string in ["?", "(", ")"]:
        state = "INICIAL"
    else:
        state = "ERRO"
    return (state, splitted_string)

def set_number_state(string):
    splitted_string = string.split(None, 1)[0]
    splitted_string = splitted_string.strip()
    if splitted_string in numbers_vocabulary:
        state = "NUMERO"
    else:
        state = "ERRO"
    return (state, splitted_string)

def set_operator_state(string):
    splitted_string = string.split(None, 1)[0]
    splitted_string = splitted_string.strip()
    if splitted_string in operators_vocabulary:
        state = "OPERADORES"
    else:
        state = "ERRO"
    return (state, splitted_string)

def set_variable_state(string):
    if len(string) > 1:
      state = "VARIAVEL"
    else:
      state = "ERRO"
    return (state, string)

def clear():
  numbers.clear()
  tokens.clear()
  special_symbols.clear()

#file_reader("text1.txt")
if __name__ == '__main__':
    expressions = [['( op ( 3 )', '( 2 op + )']]
    #expressions = file_reader("text1.txt")
    
    final_state_machine = StateMachine()
    final_state_machine.add_state("INICIAL", set_initial_state, 1)
    final_state_machine.add_state("NUMERO", set_number_state, 1)
    final_state_machine.add_state("OPERADORES", set_operator_state ,1)
    final_state_machine.add_state("VARIAVEL", set_variable_state, 1)
    final_state_machine.set_start("INICIAL")
    for calculations in expressions:
      for calculation in calculations:
        for caracter in calculation.split():
          caracter = caracter.strip()
          final_state_machine.run(caracter)
        validate_tokens(final_state_machine.tokens)
        result_tokens = final_state_machine.tokens
        final_state_machine.tokens.clear()
    print("Resultado: ", "%.3f" % results[-1])
    clear()