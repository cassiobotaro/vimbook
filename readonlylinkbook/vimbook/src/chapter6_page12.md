Inserindo linha antes e depois
---------------------------------------

Suponha que se queira um comando, considere `,t`, que faça com que a
linha indentada corrente passe a ter uma linha em branco antes e depois;
isto pode ser obtido pelo seguinte mapeamento:
```
:map ,t <Esc>:.s/^\(\s\+\)\(.*\)/\r\1\2\r/g<cr>
```
Explicando:
```
: ................ entra no modo de comando
map ,t ........... mapeia ,t para a função desejada
<Esc> ............ ao executar sai do modo de inserção
s/isto/aquilo/g .. substitui isto por aquilo
: ................ inicia o modo de comando
. ................ na linha corrente
s ................ substitua
^ ................ começo de linha
\s\+ ............. um espaço ou mais (barras são escapes)
.* ............... qualquer coisa depois
\(grupo\) ........ agrupo para referenciar com \1
\1 ............... repete na substituição o grupo 1
\r ............... insere uma quebra de linha
g ................ em todas as ocorrências da linha
<cr> ............. Enter
```
