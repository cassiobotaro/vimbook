O Vim, versão 7 ou superior, passa a ter um comando de ordenação que
também permite a retirada de linhas duplicadas, tal como foi
apresentado.

| Comando | Descrição |
|---------|-----------|
| `:sort u` | ordena e retira linhas duplicadas |
| `:sort n` | ordena numericamente |

Obs.: a ordenação numérica é diferente da ordenação alfabética se em um
trecho contendo algo como:
```text
8
9
10
11
12
```
E você tentar fazer:
```vim
:sort
```
O Vim colocará nas três primeiras linhas
```text
10
11
12
```

Portanto, lembre-se de que, se a ordenação envolver números, use:
```vim
:sort n
```
Você pode fazer a ordenação em um intervalo assim:
```vim
:1,15 sort n
```
O comando acima diz “`*Ordene numericamente da linha 1 até a linha
15*`”. Podemos ainda ordenar a partir de uma coluna:
```vim
:sort /.*\%8v/
```
O comando acima ordena a partir do 8º caractere.
