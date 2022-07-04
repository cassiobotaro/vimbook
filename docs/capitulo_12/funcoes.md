Funções
-------

### Fechamento automático de parênteses
```VimL
 " --------------------------------------
 " Ativa fechamento automático para parêntese
 " Set automatic expansion of parenthesis/brackets
 inoremap ( ()<Esc>:call BC_AddChar(")")<cr>i
 inoremap { {}<Esc>:call BC_AddChar("}")<cr>i
 inoremap [ []<Esc>:call BC_AddChar("]")<cr>i
 "
 " mapeia Ctrl-j para pular fora de parênteses colchetes etc...
 inoremap <C-j> <Esc>:call search(BC_GetChar(), "W")<cr>a
 " Function for the above
 function! BC_AddChar(schar)
	if exists("k")
		let b:robstack = b:robstack . a:schar
	else
		let b:robstack = a:schar
	endif
 endfunction
 function! BC_GetChar()
	let l:char = b:robstack[strlen(b:robstack)-1]
	let b:robstack = strpart(b:robstack, 0, strlen(b:robstack)-1)
	return l:char
 endfunction

'''Outra opção para fechamento de parênteses'''

 " Fechamento automático de parênteses
 imap { {}<left>
 imap ( ()<left>
 imap [ []<left>

 " pular fora dos parênteses, colchetes e chaves, mover o cursor
 " no modo de inserção
 imap <c-l> <Esc><right>a
 imap <c-h> <Esc><left>a
```
### Função para barra de status
```VimL
set statusline=%F%m%r%h%w
set statusline+=[FORMAT=%{&ff}]
set statusline+=[TYPE=%Y]
set statusline+=[ASCII=\%03.3b][HEX=\%02.2B]
set statusline+=[POS=%04l,%04v][%p%%][LEN=%L]
set laststatus=2
```
Caso este código não funcione acesse [este
link](http://vim.wikia.com/wiki/Writing_a_valid_statusline) 

### Rolar outra janela

Se você dividir janelas tipo
```
 Ctrl-w n
```
pode colocar esta função no seu `.vimrc`
```VimL
 " rola janela alternativa
 fun! ScrollOtherWindow(dir)
  if a:dir == "down"
    let move = "\<C-E>"
  elseif a:dir == "up"
    let move = "\<C-Y>"
  endif
  exec "normal \<C-W>p" . move . "\<C-W>p"
endfun
nmap <silent> <M-Down> :call ScrollOtherWindow("down")<CR>
nmap <silent> <M-Up> :call ScrollOtherWindow("up")<CR>
```
Esta função é acionada com o atalho *Alt-⬆* e
*Alt-⬇*.

### Função para numerar linhas

No site wikia há um código de função para [numerar
linhas](http://vim.wikia.com/wiki/Number_a_group_of_lines) 

### Função para trocar o esquema de cores
```VimL
 function! <SID>SwitchColorSchemes()
    if !exists("g:colors_name")
      let g:colors_name = 'default'
    endif
    if g:colors_name == 'default'
      colorscheme delek
    elseif g:colors_name == 'delek'
      colorscheme desert
    elseif g:colors_name == 'desert'
      colorscheme elflord
    elseif g:colors_name == 'elflord'
      colorscheme  evening
    elseif g:colors_name == 'evening'
      colorscheme industry
    elseif g:colors_name == 'industry'
      colorscheme koehler
    elseif g:colors_name == 'koehler'
      colorscheme morning
    elseif g:colors_name == 'morning'
      colorscheme default
    endif
 endfunction
 map <silent> <F6> :call <SID>SwitchColorSchemes()<CR>
```
Obs: Talvez os esquemas de cores aqui mostrados podem não existir em sua plataforma, verifique os esquemas disponíveis e modifique a função para que tudo funcione corretamente.

### Uma função para inserir cabeçalho de script

para chamar a função basta pressionar `,sh` em modo normal
```VimL
 " Cria um cabeçalho para scripts bash
 fun! InsertHeadBash()
    normal(1G)
    :set ft=bash
    :set ts=4
    call append(0, "#!/bin/bash")
    call append(1, "# Criado em: " . strftime("%a %d/%b/%Y hs %H:%M"))
    call append(2, "# Ultima modificação: " . strftime("%a %d/%b/%Y hs %H:%M"))
    call append(3, "# NOME DA SUA EMPRESA ")
    call append(4, "# Propósito do script ")
    normal($)
 endfun
 map ,sh :call InsertHeadBash()<cr>
```
### Função para inserir cabeçalhos Python
```VimL
 " função para inserir cabeçalhos Python
 fun! BufNewFile_PY()
  normal(1G)
  :set ft=python
  :set ts=4
  call append(0, "#!/usr/bin/python")
  call append(1, "# -*- coding: utf-8 -*-")
  call append(2, "# Criado: " . strftime("%a %d/%b/%Y hs %H:%M"))
  call append(3, "# Modificado: " . strftime("%a %d/%b/%Y hs %H:%M"))
  call append(4, "# Instituicao: <+nome+>")
  call append(5, "# Proposito do script: <+descreva+>")
  call append(6, "# Autor: <+seuNome+>")
  call append(7, "# site: <+seuSite+>")
  normal gg
 endfun
 autocmd BufNewFile *.py call BufNewFile_PY()
 map ,py :call BufNewFile_PY()<cr>


 " Ao editar um arquivo será aberto no último ponto em
 " que foi editado
  augroup vimrc-remember-cursor-position
   autocmd!
   autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g`\"" | endif
 augroup END
 " Permite recarregar o Vim para que modificações no
 " Próprio vimrc seja ativadas com o mesmo sendo editado
 nmap <F12> :<C-u>source $HOME/.vimrc <BAR> echo "Vimrc recarregado!"<CR>
```
Redimensionar janelas
```VimL
" Redimensionar a janela com
" Alt-seta à direita e esquerda
map <M-right> <Esc>:resize +2 <CR>
map <M-left> <Esc>:resize -2 <CR>
```
### Função para pular para uma linha
```VimL
 "ir para linha
 " ir para uma linha específica
 function! GoToLine()
 let ln = inputdialog("ir para a linha...")
 exe ":" . ln
 endfunction
 "no meu caso o mapeamento é com Ctrl-l
 "use o que melhor lhe convier
 nmap <C-l> :call GoToLine()<CR>
```
### Função para gerar backup

A função abaixo é útil para ser usada quando você vai editar um arquivo
gerando modificações significativas, assim você poderá restaurar o
backup se necessário
```VimL
 " A mapping to make a backup of the current file.
 fun! WriteBackup()
    let fname = expand("%:p") . "__" . strftime("%d-%m-%Y--%H.%M.%S")
    silent exe ":w " . fname
    echo "Wrote " . fname
 endfun
 nnoremap <Leader>ba :call WriteBackup()<CR>
```
O atalho “`<leader>`” em geral é a barra invertida
`\`, na dúvida “`:help <leader>`”.


