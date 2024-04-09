Manipulando registradores
---------------------
```
:let @a=@_   ... limpa o registrador a
:let @a=``'' ... limpa o registrador a
:let @a=@"   ... salva registrador sem nome *N*
:let @*=@a   ... copia o registrador para o buffer de colagem
:let @*=@:   ... copia o ultimo comando para o buffer de
                 colagem
:let @*=@/   ... copia a última busca para o buffer de
                 colagem
:let @*=@%   ... copia o nome do arquivo para o buffer de
                 colagem
:reg         ... mostra o conteúdo de todos os registradores
```
Em modo de inserção
```
<C-R>-   ....... Insere o registrador de pequenas deleções
<C-R>[0-9a-z] .. Insere registradores 0-9 e a-z
<C-R>%        .. Insere o nome do arquivo
<C-R>=somevar .. Insere o conteúdo de uma variável
<C-R><C-A> ..... Insere `Big-Words' veja seção 2.1
```
Um exemplo: pré-carregando o nome do arquivo no registrador `n`.

coloque em seu `~/.vimrc`
```
let @n=@%
```
Como foi atribuído ao registrador `n` o conteúdo de @%, ou seja, o nome do
arquivo, você pode fazer algo assim em modo de inserção:
```
Ctrl-r n
```
E o nome do arquivo será inserido.
