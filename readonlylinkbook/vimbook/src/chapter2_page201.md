Abrindo o arquivo para a edição
-------------------------------

Portanto, a primeira coisa a fazer é abrir um arquivo. Como visto, para
abrir um arquivo com Vim, digite em um terminal:
```
vim texto.txt
```
onde `texto.txt` é o nome do arquivo que deseja-se criar ou
editar.

Caso deseje abrir o arquivo na linha 10, usa-se:
```
vim +10 /caminho/para/o/arquivo
```
se quiser abrir o arquivo na linha que contém um determinado padrão ,
digite:
```
vim +/padrão arquivo
```
Caso o padrão tenha espaços no nome coloque entre aspas ou use
*escape* "\" a fim de não obter erro.

Se o vim for aberto sem indicação de arquivo pode-se indicar o arquivo a
ser editado em modo de comando desta forma:
```
:e /home/usuario/arquivo
```
