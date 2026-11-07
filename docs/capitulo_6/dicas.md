Para colocar a última busca em uma substituição, pressione `Ctrl-R /`
no lugar do padrão: digite `:%s/`, pressione `Ctrl-R /` e complete com
`/novo/g`.

Mais simples ainda: deixar o padrão vazio já faz o Vim reaproveitar a
última busca, e portanto o comando abaixo fará a substituição da última
busca por casinha:
```vim
:%s//casinha/g
```
