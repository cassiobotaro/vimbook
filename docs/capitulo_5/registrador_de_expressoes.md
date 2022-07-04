Registrador de expressões "=
-------------------------
```
"=
```
O registrador de expressões permite efetuar cálculos diretamente no editor,
usando o atalho "Ctrl-r =" *no modo de
inserção*, o editor mostrará um sinal de igualdade na barra de
status e o usuário digita então uma expressão matemática como uma
multiplicação "6\*9" e em seguida pressiona
Enter para que o editor finalize a operação. Veja um vídeo
demonstrando sua utilização [neste
link](http://vimeo.com/2967392).

Para entender melhor como funciona o registrador de expressões tomemos um
exemplo. Para fazer uma sequência como abaixo:
```
linha 1 tem o valor 150,
linha 2 tem o valor 300,
linha 3 tem o valor 450,
...
```
Acompanhe os passos para a criação de uma macro permite fazer uma
sequência de quantas linhas forem necessárias com o incremento proposto
acima.
```
<Esc>  ......... sai do modo de inserção
qa ............. inicia a macro
yy ............. copia a primeira linha
p .............. cola a linha copiada
w .............. pula para o número `1'
<Ctrl-a> ....... incrementa o número (agora 2)
4w ............. avança 4 palavras até 150
"ndw ........... apaga o `150' para o registrador "n
a .............. entra em modo de inserção
Ctrl-r = ....... abre o registrador de expressões
Ctrl-r n + 150   insere dentro do registrador de expressões
                 o registrador "n
<Enter>  ........ executa o registrador de expressões
<Esc> ........... sai do modo de inserção
0 ............... vai para o começo da linha
q ............... para a gravação da macro
```
Agora posicione o cursor no começo da linha e pressione `10@a`.

Na seção [Mapeamento para Calcular Expressões](../capitulo_12/mapeamentos.md) há mais dicas
sobre o uso do registrador de expressões e cálculos matemáticos.
