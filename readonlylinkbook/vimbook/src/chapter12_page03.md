Autocomandos
------------

Autocomandos habilitam comandos automáticos para situações específicas.
Para executar determinada ação ao iniciar um novo arquivo o autocomando
deverá obedecer este padrão:
```
au BufNewFile tipo ação
```
Veja um exemplo:
```
au BufNewFile,BufRead *.txt source ~/.vim/syntax/txt.vim
```
No exemplo acima o Vim aplica autocomandos para arquivos novos
“*BufNewfile*” ou existentes “*BufRead*”
terminados em `txt`, e para estes tipos carrega um arquivo de
**syntax**, ou seja, um esquema de cores específico.
```
" http://aurelio.net/doc/vim/txt.vim    coloque em ~/.vim/syntax
au BufNewFile,BufRead *.txt source ~/.vim/syntax/txt.vim
```
Para arquivos do tipo texto ‘*.txt*’ use um arquivo de
**syntax** em particular.

O autocomando abaixo coloca um cabeçalho para **scripts**
*bash* caso a linha 1 esteja vazia, observe que os arquivos
em questão tem que ter a extensão *.sh*.
```
au BufNewFile,BufRead *.sh if getline(1) == "" | normal ,sh
```
Para configurar o vim de modo que o diretório corrente fique no
**path** coloque este código no `vimrc`.
```
"fonte: wikia - wiki sobre o vim
if exists('+autochdir')
  set autochdir
else
  autocmd BufEnter * silent! lcd %:p:h:gs/ /\\ /
endif
```
### Exemplos práticos de autocomandos

#### Detectando indentação fora do padrão

Há situações em que é necessária a uniformização de ações, por exemplo,
em códigos Python deve-se manter um padrão para a indentação, ou será
com espaços ou será com tabulações, não se pode misturar os dois pois o
interpretador retornaria um erro. Outra situação em que misturar espaços
com tabulações ocasiona erros é em códigos LaTeX, ao compilar o
documento a formatação não sai como desejado. Até que se perceba o erro
leva um tempo. Para configurar o vim de forma que ele detecte este tipo
de erro ao entrar no arquivo:
```
au! VimEnter * match ErrorMsg /^\t\+/

" explicação para o autocomando acima
au! ............... automaticamente
VimEnter .......... ao entrar no vim
* ................. para qualquer tipo de arquivo
match ErrorMsg .... destaque como erro
/ ................. inicio de um padrão
^ ................. começo de linha
\t ................ tabulação
\+ ................ uma vez ou mais
/ ................. fim do padrão de buscas
```
Para evitar que este erro se repita, ou seja, que sejam adicionados no
começo de linha espaços no lugar de tabulações adiciona-se ao \~/.vimrc
```
set expandtab
```
É perfeitamente possível um autocomando que faça direto a substituição
de tabulações por espaços, mas neste caso não é recomendado que o
autocomando se aplique a todos os tipos de aquivos.

#### Inserindo automaticamente modelos de documento

Pode-se criar um autocomando para inserir um modelo de documento ‘html’
por exemplo de forma automática, ou seja, se você criar um novo
documento do tipo ‘html’ o vim colocará em seu conteúdo um modelo
pre-definido.
```
au BufNewFile *.html 0r ~/.vim/skel/skel.html
```
