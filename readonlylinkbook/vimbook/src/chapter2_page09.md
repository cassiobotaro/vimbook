Editando em modo de comando
---------------------------

Para mover um trecho usando o modo de comandos faça:
```
:10,20m $
```
O comando acima move `m` da linha 10 até a linha 20 para o
final `$`.
```
:g /palavra/ m 0
```
Move as linhas contendo ‘palavra’ para o começo (linha zero)
```
:10,20y a
```
Copia da linha ‘10’ até a linha ‘20’ para o registrador ‘a’
```
:56pu a
```
Cola o registrador ‘a’ na linha 56
```
:g/padrão/d
```
O comando acima deleta todas as linhas contendo a palavra ‘padrão’.

Podemos inverter a lógica do comando global `g`:
```
:g!/padrão/d
```
Não delete as linhas contendo padrão, ou seja, delete tudo menos as
linhas contendo a palavra ‘padrão’.
```
:v/padrão/d ........ apaga linhas que não contenham "padrão"
:v/\S/d ............ apaga linhas vazias
\S ................. significa "string"
```
A opção acima equivale a `:g!/padrão/d`. Para ler mais sobre o comando
“global” utilizado nesta seção veja o capítulo [O comando global "g"](../capitulo_6/o_comando_global_g.md).
```
:7,10copy $
```
Da linha 7 até a linha 10 copie para o final. Veja mais sobre edição no
modo de comando no capítulo [Buscas e Substituições](../capitulo_6/buscas_e_substituicoes.md).

#### Gerando sequências

Para inserir uma sequência de 1 a 10 à partir da linha inicial “zero”
fazemos:
```
:0put =range(1,10)
```
Caso queira inserir sequências como esta:
```
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
```
Usamos este comando:
```
:for i in range(1,5) | .put ='192.168.0.'.i | endfor
```

