Como definir um registrador no `vimrc`?
------------------------------------

Se você não sabe ainda como editar preferências no Vim leia antes o
capítulo [Como editar preferências no Vim](../capitulo_12/como_editar_preferencias_no_vim.md).

Você pode criar uma variável no vimrc assim:
```
let var="foo" ...... define foo para var
echo var ........... mostra o valor de var
```
Pode também dizer ao Vim algo como...
```
:let @d=strftime("c")<Enter>
```
Neste caso estou dizendo a ele que guarde na variável 'd',
o valor da data do sistema `strftime("c")` ou então
cole isto no vimrc:
```
let @d=strftime("c")<cr>
```
A diferença entre digitar diretamente um comando e adicioná-lo ao
vimrc é que uma vez no vimrc o registrador em
questão estará sempre disponível, observe também as sutis diferenças, um
Enter inserido manualmente é apenas uma indicação de uma
ação que você fará pressionando a tecla especificada, já o comando
mapeado vira `<cr>`, veja ainda que no vimrc os dois
pontos `:` somem.

Pode mapear tudo isto
```
let @d=strftime("c")<cr>
imap ,d <cr-r>d
nmap ,d "dp
```
As atribuições acima correspondem a:

1.  Guarda a data na variável 'd'

2.  Mapeamento para o modo de inserção "imap" digite ,d

3.  Mapeamento para o modo normal "nmap" digite ,d

E digitar ,d normalmente

Desmistificando o strftime
```
" d=dia m=mes Y=ano H=hora M=minuto c=data-completa
:h strftime ........ ajuda completa sobre o comando
```
e inserir em modo normal assim:
```
"dp
```
ou usar em modo de inserção assim:
```
Ctrl-r d
```
