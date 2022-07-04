Ordenando
---------

O Vim, versão 7 ou superior, passa a ter um comando de ordenação que
também permite a retirada de linhas duplicadas, tal como foi
apresentado.
```
:sort u ... ordena e retira linhas duplicadas
:sort n ... ordena numericamente
```
Obs: a ordenação numérica é diferente da ordenação alfabética se em um
trecho contendo algo como:
```
8
9
10
11
12
```
E você tentar fazer:
```
:sort

```
O Vim colocará nas três primeiras linhas
```
10
11
12
```

Portanto lembre-se que se a ordenação envolver números use:
```
:sort n

```
Você pode fazer a ordenação em um intervalo assim:
```
:1,15 sort n
```
O comando acima diz “`*Ordene numericamente da linha 1 até a linha
15*`”. Podemos ainda ordenar à partir de uma coluna:
```
:sort /.*\%8v/   ..... ordena à partir do 8º caractere
```
