Restaurando sessões
-------------------

Após gravar sessões, elas podem ser carregadas ao iniciar o Vim:
```
vim -S sessao.vim
```
ou então de dentro do próprio Vim (no modo de comando):
```
:so sessao.vim
```
Após restaurar a sessão, o nome da sessão corrente é acessível através
de uma variável interna `v:this_session`; caso queira-se exibir na
linha de comando o nome da sessão ativa (incluindo o caminho), faz-se:
```
:echo v:this_session
```
Podemos fazer mapeamentos para atualizar a sessão atual e exibir
detalhes da mesma:
```
"mapeamento para gravar sessão
nmap <F4> :wa<Bar>exe "mksession! " . v:this_session<CR>:so ~/sessions/

"mapeamento para exibir a sessão ativa
map <s-F4> <esc>:echo v:this_session<cr>
```
