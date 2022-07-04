Copiar, Colar e Deletar
-----------------------

No modo normal, o ato de deletar ou eliminar o texto está associado à
letra `d`. No modo de inserção as teclas usuais também funcionam.
```
dd .... deleta linha atual
D ..... deleta restante da linha
d$ .... deleta do ponto atual até o final da linha
d^ .... deleta do cursor ao primeiro caractere não-nulo da linha
d0 .... deleta do cursor ao início da linha
```
Pode-se combinar o comando de deleção `d` com o comando de movimento
(considere o modo normal) para apagar até a próxima vírgula use:
`df,`.

Copiar está associado à letra `y`.
```
yy .... copia a linha atual
Y ..... copia a linha atual
ye .... copia do cursor ao fim da palavra
yb .... copia do começo da palavra ao cursor
```
O que foi deletado ou copiado pode ser colado:
```
p .... cola o que foi copiado ou deletado abaixo
P .... cola o que foi copiado ou deletado acima
[p ... cola o que foi copiado ou deletado antes do cursor
]p ... cola o que foi copiado ou deletado após o cursor
```
### Deletando uma parte do texto

O comando `d` remove o conteúdo para a memória.
```
x .... apaga o caractere sob o cursor
xp ... troca letras de lugar
ddp .. troca linhas de lugar
d5x .. apaga os próximos 5 caracteres
dd  .. apaga a linha atual
5dd .. apaga 5 linhas (também pode ser: d5d)
d5G .. apaga até a linha 5
dw  .. apaga uma palavra
5dw .. apaga 5 palavras (também pode ser: d5w)
dl  .. apaga uma letra (sinônimo: x)
5dl .. apaga 5 letras (também pode ser: d5l ou 5x)
d0  .. apaga até o início da linha
d^  .. apaga até o primeiro caractere da linha
d$  .. apaga até o final da linha (sinônimo: D)
dgg .. apaga até o início do arquivo
dG  .. apaga até o final do arquivo
D .... apaga o resto da linha
d% ... deleta até o próximo (,[,{
da" .. deleta aspas com conteúdo
```
Depois do texto ter sido colocado na memória, digite `p`
para ‘inserir’ o texto em uma outra posição. Outros comandos:
```
diw .. apaga palavra mesmo que não esteja posicionado no início
dip .. apaga o parágrafo atual
d4b .. apaga as quatro palavras anteriores
dfx .. apaga até o próximo ``x''
d/casa/+1 - deleta até a linha após a palavra casa
```
Trocando a letra `d` nos comandos acima por
`c` de *change* (mudanças) ao invés de deletar
será feita uma mudança de conteúdo. Por exemplo:
```
ciw .............. modifica uma palavra
cip .............. modifica um parágrafo
cis .............. modifica uma sentença
C ................ modifica até o final da linha
```

### Copiando sem deletar

O comando `y` (*yank*) permite copiar uma
parte do texto para a memória sem deletar. Existe uma semelhança muito
grande entre os comandos `y` e os comandos
`d`, um ativa a ‘cópia’ e outro a ‘exclusão’ de conteúdo,
suportando ambos quantificadores:
```
yy  .... copia a linha atual (sinônimo: Y)
5yy .... copia 5 linhas (também pode ser: y5y ou 5Y)
y/pat .. copia até `pat'
yw  .... copia uma palavra
5yw .... copia 5 palavras (também pode ser: y5w)
yl  .... copia uma letra
5yl .... copia 5 letras (também pode ser: y5l)
y^  .... copia da posição atual até o início da linha(sinônimo: y0)
y$  .... copia da posição atual até o final da linha
ygg .... copia da posição atual até o início do arquivo
yG  .... copia da posição atual até o final do arquivo
```
Digite `P` (p maiúsculo) para colar o texto recém copiado
na posição onde encontra-se o cursor, ou `p` para colar o
texto na posição imediatamente após o cursor.
```
yi" .... copia trecho entre aspas (atual - inner)
vip .... seleção visual para parágrafo atual `inner paragraph'
yip .... copia o parágrafo atual
yit .... copia a tag atual `inner tag' útil para arquivos HTML, XML, etc.
```
### Usando a área de transferência `Clipboard`

Exemplos para o modo visual:
```
Ctrl-insert .... copia área selecionada
Shift-insert ... cola o que está no clipboard
Ctrl-del ....... recorta para o clipboard
```
Caso obtenhamos erro ao colar textos da área de transferência usando os
comandos acima citados podemos usar outra alternativa. Os comandos
abaixo preservam a indentação[^1].
```
"+p ............ cola preservando indentação
"+y ............ copia área selecionada
```
Para evitar erros ao colar usando `Shift-insert` use este
comando `:set paste`.

### Removendo linhas duplicadas
```
:sort u
```


[^1]: Espaçamento entre o começo da linha e o início do texto
