Usando o `grep` interno do Vim
------------------------------

Para editar todos os arquivos que contenham a palavra “inusitada”:
```
:vimgrep /\cinusitada/ *
```
a opção `\c` torna a busca indiferente a letras maiúsculas e
minúsculas.

Obs: o Vim busca à partir do diretório atual, para se descobrir o
diretório atual ou mudá-lo:
```
:pwd ........... exibe o diretório atual
:cd /diretório   muda de diretório
```

