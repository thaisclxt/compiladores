# Enunciado

Implementar computacionalmente, um programa que converta expressões regulares na forma infixa, fornecidas pelo usuário, em expressões regulares na forma posfixa, ou polonesa reversa. Para isso, você deve utilizar os algoritmos apresentados em unidade. Considere ainda:

- O símbolo ‘ + ’ como operador binário de união (menor precedência);

- O símbolo ‘ . ’ como operador binário de concatenação;

- O símbolo ‘ \* ’ como operador unário de fecho de Kleene (maior precedência);

- O símbolo ‘&’ para representar a palavra vazia;

- O operador de concatenação pode estar implícito ou explicito na expressão regular de entrada na forma infixa;

- O operador de concatenação deverá estar explicito na expressão regular de saída na forma posfixa;

**Observação:** os símbolos diferentes de operandos contidos na expressão regular +, \*, ., (, ) ficarão inutilizados como entrada no analisador léxico. Para não inutilizá-los, é comum o uso o símbolo ‘\’ como literal, ou seja, o símbolo que vier na sequência de ‘\’ será obrigatoriamente operando, o que inclui ele próprio.
