Usando o comando `bufdo`
------------------------

Com o comando :bufdo, pode-se executar um comando em um
conjunto de arquivos de forma rápida. No exemplo a seguir, serão abertos
todos os arquivos HTML do diretório atual, será efetuado uma
substituição e em seguida serão todos salvos.
```
vim *.html
:bufdo %s/bgcolor="eeeeee"/bgcolor="ffffff"/ge | :wall
:qall
```
O comando :wall salva “*write*” todos
“*all*” os arquivos abertos pelo comando
vim \*.html. Opcionalmente você pode combinar
“:wall” e “:qall” com o comando
:wqall, que salva todos os arquivos abertos e em seguida
sai do Vim. A opção ‘e’ faz com que o vim não exiba
mensagens de erro caso o *buffer* em questão não contenha o
padrão a ser substituído.
