Exemplos
-------------

Busca usando alternativas:
```
/end\(if\|while\|for\)
```
Buscará ‘if’, ‘while’ e ‘for’.
Observe que é necessário ‘escapar’ os caracteres `\(`, `\`| e `\)`, caso
contrário eles serão interpretados como caracteres comuns.

Quebra de linha
```
/quebra\nde linha
```
Ignorando maiúsculas e minúsculas
```
/\cpalavra
```
Usando `\c` o Vim encontrará “*palavra*”,
“*Palavra*” ou até mesmo
“*PALAVRA*”. Uma dica é colocar no seu arquivo
de configuração “vimrc” veja o capítulo
[Como editar preferências no Vim](../capitulo_12/como_editar_preferencias_no_vim.md).
```
set ignorecase .. ignora maiúsculas e minúsculas na bucsca
set smartcase ... se busca contiver maiúsculas ele passa a
                  considerá-las
set hlsearch .... mostra o que está sendo buscado em cores
set incsearch ... ativa a busca incremental
```
se você não sabe ainda como colocar estas preferências no arquivo de
configuração pode ativa-las em modo de comando precedendo-as com dois
pontos, assim:
```
:set ignorecase<Enter>
```
Substituições com confirmação:
```
:%s/word/palavra/c ..... o `c' no final habilita a confirmação
```
Procurando palavras repetidas
```
/\<\(\w*\) \1\>
```
Multilinha
```
/Hello\_s\+World
```
Buscará ‘World’, separado por qualquer número de espaços, incluindo
quebras de linha. Buscará as três sequências:
```
Hello World

Hello    World

Hello
World
```
Buscar linhas de até 30 caracteres de comprimento
```
/^.\{,30\}$

^  ..... representa começo de linha
.  ..... representa qualquer caractere

:%s/<[^>]*>//g ... apaga tags HTML/XML
:%g/^$/d ......... apaga linhas vazias
:%s/^[\ \t]*\n//g  apaga linhas vazias
```
Remover duas ou mais linhas vazias entre parágrafos diminuindo para uma
só linha vazia.
```
:%s/\(^\n\{2,}\)/\r/g
```
Você pode criar um mapeamento e colocar no seu  /.vimrc
```
map ,s <Esc>:%s/\(^\n\{2,}\)/\r/g<cr>
```
No exemplo acima, ‘,s’ é um mapeamento para reduzir linhas
em branco sucessivas para uma só\

Remove não dígitos (não pega números)
```
:%s/^\D.*//g
```
Remove final de linha DOS/Windows `^M` que tem código hexadecimal igual
a ‘0d’
```
:%s/\%x0d//g
```
Troca palavras de lugar usando expressões regulares:
```
:%s/\(.\+\)\s\(.\+\)/\2 \1/
```
Modificando todas as tags HTML para minúsculo:
```
:%s/<\([^>]*\)>/<\L\1>/g
```
Move linhas 10 a 12 para além da linha 30:
```
:10,12m30
```
