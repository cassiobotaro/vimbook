Salvando
--------

A maneira mais simples de salvar um arquivo, é usar o comando:
```
:w
```
Para especificar um novo nome para o arquivo, simplesmente digite:
```
:w! >> “file”
```
O conteúdo será gravado no arquivo `file` e você continuará
no arquivo original.

Também existe o comando
```
:sav[eas] nome
```
salva o arquivo com um novo nome e muda para esse novo arquivo (o
arquivo original não é apagado). Para sair do editor, salvando o arquivo
atual, digite `:x` (ou `:wq`).
```
:w ............................ salva
:wq  .......................... salva e sai
:w nome ....................... salvar como
:saveas nome .................. salvar como
:sav nome ..................... mesmo que "saveas nome"
:x ............................ salva se existirem modificações
:10,20 w! ~/Desktop/teste.txt . salva um trecho para outro arquivo
:w! ........................... salvamento forçado
:e! ........................... reinicia a edição ignorando alterações
```
