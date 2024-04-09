Exemplo de menu
---------------
```
" cores
menu T&emas.cores.quagmire :colo quagmire<CR>
menu T&emas.cores.inkpot :colo inkpot<CR>
menu T&emas.cores.google :colo google<CR>
menu T&emas.cores.ir_black :colo ir_black<CR>
menu T&emas.cores.molokai :colo molokai<CR>
" Fontes
menu T&emas.fonte.Inconsolata :set gfn=Inconsolata:h10<CR>
menu T&emas.fonte.Anonymous :set anti gfn=Anonymous:h8<CR>
menu T&emas.fonte.Envy\ Code :set anti gfn=Envy_Code_R:h10<CR>
menu T&emas.fonte.Monaco :set gfn=monaco:h9<CR>
menu T&emas.fonte.Crisp :set anti gfn=Crisp:h12<CR>
menu T&emas.fonte.Liberation\ Mono :set gfn=Liberation\ Mono:h10<CR>
```
O comando “*:update*” Atualiza o menu recém modificado.
Quando o comando “*:amenu*” É usado sem nenhum argumento o
Vim mostra os menus definidos atualmente. Para listar todas as opções de
menu para `Plugin` por exemplo digita-se no modo de comandos
“*:amenu Plugin*”.

#### Ocultando as barras de ferramentas e menu
```
:set guioptions-=m  ........ oculta menus
:set guioptions-=T  ........ oculta icones

obs: para exibir novamente repita o comando
substituindo o sinal de menos por mais.
```
