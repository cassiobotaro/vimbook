Abrindo o último arquivo rapidamente
------------------------------------

O Vim guarda um registrador para cada arquivo editado veja mais no capítulo [Registradores](../capitulo_5/registradores.md).
```
'0 ........ abre o último arquivo editado
'1 ........ abre o penúltimo arquivo editado
Ctrl-6 .... abre o arquivo alternativo (booleano)
```
Bom, já que abrimos o nosso último arquivo editado com o comando
```
'0
```
podemos, e provavelmente o faremos, editar no mesmo ponto em que
estávamos editando da última vez:
```
gi
```
Pode-se criar um `alias`[^1] para que ao abrir o vim o
mesmo abra o último arquivo editado:
`alias lvim="vim -c \"normal '0\""`. No capítulo [Buscas e Substituições](../capitulo_6/buscas_e_substituicoes.md) você encontra mais dicas de edição.


[^1]: Abreviação para um comando do GNU/Linux
