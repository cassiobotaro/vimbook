Comentando rapidamente um trecho
--------------------------------

Tomando como exemplo um trecho de código como abaixo:
```
1   input{capitulo1}
2   input{capitulo2}
3   input{capitulo3}
4   input{capitulo4}
5   input{capitulo5}
6   input{capitulo6}
7   input{capitulo7}
8   input{capitulo8}
9   input{capitulo9}
```
Se desejamos comentar da linha 4 até a linha 9 podemos fazer:
```
posicionar o cursor no começo da linha 4
Ctrl-v ........... inicia seleção por blocos
5j ............... estende a seleção até o fim
Shift-i .......... inicia inserção no começo da linha
% ................ insere comentário (LaTeX)
Esc .............. sai do modo de inserção
```
