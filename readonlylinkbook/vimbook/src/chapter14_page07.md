Use autocomandos
----------------

No arquivo de configuração do Vim `~/.vimrc` pode-se pode criar comandos
automáticos que serão executados diante de uma determinada
circunstância. O comando abaixo será executado em qualquer arquivo
existente, ao abrir o mesmo, posicionando o cursor no último local
editado:
```VimL
"autocmd BufEnter * lcd %:p:h
autocmd BufReadPost *
  \ if line("'\"") > 0 && line("'\"") <= line("$") |
  \   exe "normal g`\"" |
  \ endif
```
Grupo de comandos para arquivos do tipo ‘html’. Observe que
o autocomando carrega um arquivo de configuração do Vim exclusivo para o
tipo html/htm e no caso de arquivos novos
‘BufNewFile’ ele já cria um esqueleto puxando do endereço
indicado:
```VimL
augroup html
 au! <--> Remove all html autocommands
  au!
  au BufNewFile,BufRead *.html,*.shtml,*.htm set ft=html
  au BufNewFile,BufRead,BufEnter  *.html,*.shtml,*.htm so ~/docs/vim/.vimrc-html
  au BufNewFile *.html 0r ~/docs/vim/skel.html
  au BufNewFile *.html*.shtml,*.htm /body/+  " coloca o cursor após o corpo <body>
  au BufNewFile,BufRead *.html,*.shtml,*.htm set noautoindent
augroup end
```
