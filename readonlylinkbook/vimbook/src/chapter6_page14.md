O comando global “g”
--------------------

Buscando um padrão e gravando em outro arquivo:
```
:'a,'b g/^Error/ . w >> errors.txt
```
Apenas imprimir linhas que contém determinada palavra, isto é útil
quando você quer ter uma visão sobre um determina aspecto do seu arquivo
vejamos:
```
:set nu ..... habilita numeração
:g/Error/p .. apenas mostra as linhas correspondentes
```
Para mostrar o as linhas correspondentes a um padrão, mesmo que a
numeração de linha não esteja habilitada use
`:g/padrão/\#`.

numerar linhas:
```
:let i=1 | g/^/s//\=i."\t"/ | let i=i+1
```
Outro modo de inserir números de linha
```
:%s/^/\=line('.').'  '

: ............ comando
% ............ em todo o arquivo
s ............ substituição
/ ............ inicio da busca
^ ............ começo de linha
/ ............ inicio da substituição
\=line('.') .. corresponde ao nº da linha atual
.'  ' ........ concatena um espaço após o nº
```
Para copiar linhas começadas com *Error* para o final do
arquivo faça:
```
:g/^Error/ copy $
```
Obs: O comando ‘copy’ pode ser abreviado ‘co’
ou ainda pode-se usar ‘t’ para mais detalhes:
```
:h co
```
Como adicionar um padrão copiado com ‘yy’ após um
determinado padrão?
```
:g/padrao/+put!
:g/padrao/.put='teste'
```
Entre as linhas que contiverem ‘fred’ e ‘joe’
substitua:
```
:g/fred/,/joe/s/isto/aquilo/gic
```
As opções ‘gic’ correspondem a *global*, *ignore
case* e *confirm*, podendo ser omitidas deixando só
o *global*.\

Pegar caracteres numéricos e jogar no final do arquivo:
```
:g/^\d\+.*/m $
```
Inverter a ordem das linhas do arquivo:
```
:g/^/m0
```
Apagar as linhas que contém Line commented:
```
:g/Line commented/d
```
Apagar todas as linhas comentadas
```
 :g/^\s*#/d
```
Copiar determinado padrão para um registrador:
```
:g/pattern/ normal "Ayy
```
Copiar linhas que contém um padrão e a linha subsequente para o final:
```
:g/padrão/;+1 copy $
```
Deletar linhas que não contenham um padrão:
```
:v/dicas/d  ..... deleta linhas que não contenham `dicas'
```
Incrementar números no começo da linha:
```
:.,20g/^\d/exe "normal! \<c-a>"
```
Sublinhar linhas começadas com *Chapter*:
```
:g/^Chapter/t.|s/./-/g

: ........ comando
g ........ global
/ ........ inicio de um padrão
^ ........ começo de linha
Chapter .. palavra literal
/ ........ fim do parão
t ........ copia
. ........ linha atual
s ........ substitua
/ ........ inicio de um padrão
. ........ qualquer caractere
/ ........ início da substituição
- ........ por traço
/ ........ fim da substituição
g ........ em todas as ocorrências
```
