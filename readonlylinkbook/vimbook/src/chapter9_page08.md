Indent
------

Indent[^1] é um programa que indenta seu código fonte de
acordo com os padrões configurados no seu arquivo
HOME/.indent.pro. Vou pressupor que você já saiba usar o
indent e como fazer as configurações necessárias para ele
funcionar, então vamos ao funcionamento dele no Vim:

Para indentar um bloco de código, primeiro selecione-o com o modo
*visual line* (com V), depois é só entrar com
o comando como se fosse qualquer outro comando externo:
```
:!indent
```
No caso, como foi selecionado um bloco de código, irão aparecer alguns
caracteres extras, mas o procedimento continua o mesmo:
```
:'<,'>!indent
```
[^1]: [http://www.gnu.org/software/indent](http://www.gnu.org/software/indent)
