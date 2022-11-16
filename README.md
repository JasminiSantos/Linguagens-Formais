# Linguagens Formais
<p> Jasmini Rebecca Gomes dos Santos</p>
<p> Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação Python, C++, C, que seja capaz de validar e executar programas escritos na 
linguagem  proposta  a  seguir  emitindo  um  relatório  de  análise  léxica,  a  classificação  como  válida  ou 
invalida para cada declaração da linguagem e o resultado do programa. </p>
<p>Descrição da linguagem </p>
<p>Identificadores: compostos apenas de letras minúsculas e números; </p>
<p> Símbolos especiais: ?, ), (;  
<p> Operações:  soma  (+),  subtração  (-),  multiplicação  (*),  divisão  (/),  seno  (sin),  cosseno  (cos), 
exponenciação (exp), raiz (rot) segundo os seguintes exemplos: </p>
<p> (3 4 +) representa a soma de 3 e 4 e devolve 7.000;  </p>
<p> (3.4 2.5 -) representa a subtração entre 3,6 e 2,5 e devolve 1.100;  </p>
<p> (2.5 3 *) representa o produto de 2,5 por 3 e devolve 7.500; </p>
<p> (2.6 2 /) representa a divisão de 2,6 por 2 e devolve 1.300; </p> 
<p> (sin 30) representa o seno de 30 graus e devolve 0.500;  </p> 
<p> (cos 30) representa o cosseno de 30 graus e devolve 0.866;  </p> 
<p> (exp 3 2) representa 3 elevado a 2 e devolve 9.000; </p> 
<p> (rot 81 2) representa a raiz quadrada de 81 e devolve 9.000; </p> 
<p> Observe  que  todos  os  números  são  reais  de  precisão  dupla  e  todos  os  resultados  serão 
truncados na terceira casa depois da vírgula. </p> 
<p> O símbolo especial será usado para passar o resultado de uma linha para a linha seguinte. Assim, 
um arquivo contendo as declarações a seguir: </p>  
<p>(3 4 +) </p>
<p>(2 ? *) </p> 
<p> Deverá  devolver  como  reposta  14  além da  validação  de todos  os  lexemas  e da  validação  das 
declarções. Para o exemplo acima, a saída deverá ser: </p>   
<p>Linha 1: lexemas: (, 3, 4, +,) todos válidos </p>
<p>Linha 1: sintaxe: correta </p>
<p>Linha 2: lexemas: (, 2, ?, ) todos válidos </p> 
<p>Linha 2: sitaxe: correta </p>
<p>Além  disso,  poderemos  usar  indentificadores  e  ainhamento.  Então  para  criar  uma  variável  e 
armazenar um valor usaremos a sentença: </p>
<p>(teste (2 3 *)) </p> 
<p>Neste exemplo foi criada a variável teste e esta variável irá armazenar o valor 6.000.   
Um programa completo poderia ser escrito como: </p> 
  
<p>(op1 15)</p>  
<p>(op2 2) </p> 
<p>(sin (op1 op2 *) </p> 
<p>(3 ? *) </p>
<p>Neste exemplo o resultado será 1.500.  
Considerações  importantes:  para  testar  seu  programa,  você  deverá  enviar  três  arquivos 
contendo  programas  com  6  ou  mais  declarações  que  usem  todas  as  operações  descritas  com  pelo 
menos dois aninhamento de operações em cada arquivo de testes e com, no mínimo uma variável em 
cada arquivo de testes. </p> 
<p>Os testes devem ser capazes de indicar o comportamento do seu programa caso o código criado 
contenha erros léxicos ou sintáticos. </p> 
<p>Para a realização da validação léxica você deverá simular, em código, uma máquina de estados 
finitos e não poderá utilizar nenhuma expressão regular.</p>    
<p>Para  a  realização  da  validação  sintática  você  pode  usar  um  parser  LL1  ou  criar  o  seu  próprio 
código de validação de declarações.</p>

<a href="https://replit.com/@JasminiSantos/Linguagens-Formais#main.py">Link para o projeto</a>
