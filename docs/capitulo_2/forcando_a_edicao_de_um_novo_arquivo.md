Forçando a edição de um novo arquivo
------------------------------------

O Vim, como qualquer outro editor, é muito exigente no que se refere a
alterações de arquivo. Ao tentar abandonar um arquivo editado e não
salvo, o Vim irá se certificar da ação. Para abrir um novo arquivo sem
salvar o antigo:
```
:enew!
```
O comando acima é uma abreviação de `edit new`. De modo
similar pode-se ignorar todas as alterações feitas desde a abertura do
arquivo:
```
:e!
```
