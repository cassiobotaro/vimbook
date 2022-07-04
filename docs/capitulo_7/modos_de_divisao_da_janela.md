Modos de divisão da janela
--------------------------

Como foi dito anteriormente, é possível visualizar mais de um buffer ao mesmo
tempo, e isso pode ser feito utilizando *tab* ou *split*.

### Utilizando abas (tab)

A partir do Vim 7 foi disponibilizada a função de abrir arquivos em
abas, portanto é possível ter vários buffers abertos em abas distintas e
alternar entre elas facilmente. Os comandos para utilização das abas são:
```
:tabnew ........... Abre uma nova tab
:tabprevious ...... Vai para a tab anterior
:tabnext .......... Vai para a próxima tab
```
### Utilizando split horizontal

Enquanto os comandos referentes a *tab* deixam a janela
inteira disponível para o texto e apenas cria uma pequena aba na parte
superior, o comando *split* literamente divide a tela atual
em duas para visualização simultânea dos “buffers” (seja ele o mesmo ou
outro diferente). Esse é o split padrão do Vim mas pode ser alterado
facilmente colocando a linha abaixo no seu `~/.vimrc`:
```
:set splitright .... split padrão para vertical
```
### Utilizando split vertical

O split vertical funciona da mesma maneira que o split horizontal, sendo
a unica diferença o modo como a tela é dividida, pois nesse caso a tela
é dividida verticalmente.
