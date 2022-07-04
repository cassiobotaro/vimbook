Um Wiki para o Vim
==================

É inegável a facilidade que um Wiki nos traz, os documentos são
indexados e linkados de forma simples. Já pesquisei uma porção de Wikis
e, para uso pessoal recomendo o Potwiki. O “link” do Potwiki é
[este](http://www.vim.org/scripts/script.php?script_id=1018). 
O Potwiki é um Wiki completo para o Vim, funciona localmente embora
possa ser aberto remotamente via ssh[^1]. Para criar um “link” no
Potwiki basta usar WikiNames, são nomes iniciados com letra maiúscula e
que contenham outra letra em maiúsculo no meio.

Ao baixar o arquivo salve em `~/.vim/plugin`.

Mais ou menos na linha 53 do Potwiki `~/.vim/plugin/potwiki.vim` você
define onde ele guardará os arquivos, no meu caso
`/home/docs/textos/wiki`. a linha ficou assim:
```
call s:default('home',"~/.wiki/HomePage")
```
Outra forma de indicar a página inicial seria colocar no seu .virmc
```
let potwiki_home = "$HOME/.wiki/HomePage"
```
[^1]: Sistema de acesso remoto
