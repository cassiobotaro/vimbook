Copiar a partir de um ponto
------------------------------------
```
:19;+3 co $
```
O Vim sempre necessita de um intervalo (inicial e final) mas se usar-mos
‘;’ ele considera a primeira linha como segundo ponto do intervalo, e no
caso acima estamos dizendo (nas entrelinhas) linhas 19 e 19+3\

De forma análoga pode-se usar como referência um padrão qualquer:
```
:/palavra/;+10 m 0
```
O comando acima diz: à partir da linha que contém “palavra” incluindo as
10 próximas linhas mova ‘m’ para a primeira linha ‘0’, ou
seja, antes da linha 1.
