Trabalhando com registradores
-----------------------------

Pode-se guardar trechos do que foi copiado ou apagado para registradores
distintos (área de transferência múltipla). Os registradores são indicados
por aspas seguido por uma letra. Exemplos: `"a`,
`"b`, `"c`, etc.

Como copiar o texto para um registrador? É simples: basta especificar o
nome do registrador antes:
```
"add ... apaga linha para o registrador "a"
"bdd ... apaga linha para o registrador "b"
"ap .... cola" o conteúdo do registrador "a"
"bp .... cola" o conteúdo do registrador "b"
"x3dd .. apaga 3 linhas para o registrador "x"
"ayy  .. copia linha para o registrador "a"
"a3yy .. copia 3 linhas para o registrador "a"
"ayw  .. copia uma palavra para o registrador "a"
"a3yw .. copia 3 palavras para o registrador "a"
```
No “modo de inserção”, como visto anteriormente, pode-se usar um atalho
para colar rapidamente o conteúdo de um registrador.
```
Ctrl-r (registrador)
```
Para colar o conteúdo do registrador ‘a’
```
Ctrl-r a
```
Para copiar a linha atual para a área de transferência
```
"+yy
```
Para colar da área de transferência
```
"+p
```
Para copiar o arquivo atual para a área de transferência
“*clipboard*”:
```
:%y+
```
