Outros mapeamentos
------------------

Destaca espaços e tabulações redundantes:
```
highlight RedundantWhitespace ctermbg=red guibg=red
match RedundantWhitespace /\s\+$\| \+\ze\t/
```
Explicando com detalhes
```
\s ..... espaço
\+ ..... uma ou mais vezes
$ ...... no final da linha
\| ..... ou
`` '' .. espaço (veja imagem acima)
\+ ..... uma ou mais vezes
\ze .... até o fim
\t ..... tabulação
```
Portanto a expressão regular acima localizará espaços ou tabulações no
final de linha e destacará em vermelho.
```VimL
"Remove espaços redundantes no fim das linhas
map <F7> <Esc>mz:%s/\s\+$//g<cr>`z
```
Um detalhe importante
```
mz ... marca a posição atual do cursor para retornar no final do comando
`z ... retorna à marca criada
```
Se não fosse feito isto o cursor iria ficar na linha da última
substituição!
```VimL
"Abre o vim explorer
map <F6> <Esc>:vne .<cr><bar>:vertical resize -30<cr><bar>:set nonu<cr>
```
Podemos usar “Expressões Regulares[^1]” em buscas do Vim veja um exemplo
para retirar todas as tags HTML
```VimL
"mapeamento para retirar tags HTML com Ctrl-Alt-t
nmap <C-M-t> :%s/<[^>]*>//g <cr>
" Quebra a linha atual no local do cursor com F2
nmap <F2> a<CR><Esc>
" join lines  -- Junta as linhas com Shift-F2
nmap <S-F2> A<Del><Space>
```
Para mais detalhes sobre buscas acesse o capítulo [Buscas e substituições](../capitulo_6/buscas_e_substituicoes.md).

[^1]: <http://guia-er.sourceforge.net>
