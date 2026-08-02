---
title: Modos de divisão da janela
---

Como foi dito anteriormente, é possível visualizar mais de um buffer ao mesmo
tempo, e isso pode ser feito utilizando *tab* ou *split*.

### Utilizando abas (tab)

A partir do Vim 7 foi disponibilizada a função de abrir arquivos em
abas, portanto é possível ter vários buffers abertos em abas distintas e
alternar entre elas facilmente. Os comandos para utilização das abas são:

| Comando | Descrição |
|---------|-----------|
| `:tabnew` | Abre uma nova tab |
| `:tabprevious` | Vai para a tab anterior |
| `:tabnext` | Vai para a próxima tab |

### Utilizando split horizontal

Enquanto os comandos referentes a *tab* deixam a janela
inteira disponível para o texto e apenas cria uma pequena aba na parte
superior, o comando *split* literalmente divide a tela atual
em duas para visualização simultânea dos “buffers” (seja ele o mesmo ou
outro diferente). O comando é `:split` (ou `:sp`), e por padrão a nova
janela aparece acima da atual. Para que ela apareça abaixo, coloque no
seu `~/.vimrc`:
```
:set splitbelow .... a janela nova abre abaixo da atual
```
### Utilizando split vertical

O split vertical funciona da mesma maneira que o split horizontal, sendo
a única diferença o modo como a tela é dividida, pois nesse caso a tela
é dividida verticalmente. O comando é `:vsplit` (ou `:vs`), e por padrão
a nova janela aparece à esquerda da atual. Para que ela apareça à
direita:
```
:set splitright .... a janela nova abre à direita da atual
```
