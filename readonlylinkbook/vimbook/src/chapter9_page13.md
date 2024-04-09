Removendo linhas duplicadas
---------------------------
```
:%!uniq
```
O caractere "%" representa a região equivalente ao arquivo atual
inteiro. A versão do Vim 7 em diante tem um comando *sort*
que permite remover linhas duplicadas *uniq* e ordenar, sem
a necessidade de usar comandos externos, para mais detalhes:
```
:h sort
```
