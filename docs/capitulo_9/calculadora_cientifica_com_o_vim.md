Calculadora Científica com o Vim
--------------------------------

Para usar a função de Calculadora Científica no Vim usamos uma
ferramenta externa, que pode ser o comando `bc` do
GNU/Linux, ou uma linguagem de programação como *Python* ou
*Ruby*, veremos como habilitar a calculadora usando o
*Python*. Obviamente esta linguagem de programação deve
estar instalada no sistema em que se deseja usar seus recursos. Deve-se
testar se a versão do Vim tem suporte ao Python `:version`, em seguida
colocam-se os mapeamentos no `.vimrc`.
```
:command! -nargs=+ Calc :py print <args>
:py from math import *
```
Feito isto pode-se usar o comando `:Calc` como visto
abaixo:
```
:Calc pi
:Calc cos(30)
:Calc pow(5,3)
:Calc 10.0/3
:Calc sum(xrange(1,101))
:Calc [x**2 for x in range(10)] 
```
