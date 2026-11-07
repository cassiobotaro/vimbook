---
title: Repetindo substituições
---

Caso seja feita uma substituição em um intervalo como abaixo
```vim
:5,32s/isto/aquilo/g
```
Pode-se repetir esta substituição em qualquer linha que estiver apenas
usando este símbolo
```text
&
```
O Vim substituirá na linha corrente ‘isto’ por ‘aquilo’. Podendo repetir
a última substituição globalmente assim:
```text
g&
```
