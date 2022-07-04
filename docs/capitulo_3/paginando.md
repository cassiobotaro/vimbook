Paginando
---------

Para rolar uma página de cada vez (em modo normal)

```
Ctrl-f
Ctrl-b

:h jumps . ajuda sobre a lista de saltos
:jumps ... exibe a lista de saltos
Ctrl-i ... salta para a posição mais recente
Ctrl-o ... salta para a posição mais antiga
'0 ....... abre o último arquivo editado
'1 ....... abre o penúltimo arquivo editado
gd ....... pula para a definição de uma variável
} ........ pula para o fim do parágrafo
10| ...... pula para a coluna 10
[i ....... pula para definição de variável sob o cursor
```

Observação: lembre-se

```
^ .... equivale a Ctrl
^I ... equivale a Ctrl-I
```

É possível abrir vários arquivos tipo `vim *.txt`. Editar algum arquivo,
salvar e ir para o próximo arquivo com o comando à seguir:

```
:wn
```

Ou voltar ao arquivo anterior

```
:wp
```

É possível ainda “rebobinar” sua lista de arquivos.

```
:rew[wind]
```

Ir para o primeiro

```
:fir[st]
```

Ou para o último

```
:la[st]
```
