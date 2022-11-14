# Jasmini Rebecca Gomes dos Santos
'''
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação Python, C++, C, que seja capaz de validar e executar programas escritos na 
linguagem  proposta  a  seguir  emitindo  um  relatório  de  análise  léxica,  a  classificação  como  válida  ou 
invalida para cada declaração da linguagem e o resultado do programa.   
Descrição da linguagem  
Identificadores: compostos apenas de letras minúsculas e números;  
Símbolos especiais: ?, ), (;  
Operações:  soma  (+),  subtração  (-),  multiplicação  (*),  divisão  (/),  seno  (sin),  cosseno  (cos), 
exponenciação (exp), raiz (rot) segundo os seguintes exemplos:  
(3 4 +) representa a soma de 3 e 4 e devolve 7.000;  
  (3.4 2.5 -) representa a subtração entre 3,6 e 2,5 e devolve 1.100;  
(2.5 3 *) representa o produto de 2,5 por 3 e devolve 7.500;   
(2.6 2 /) representa a divisão de 2,6 por 2 e devolve 1.300;  
   (sin 30) representa o seno de 30 graus e devolve 0.500;  
   (cos 30) representa o cosseno de 30 graus e devolve 0.866;  
   (exp 3 2) representa 3 elevado a 2 e devolve 9.000;  
   (rot 81 2) representa a raiz quadrada de 81 e devolve 9.000;  
Observe  que  todos  os  números  são  reais  de  precisão  dupla  e  todos  os  resultados  serão 
truncados na terceira casa depois da vírgula.  
O símbolo especial será usado para passar o resultado de uma linha para a linha seguinte. Assim, 
um arquivo contendo as declarações a seguir:   
(3 4 +)  
(2 ? *)  
Deverá  devolver  como  reposta  14  além da  validação  de todos  os  lexemas  e da  validação  das 
declarações. Para o exemplo acima, a saída deverá ser:   
Linha 1: lexemas: (, 3, 4, +,) todos válidos  
Linha 1: sintaxe: correta  
Linha 2: lexemas: (, 2, ?, ) todos válidos  
Linha 2: sintaxe: correta  
Além  disso,  poderemos  usar  indentificadores  e  ainhamento.  Então  para  criar  uma  variável  e 
armazenar um valor usaremos a sentença:   
(teste (2 3 *))   
Neste exemplo foi criada a variável teste e esta variável irá armazenar o valor 6.000.   
Um programa completo poderia ser escrito como:   
(op1 15)  
(op2 2)  
(sin (op1 op2 *) ) 
(3 ? *)  
Neste exemplo o resultado será 1.500.  
Considerações  importantes:  para  testar  seu  programa,  você  deverá  enviar  três  arquivos 
contendo  programas  com  6  ou  mais  declarações  que  usem  todas  as  operações  descritas  com  pelo 
menos dois aninhamento de operações em cada arquivo de testes e com, no mínimo uma variável em 
cada arquivo de testes.   
Os testes devem ser capazes de indicar o comportamento do seu programa caso o código criado 
contenha erros léxicos ou sintáticos.  
Para a realização da validação léxica você deverá simular, em código, uma máquina de estados 
finitos e não poderá utilizar nenhuma expressão regular.   
Para  a  realização  da  validação  sintática  você  pode  usar  um  parser  LL1  ou  criar  o  seu  próprio 
código de validação de declarações. 
'''

import math
from StateMachine import *
from string import ascii_lowercase

alphabet = list(ascii_lowercase)
numbers_vocabulary = ["1","2","3","4","5","6","7","8","9","0","."]
operators_vocabulary = ["+","-","/","*","sin","cos","rot","exp"]
tokens = []
numbers = []
operators = []
special_symbols = []
results = []
identifiers = []
variables = {}
all_lexemes = []

def file_reader(filename):
    file = open(filename, "r")
    lines = file.read().split("\n")
    file.close()
    return lines
  
def check_number(s):
  return s.replace('.','',1).isdigit()

def check_identifier(identifier):
  for character in identifier:
    if character not in alphabet and character not in numbers_vocabulary:
      return False
  if check_number(identifier):
    return False  
  return True

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
        if variables[token[1]] in results:
          results.remove(variables[token[1]])
  calculate()

def calculate():
  if (len(operators) == 0) and len(numbers) > 0:
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
      redo()
    if len(identifiers) != 0:
      set_variable()


def remove(n):
  for i in range(n):
    numbers.pop(0)
  operators.pop(0)

def redo():
  for special in special_symbols:
    if special == "?":
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
    if check_number(splitted_string):
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
    if check_identifier(string):
      state = "VARIAVEL"
    else:
      state = "ERRO"
    return (state, string)

def clear():
  numbers.clear()
  tokens.clear()
  special_symbols.clear()

def get_lexemes(tokens):
  lexemes = []
  for token in tokens:
    lexemes.append(token[1])
  return lexemes

def format_result(lexemes):
  result_text = ""
  for i in range(len(lexemes)):
    result_text = "Linha", i + 1, ": lexemas: "
    for j in range(len(lexemes[i])):
      if j != len(lexemes[i]) - 1:
        result_text = result_text + str(lexemes[i][j]) + ","
      else:
        result_text = result_text + str(lexemes[i][j]) + " todos válidos"
    print(result_text)
    print("Linha", i + 1, "sintaxe: correta")
    print("Resultado: ", "%.3f" % results[i])
        
def run_final_state_machine(expressions):
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
      all_lexemes.append(get_lexemes(result_tokens))
      final_state_machine.tokens.clear()
  #format_result(all_lexemes)
    print("Resultado: ", "%.3f" % results[-1])
  clear()
  
if __name__ == '__main__':
    expressions = []
    expressions.append(file_reader("text1.txt"))
    expressions.append(file_reader("text2.txt"))
    expressions.append(file_reader("text3.txt"))
    run_final_state_machine(expressions)