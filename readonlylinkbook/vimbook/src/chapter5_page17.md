Registradores nomeados de "a até z" ou "A até Z"
--------------------------------------------

Pode-se armazenar uma linha em modo normal assim:
```
"ayy
```
Desse modo o Vim guarda o conteúdo da linha no registrador 'a'
caso queira armazenar mais uma linha no registrador 'a' use
este comando:
```
"Add
```
Neste caso a linha corrente é apagada 'dd' e adicionada ao
final do registrador "a".
```
"ayip .. copia o parágrafo atual para o registrador "a"
"a ..... registrador a
y ...... yank (copia)
ip ..... inner paragraph (este parágrafo)
```
