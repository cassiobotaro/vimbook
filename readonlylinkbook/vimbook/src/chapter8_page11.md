Repetindo substituições 
------------------------

Caso seja feito uma substituição em um intervalo como abaixo
```
:5,32s/isto/aquilo/g
```
Pode-se repetir esta substituição em qualquer linha que estiver apenas
usando este símbolo
```
&
```
O Vim substituirá na linha corrente ‘isto’ por ‘aquilo’. Podendo repetir
a última substituição globalmente assim:
```
g&
```
