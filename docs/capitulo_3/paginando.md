Para rolar uma página de cada vez (em modo normal)

| Comando | Descrição |
|---------|-----------|
| `Ctrl-F` | avança uma página |
| `Ctrl-B` | volta uma página |
| `:h jumps` | ajuda sobre a lista de saltos |
| `:jumps` | exibe a lista de saltos |
| `Ctrl-I` | salta para a posição mais recente |
| `Ctrl-O` | salta para a posição mais antiga |
| `'0` | abre o último arquivo editado |
| `'1` | abre o penúltimo arquivo editado |
| `gd` | pula para a definição de uma variável |
| `}` | pula para o fim do parágrafo |
| <code>10&#124;</code> | pula para a coluna 10 |
| `[i` | pula para definição de variável sob o cursor |

É possível abrir vários arquivos tipo `vim *.txt`. Editar algum arquivo,
salvar e ir para o próximo arquivo com o comando a seguir:

```vim
:wn
```

Ou voltar ao arquivo anterior

```vim
:wp
```

É possível ainda “rebobinar” sua lista de arquivos.

```vim
:rew[ind]
```

Ir para o primeiro

```vim
:fir[st]
```

Ou para o último

```vim
:la[st]
```
