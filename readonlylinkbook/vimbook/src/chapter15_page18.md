Criando seções *LaTeX*
----------------------

o comando abaixo substitui

```
==seção==
```

   por

```
\section{seção}
```

```
:.s/^==\s\?\([^=]*\)\s\?==/\\section{\1}/g

: ......... comando
. ......... linha atual
s ......... substitua
^ ......... começo de linha
== ........ dois sinais de igual
\s\? ...... seguido ou não de espaço
[^=] ...... não pode haver = (^ dentro de [] é negação)
* ......... diz que o que vem antes pode vir zero ou mais vezes
\s\? ...... seguido ou não de espaço
\\ ........ insere uma barra invertida
\1 ........ repete o primeiro trecho entre ()
```
