%{
#include<stdio.h>
#include<stdlib.h>
%}

NUM [0-9]
LETRA [a-zA-Z_]
FRACAO \.{NUM}+
ALPHANUM ({NUM}|{LETRA})
TEXTO ({ALPHANUM}|[ ])

%%

\;                      {printf("<DELIMITADOR> ");}
\:\=                    {printf("<ATRIBUICAO> ");}
\<                      {printf("<OPERADOR_RELACIONAL> ");}
\>                      {printf("<OPERADOR_RELACIONAL> ");}
\=                      {printf("<OPERADOR_RELACIONAL> ");}
\<\=                    {printf("<OPERADOR_RELACIONAL> ");}
\>\=                    {printf("<OPERADOR_RELACIONAL> ");}
\<\>                    {printf("<OPERADOR_RELACIONAL> ");}
\+                      {printf("<OPERADOR_ARITMETICO> ");}
\-                      {printf("<OPERADOR_ARITMETICO> ");}
\*                      {printf("<OPERADOR_ARITMETICO> ");}
\/                      {printf("<OPERADOR_ARITMETICO> ");}
\[{NUM}+\]		{printf("<INDEX> ");}
\[			{printf("<COLCHETE> ");}
\]			{printf("<COLCHETE> ");}
or                      {printf("<OPERADOR_LOGICO> ");}
and                     {printf("<OPERADOR_LOGICO> ");}
not                     {printf("<OPERADOR_LOGICO> ");}
begin                   {printf("<PALAVRA_RESERVADA> ");}
end                     {printf("<PALAVRA_RESERVADA> ");}
for                     {printf("<PALAVRA_RESERVADA> ");}
do                      {printf("<PALAVRA_RESERVADA> ");}
if                      {printf("<PALAVRA_RESERVADA> ");}
then                    {printf("<PALAVRA_RESERVADA> ");}
else                    {printf("<PALAVRA_RESERVADA> ");}
while                   {printf("<PALAVRA_RESERVADA> ");}
dol                     {printf("<PALAVRA_RESERVADA> ");}
integer                 {printf("<TIPO_DADO> ");}
real                    {printf("<TIPO_DADO> ");}
double                  {printf("<TIPO_DADO> ");}
char                    {printf("<TIPO_DADO> ");}
string                  {printf("<TIPO_DADO> ");}
boolean                 {printf("<TIPO_DADO> ");}
{LETRA}{ALPHANUM}+      {printf("<IDENTIFICADOR> ");}
[+-]?{NUM}+             {printf("<NUMERO_INTEIRO> ");}
[+-]?{NUM}+{FRACAO}     {printf("<NUMERO_REAL> ");}
\"{TEXTO}+\"            {printf("<LITERAL> ");}
#{TEXTO}+#              {printf("<COMENTARIO> ");}
.                       {printf("<INVALIDO> ");}

%%

int main() {
    system("clear");
    printf("Entre o código fonte:\n");
    yylex();
    return 1;
}

