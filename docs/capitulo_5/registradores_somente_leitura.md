Registradores somente leitura ": . % \#"
------------------------------------
```
": ..... armazena o último comando
". ..... armazena uma cópia do último texto inserido
"% ..... contém o nome do arquivo corrente
"# ..... contém o nome do arquivo alternativo
```
Uma forma prática de usar registradores em modo de inserção é usando:
`Ctrl-r`
```
Ctrl-r % .... insere o nome do arquivo atual
Ctrl-r : .... insere o último comando digitado
Ctrl-r / .... insere a última busca efetuada
Ctrl-r a .... insere o registrador `a'
```
Em modo de inserção pode-se repetir a última inserção de texto
simplesmente pressionando:
```
Ctrl-a
```
