Uma calculadora diferente
-------------------------

Sempre que for necessário digitar o resultado de uma expressão
matemática (portanto no modo de inserção) pode-se usar o atalho
`Ctrl-r =`, ele ativa o registrador de expressões, na linha de
comando do Vim aparece um sinal de igual, digita-se então uma expressão
matemática qualquer tipo `35\*6` e em seguida pressiona-se
`Enter`, o Vim coloca então o resultado da expressão no
lugar desejado. Portanto não precisa-se recorrer a nenhuma calculadora
para fazer cálculos. Pode-se fazer uso do “registrador de Expressões”
dentro de macros, ou seja, ao gravar ações pode-se fazer uso deste
recurso, aumentando assim sua complexidade e poder! Para ler sobre
“macros” veja o capítulo [Gravando Comandos](../capitulo_8/gravando_comandos.md).
E veja também o capítulo [registrador de expressões](../capitulo_5/registrador_de_expressoes.md).

Na capítulo [Calculadora Científica com Vim](../capitulo_9/calculadora_cientifica_com_o_vim.md) há uma descrição sobre como fazer cálculos com maior
precisão e complexidade.

Se a intenção for apenas exibir um calculo na barra de comandos é
possível fazer algo assim:
```
:echo 5.2 * 3
```

