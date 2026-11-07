Como no Vim podemos ter infinitos comandos fica complicado memorizar
tudo, e é aí que entram os menus: podemos colocar nossos plugins e atalhos
favoritos em um menu. Veja este exemplo:
```vim
amenu Ferramentas.ExibirNomeDoTema :echo g:colors_name<cr>
```
O comando acima diz:

| Comando | Descrição |
|---------|-----------|
| `amenu` | cria um menu |
| `Ferramentas.ExibirNomeDoTema` | menu Ferramentas, submenu ExibirNomeDoTema |
| `:echo g:colors_name<cr>` | exibe o nome do tema atual |

Caso haja espaços no nome a definir você pode fazer assim
```vim
amenu Ferramentas.Exibir\ nome\ do\ tema :echo g:colors_name<cr>
```
