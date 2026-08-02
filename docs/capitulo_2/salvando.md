A maneira mais simples de salvar um arquivo, é usar o comando:
```
:w
```
Para gravar o conteúdo em outro arquivo, simplesmente digite:
```
:w arquivo
```
O conteúdo será gravado no arquivo `arquivo` e você continuará
no arquivo original. Para anexar o conteúdo ao final de um arquivo já
existente, em vez de sobrescrevê-lo, usa-se:
```
:w >> arquivo
```

Também existe o comando:
```
:sav[eas] nome
```
salva o arquivo com um novo nome e muda para esse novo arquivo (o
arquivo original não é apagado). Para sair do editor, salvando o arquivo
atual, digite `:x` (ou `:wq`).

| Comando | Descrição |
|---------|-----------|
| `:w` | salva |
| `:wq` | salva e sai |
| `:w nome` | salvar como |
| `:saveas nome` | salvar como |
| `:sav nome` | mesmo que "saveas nome" |
| `:x` | salva se existirem modificações |
| `:10,20 w! ~/Desktop/teste.txt` | salva um trecho para outro arquivo |
| `:w!` | salvamento forçado |
| `:e!` | reinicia a edição ignorando alterações |

