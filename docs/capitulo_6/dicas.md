Para colocar a última busca em uma substituição, pressione `Ctrl-r`
seguido de `/` no lugar do padrão:
```
:%s/<Ctrl-r>//novo/g
```
Mais simples ainda: deixar o padrão vazio já faz o Vim reaproveitar a
última busca, e portanto o comando abaixo fará a substituição da última
busca por casinha:
```
:%s//casinha/g
```
