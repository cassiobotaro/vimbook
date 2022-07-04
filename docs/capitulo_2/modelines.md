Modelines
---------

São um modo de guardar preferências no próprio arquivo, suas
preferências viajam literalmente junto com o arquivo, basta usar em uma
das 5 primeiras linhas ou na última linha do arquivo algo como:
```
# vim:ft=sh:
```
OBS: Você deve colocar um espaço entre a palavra `vim` e a
primeira coluna, ou seja, a palavra `vim` deve vir
precedida de um espaço, daí em diante cada opção fica assim:
```
:opção:
```
Por exemplo: posso salvar um arquivo com extensão `.sh` e dentro do
mesmo indicar no `modeline` algo como:
```
# vim:ft=txt:nu:
```
Apesar de usar a extensão `sh` o Vim reconhecerá este
arquivo como `txt`, e caso eu não tenha habilitado a
numeração, ainda assim o Vim usará por causa da opção `nu`.
Portanto o uso de `modelines` pode ser um grande recurso
para o seu dia-a-dia pois você pode coloca-las dentro dos comentários!
