---
title: File Explorer
---

Para abrir o gerenciador de arquivos do Vim use:
```
:Vex ............ abre o file explorer verticalmente
:Sex ............ abre o file explorer em nova janela
:Tex ............ abre o file explorer em nova aba
:Ex ............. abre o file explorer na janela atual
após abrir chame a ajuda <F1>
```
O `:Vex` abre a janela à esquerda. Para que ela abra à direita, coloque a
linha abaixo no seu `~/.vimrc`
```
let g:netrw_altv = 1
```
É possível mapear um atalho “no caso abaixo F2” para abrir o File
Explorer.
```
map <F2> <Esc>:Vex<cr>
```
Ao editar um arquivo no qual há referência a um outro arquivo, por
exemplo: ‘/etc/hosts’, pode-se usar o atalho ‘Ctrl-wf’ para abri-lo em nova janela, ou ‘gf’ para abri-lo
na janela atual. Mas é importante posicionar o cursor sobre o nome do
arquivo. Veja também mapeamentos na seção [Mapeamentos](../capitulo_12/mapeamentos.md).
