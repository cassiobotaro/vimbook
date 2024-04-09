Criando um menu 
---------------

Como no Vim podemos ter infinitos comandos fica complicado memorizar
tudo é aí que entram os menus, podemos colocar nossos plugins e atalhos
favoritos em um menu veja este exemplo
```
amenu Ferramentas.ExibirNomeDoTema :echo g:colors_name<cr>
```
O comando acima diz:
```
amenu ........................ cria um menu
Ferramentas.ExibirNomeDoTema . Menu plugin submenu ExibirNomeDoTema
:echo g:colors_name<cr> ...... exibe o nome do tema atual
```
Caso haja espaços no nome a definir você pode fazer assim
```
amenu Ferramentas.Exibir\ nome\ do\ tema :echo g:colors_name<cr>
```
