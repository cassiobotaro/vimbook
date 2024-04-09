Substituições
------------------

Para fazer uma busca, certifique-se de que está em modo normal, em
seguida digite use o comando ‘s’, conforme será explicado.

Para substituir “foo” por “bar” na linha atual:
```
:s/foo/bar
```
Para substituir “foo” por “bar” da primeira à décima linha do arquivo:
```
:1,10 s/foo/bar
```
Para substituir “foo” por “bar” da primeira à última linha do arquivo:
```
:1,$ s/foo/bar
```
Ou simplesmente:
```
:% s/foo/bar

$ ... significa para o Vim final do arquivo
% ... representa o arquivo atual
```
O comando ‘s’ possui muitas opções que modificam seu
comportamento.
