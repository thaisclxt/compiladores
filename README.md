# Compiladores

Repositório para a disciplina de Compiladores 2022.2 contendo os trabalhos de análise léxica e sintática

## Organização das pastas

O repositório está organizado da seguinte forma:

### `tarefa-lex`

Atividade para classificar lexemas. \
Você encontra o enunciado em `/enunciado.md`

Para compilar, vá até a pasta `tarefa-lex` e execute os seguintes comandos:

```shell
lex tarefa.l
gcc lex.yy.c -o tarefa -ll
./tarefa
```

### `regex-expression`

Trabalho para criar um compilador que faz a análise léxica de expressões regulates

Para isso, teremos que:

1. Converter expressões regulares na forma infixa para a forma posfixa, ou polonesa reversa. Considerando:

   - O símbolo ‘ + ’ como operador binário de união (menor precedência);

   - O símbolo ‘ . ’ como operador binário de concatenação;

   - O símbolo ‘ \* ’ como operador unário de fecho de Kleene (maior precedência);

   - O símbolo ‘&’ para representar a palavra vazia;

   - O operador de concatenação pode estar implícito ou explicito na expressão regular de entrada na forma infixa;

   - O operador de concatenação deverá estar explicito na expressão regular de saída na forma posfixa;

   **Observação:** os símbolos diferentes de operandos contidos na expressão regular +, \*, ., (, ) ficarão inutilizados como entrada no analisador léxico. Para não inutilizá-los, é comum o uso o símbolo ‘\’ como literal, ou seja, o símbolo que vier na sequência de ‘\’ será obrigatoriamente operando, o que inclui ele próprio.

2. Construir um AFN-ɛ (Autômato Finito Não-determinístico com Movimento Vazio) a partir de expressão regular na forma posfixa, oriundas do tópico 1.

   **Observação:** utilizar o algoritmo de Thompson.

3. Construir um AFD (Autômato Finito Determinístico) a partir de um AFN-ɛ (Autômato Finito Não-determinístico com Movimento Vazio), oriundo do tópico 2.

4. Gerar um Analisador Léxico automático a partir de AFDs (Autômatos Finitos Determinísticos), oriundos do tópico 3.
