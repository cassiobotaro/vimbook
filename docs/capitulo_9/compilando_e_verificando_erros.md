Compilando e verificando erros
------------------------------

Se o seu projeto já possui um Makefile, então você pode
fazer uso do comando :make para poder compilar seus
programas no conforto de seu Vim:
```
:make
```
A vantagem de fazer isso é poder usar outra ferramenta bastante
interessante, a janela de *quickfix*:
```
:cw[indow]
```
O comando cwindow abrirá uma janela em um
*split* horizontal com a listagem de erros e
*warnings*. Você poderá navegar pela lista usando os
cursores e ir diretamente para o arquivo e linha da ocorrência.

Modificando o compilador, o comando make pode mudar sua
ação.
```
:compiler javac
:compiler gcc
:compiler php
```
Note que *php* não tem um compilador. Logo, quando
executado, o make irá verificar por erros de sintaxes.
```
:compiler
```
O comando acima lista todos os compiladores suportados.
