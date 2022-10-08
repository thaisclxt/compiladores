# Enunciado

Escreva no campo de texto abaixo um código em lex/flex para classificar os lexemas nos seguintes tokens:

- DELIMITADOR ;
- ATRIBUICAO :=
- OPERADOR_RELACIONAL < > = <= >= <>
- OPERADOR_ARITMETICO + - \* /
- OPERADOR_LOGICO or and not
- PALAVRA_RESERVADA begin end for do if then else while dol
- TIPO_DADO integer real double char string boolean
- IDENTIFICADOR \_nome123 (palavras que começam com underline ou letra justaposta a uma sequência de letras, underline ou números)
- NUMERO_INTEIRO 123 (sequência de dígitos numéricos formando um número inteiro, positivo ou negativo)
- NUMERO_REAL 123.123 (sequência de dígitos numéricos formando um número real, positivo ou negativo)
- LITERAL "um texto" (uma sequência de alfanuméricos entre aspas)
- COMENTÁRIO # texto # (alfanuméricos delimitados por “#”)
- INVALIDO demais elementos não presentes nesta descrição
