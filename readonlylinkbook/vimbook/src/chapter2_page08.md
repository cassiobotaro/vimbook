Edição avançada de linhas
-------------------------

Seja o seguinte texto:
```
1  este é um texto novo
2  este é um texto novo
3  este é um texto novo
4  este é um texto novo
5  este é um texto novo
6  este é um texto novo
7  este é um texto novo
8  este é um texto novo
9  este é um texto novo
10 este é um texto novo
```
Suponha que queira-se apagar `é um texto` da linha 5 até o
fim (linha 10). Isto pode ser feito assim:
```
:5,$ normal 0wd3w
```
Explicando o comando acima:
```
:5,$ .... indica o intervalo que é da linha 5 até o fim '$'
normal .. executa em modo normal
0 ....... move o cursor para o começo da linha
w ....... pula uma palavra
d3w ..... apaga 3 palavras 'w'
```
Obs: É claro que um comando de substituição simples
```
:5,$s/é um texto//g
```
Resolveria neste caso, mas a vantagem do método anterior é que é válido
para três palavras, sejam quais forem. Também é possível empregar
comandos de inserção como `i` ou `a` e
retornar ao modo normal, bastando para isso usar o recurso `Ctrl-v Esc`,
de forma a simular o acionamento da tecla `Esc` (saída do modo de
inserção). Por exemplo, suponha agora que deseja-se mudar a frase
`este é um texto novo` para `este não é um texto velho`; pode ser feito assim:
```
:5,$ normal 02winão ^[$ciwvelho
```
Decompondo o comando acima temos:
```
:5,$ .... indica o intervalo que é da linha 5 até o fim '$'
normal .. executa em modo normal
0 ....... move o cursor para o começo da linha
2w ...... pula duas palavras (vai para a palavra "é")
i ....... entra no modo de inserção
não  .... insere a palavra "não" seguida de espaço " "
^[ ...... sai do modo de inserção (através de Ctrl-v seguido de Esc)
$ ....... vai para o fim da linha
ciw ..... apaga a última palavra ("novo") e entra em modo de inserção
velho ... insere a palavra "velho" no lugar de "novo"
```
A combinação `Ctrl-v` é utilizada para inserir caracteres de controle na
sua forma literal, prevenindo-se assim a interpretação destes neste
exato momento.
