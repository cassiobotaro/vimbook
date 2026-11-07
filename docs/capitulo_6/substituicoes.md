---
title: Substituições
---

Para fazer uma substituição, certifique-se de que está em modo normal e
em seguida use o comando ‘s’, conforme será explicado.

Para substituir “foo” por “bar” na linha atual:
```vim
:s/foo/bar
```
Para substituir “foo” por “bar” da primeira à décima linha do arquivo:
```vim
:1,10 s/foo/bar
```
Para substituir “foo” por “bar” da primeira à última linha do arquivo:
```vim
:1,$ s/foo/bar
```
Ou simplesmente:
```vim
:% s/foo/bar
```
No primeiro comando, `$` significa para o Vim o final do arquivo; no
segundo, `%` representa o arquivo atual.

O comando ‘s’ possui muitas opções que modificam seu
comportamento.
