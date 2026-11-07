```text
:let @a=@_   ... limpa o registrador a
:let @a=""   ... limpa o registrador a
:let @a=@"   ... salva registrador sem nome *N*
:let @*=@a   ... copia o registrador para o buffer de colagem
:let @*=@:   ... copia o último comando para o buffer de
                 colagem
:let @*=@/   ... copia a última busca para o buffer de
                 colagem
:let @*=@%   ... copia o nome do arquivo para o buffer de
                 colagem
:reg         ... mostra o conteúdo de todos os registradores
```
Em modo de inserção

| Comando | Descrição |
|---------|-----------|
| `Ctrl-R -` | Insere o registrador de pequenas deleções |
| `Ctrl-R` seguido de `0`-`9` ou `a`-`z` | Insere registradores 0-9 e a-z |
| `Ctrl-R %` | Insere o nome do arquivo |
| `Ctrl-R =` seguido do nome da variável | Insere o conteúdo de uma variável |
| `Ctrl-R Ctrl-W` | Insere a palavra sob o cursor |
| `Ctrl-R Ctrl-A` | Insere a WORD sob o cursor (delimitada por espaços) |

Um exemplo: pré-carregando o nome do arquivo no registrador `n`.

coloque em seu `~/.vimrc`
```vim
let @n=@%
```
Como foi atribuído ao registrador `n` o conteúdo de @%, ou seja, o nome do
arquivo, você pode pressionar `Ctrl-R n` em modo de inserção e o nome do arquivo será inserido.
